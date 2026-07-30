import sqlite3
import os
import secrets
import hashlib
from typing import Dict, Any, Optional, Tuple

class DatabaseManager:
    """
    Thread-safe SQLite Database Manager for Cyber Fraud Shield.
    Handles user authentication (salted PBKDF2 SHA-256 password hashing)
    and user personal profile records.
    """

    def __init__(self, db_path: str = None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(base_dir, "cyber_shield.db")
        
        self.db_path = db_path
        self.init_db()

    def _get_connection(self) -> sqlite3.Connection:
        """Establishes a database connection with PRAGMA foreign_keys enabled."""
        conn = sqlite3.connect(self.db_path, timeout=10.0)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self):
        """Creates 'users' and 'user_profiles' tables if they do not exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Table 1: users (Authentication credentials)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            # Table 2: user_profiles (Personal details page)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                age INTEGER,
                mobile_number TEXT NOT NULL,
                address TEXT DEFAULT '',
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
            """)
            conn.commit()

    def _hash_password(self, password: str, salt: bytes = None) -> Tuple[str, str]:
        """Hashes password using PBKDF2-HMAC-SHA256 with 100,000 iterations."""
        if salt is None:
            salt = secrets.token_bytes(16)
        
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return pwd_hash.hex(), salt.hex()

    def _verify_password(self, password: str, password_hash_hex: str, salt_hex: str) -> bool:
        """Verifies candidate password against stored salt and hash."""
        salt = bytes.fromhex(salt_hex)
        pwd_hash_hex, _ = self._hash_password(password, salt)
        return secrets.compare_digest(pwd_hash_hex, password_hash_hex)

    def register_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str,
        age: int,
        mobile_number: str,
        address: str = ""
    ) -> Tuple[bool, str]:
        """
        Registers a new user and creates their personal profile record inside a single SQL transaction.
        Returns (success_boolean, message).
        """
        username = username.strip()
        email = email.strip().lower()
        full_name = full_name.strip()
        mobile_number = mobile_number.strip()

        if not username or not email or not password or not full_name or not mobile_number:
            return False, "All required fields (username, email, password, full name, mobile number) must be filled."

        pwd_hash, salt_hex = self._hash_password(password)

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # Check for existing username/email
                cursor.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
                if cursor.fetchone():
                    return False, "Username or Email is already registered."

                # Insert into users table
                cursor.execute(
                    "INSERT INTO users (username, email, password_hash, salt) VALUES (?, ?, ?, ?)",
                    (username, email, pwd_hash, salt_hex)
                )
                user_id = cursor.lastrowid

                # Insert into user_profiles table
                cursor.execute(
                    "INSERT INTO user_profiles (user_id, full_name, age, mobile_number, address) VALUES (?, ?, ?, ?, ?)",
                    (user_id, full_name, age, mobile_number, address)
                )
                conn.commit()
                return True, "Account registered successfully! Please log in."
        except sqlite3.IntegrityError as e:
            return False, f"Database Integrity Error: {e}"
        except Exception as e:
            return False, f"Registration failed: {e}"

    def authenticate_user(self, username_or_email: str, password: str) -> Tuple[Optional[Dict[str, Any]], str]:
        """
        Authenticates user by username or email.
        Returns (user_dict_or_None, status_message).
        """
        identifier = username_or_email.strip().lower()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.id, u.username, u.email, u.password_hash, u.salt,
                       p.full_name, p.age, p.mobile_number, p.address
                FROM users u
                JOIN user_profiles p ON u.id = p.user_id
                WHERE LOWER(u.username) = ? OR LOWER(u.email) = ?
            """, (identifier, identifier))
            
            row = cursor.fetchone()
            if not row:
                return None, "Invalid Username/Email or Password."

            if self._verify_password(password, row["password_hash"], row["salt"]):
                user_data = {
                    "user_id": row["id"],
                    "username": row["username"],
                    "email": row["email"],
                    "full_name": row["full_name"],
                    "age": row["age"],
                    "mobile_number": row["mobile_number"],
                    "address": row["address"]
                }
                return user_data, "Login successful!"

            return None, "Invalid Username/Email or Password."

    def get_user_profile(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Retrieves user profile by user_id."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.id, u.username, u.email, u.created_at,
                       p.full_name, p.age, p.mobile_number, p.address, p.updated_at
                FROM users u
                JOIN user_profiles p ON u.id = p.user_id
                WHERE u.id = ?
            """, (user_id,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None

    def update_user_profile(
        self,
        user_id: int,
        full_name: str,
        age: int,
        mobile_number: str,
        address: str
    ) -> Tuple[bool, str]:
        """Updates personal details in user_profiles table."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE user_profiles
                    SET full_name = ?, age = ?, mobile_number = ?, address = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ?
                """, (full_name.strip(), age, mobile_number.strip(), address.strip(), user_id))
                conn.commit()
                return True, "Profile updated successfully!"
        except Exception as e:
            return False, f"Failed to update profile: {e}"
