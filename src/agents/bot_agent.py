import json
from typing import List, Dict, Any
from src.config import Config, EMERGENCY_PLAYBOOKS

class CyberShieldBotAgent:
    """
    Interactive Cyber Fraud Emergency & Security Advisor AI Bot.
    Provides immediate incident guidance, threat mitigation checklists,
    and conversational Q&A to protect users against active fraud.
    """
    
    def __init__(self):
        self.name = "Cyber Shield Bot"
        self.role = "Cyber Security & Fraud Emergency Advisor"
        self.system_prompt = """
You are Cyber Shield Bot, an empathetic, highly knowledgeable, and authoritative Cyber Security & Fraud Emergency AI Advisor.
Your objective:
1. Provide immediate, clear, actionable instructions to individuals facing suspected or active cyber fraud (bank scams, phishing, voice spoofing, OTP theft).
2. Maintain a reassuring, calm, and security-focused tone.
3. List step-by-step emergency actions first (e.g., call 1930 / bank helpline, freeze cards, report fraud).
4. Explain the scam mechanism clearly so the user learns how to avoid future traps.
"""

    def respond(self, message: str, chat_history: List[Dict[str, str]] = None) -> str:
        if not message or not message.strip():
            return "Hello! I am **Cyber Shield Bot**. How can I help protect you or investigate a cyber threat today?"

        if chat_history is None:
            chat_history = []

        # Try Groq Free API first
        if Config.is_groq_available():
            try:
                return self._respond_with_groq(message, chat_history)
            except Exception as e:
                print(f"[BotAgent] Groq API call failed: {e}. Using fallback Security KB Engine.")

        # Fallback Knowledge Base Response
        return self._respond_with_knowledge_base(message)

    def _respond_with_groq(self, message: str, chat_history: List[Dict[str, str]]) -> str:
        from groq import Groq
        client = Groq(api_key=Config.GROQ_API_KEY)
        
        messages = [{"role": "system", "content": self.system_prompt}]
        for item in chat_history[-6:]:
            messages.append({"role": item.get("role", "user"), "content": item.get("content", "")})
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=600
        )
        
        return response.choices[0].message.content

    def _respond_with_knowledge_base(self, message: str) -> str:
        msg_lower = message.lower()
        
        # Check against emergency categories
        if any(k in msg_lower for k in ["otp", "pin", "shared code", "bank password"]):
            playbook = "\n".join(f"- {step}" for step in EMERGENCY_PLAYBOOKS["Shared OTP / PIN"])
            return f"""🚨 **EMERGENCY ACTION REQUIRED: Shared OTP / PIN**

If you have shared an OTP, PIN, or banking password with an unverified party, take these steps RIGHT NOW:

{playbook}

💡 **Security Insight:** Legitimate banks and government officials will NEVER request your OTP or PIN over phone or chat."""

        elif any(k in msg_lower for k in ["link", "clicked", "url", "website"]):
            playbook = "\n".join(f"- {step}" for step in EMERGENCY_PLAYBOOKS["Clicked Suspicious Link"])
            return f"""⚠️ **URGENT STEPS: Clicked Suspicious Link**

Follow this safety protocol immediately:

{playbook}

💡 **Security Insight:** Fraudulent links often mimic official web domains using tiny typos (e.g. `secur-bank.com` instead of `bank.com`)."""

        elif any(k in msg_lower for k in ["voice", "call", "cloned", "audio", "police", "customs"]):
            playbook = "\n".join(f"- {step}" for step in EMERGENCY_PLAYBOOKS["Simulated Voice / Impersonation Call"])
            return f"""📞 **TACTICAL STEPS: Impersonation / Voice Scam Call**

If you received a suspicious call or fake authority threat:

{playbook}

💡 **Security Insight:** Scammers use AI voice cloning and caller ID spoofing to impersonate relatives or law enforcement officers."""

        elif any(k in msg_lower for k in ["money", "lost", "transferred", "fraud", "paid"]):
            playbook = "\n".join(f"- {step}" for step in EMERGENCY_PLAYBOOKS["Financial Loss / Transfer Sent"])
            return f"""🚨 **FINANCIAL RECOVERY PROTOCOL**

Act quickly to maximize chances of fund freezing & recovery:

{playbook}

💡 **Security Insight:** Reporting within the first 1-2 hours ("golden hours") drastically increases the chance of banks freezing fraudulent recipient accounts."""

        # Default Helpful Advisor Response
        return f"""🛡️ **Cyber Shield Advisor Guidance**

Thank you for reaching out. Here is standard protocol for evaluating potential cyber threats:

1. **Verify Sender Identity:** Always verify calls, emails, or messages through official customer care numbers listed on official websites.
2. **Never Share Credentials:** Never reveal OTPs, PINs, passwords, or CVV numbers.
3. **Inspect URLs carefully:** Do not log in through links sent in SMS or WhatsApp.
4. **Report Suspicious Incidents:** File reports on official cyber crime portals (e.g. cybercrime.gov.in or hotline 1930).

You can also use our **Text Scanner** or **Voice AI Scanner** tabs to analyze suspicious messages or voice recordings! How else can I assist you?"""
