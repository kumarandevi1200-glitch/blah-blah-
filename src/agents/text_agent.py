import re
import json
from typing import Dict, Any, List
from src.config import Config, SCAM_INDICATORS

class TextScamDetectorAgent:
    """
    AI Agent responsible for scanning text messages, emails, and call transcripts
    for cyber fraud indicators, phishing patterns, and authority impersonation.
    Supports both Free API Mode (Groq Llama-3.3-70B / Gemini) and Heuristic Engine Fallback.
    """
    
    def __init__(self):
        self.name = "Text Scam Detector Agent"
        self.role = "Cyber Fraud Content & Phishing Analyzer"
        
    def analyze(self, text: str) -> Dict[str, Any]:
        if not text or not text.strip():
            return {
                "error": "Empty input provided",
                "risk_score": 0,
                "threat_level": "Safe",
                "scam_type": "None",
                "indicators": [],
                "explanation": "No text content was submitted for evaluation.",
                "recommendation": "Paste suspect text to run cyber fraud analysis."
            }

        # Try Groq Free API first if key exists
        if Config.is_groq_available():
            try:
                return self._analyze_with_groq(text)
            except Exception as e:
                # Fallback to local heuristic engine on API failure
                print(f"[TextAgent] Groq API call failed: {e}. Falling back to Heuristic Engine.")

        # Fallback to Heuristic Engine
        return self._analyze_with_heuristics(text)

    def _analyze_with_groq(self, text: str) -> Dict[str, Any]:
        from groq import Groq
        client = Groq(api_key=Config.GROQ_API_KEY)
        
        prompt = f"""
You are Cyber Fraud Shield's Text Scam Detector Agent.
Analyze the following input message/transcript for potential cyber fraud, phishing, social engineering, or scam tactics.

Input Text:
\"\"\"{text}\"\"\"

Return ONLY a valid JSON object with the following fields:
{{
    "risk_score": (integer 0 to 100),
    "threat_level": ("Safe", "Caution", "High Alert", "Critical Threat"),
    "scam_type": ("Bank Impersonation", "Courier/Delivery Scam", "Lottery/Prize Fraud", "Tech Support Scam", "Urgent Phishing", "Job Fraud", "Legitimate / Clean"),
    "matched_tactics": [list of strings detailing tactics found, e.g., "Artificial Urgency", "Suspicious URL", "Credential Request"],
    "summary": "Brief 1-2 sentence executive summary of the threat level and tactics.",
    "key_warning_signs": [list of 2-4 bullet points highlighting specific red flags in the message],
    "actionable_advice": "Immediate steps the recipient must take."
}}
"""
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a cyber security threat analyst agent. Return raw valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        data["engine_used"] = "Groq Llama-3.3-70B (Free API)"
        return data

    def _analyze_with_heuristics(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        matched_indicators: List[str] = []
        score = 0
        
        # Check categories
        for category, keywords in SCAM_INDICATORS.items():
            found = [kw for kw in keywords if kw in text_lower]
            if found:
                matched_indicators.append(f"{category.replace('_', ' ').title()}: matched '{', '.join(found[:3])}'")
                score += len(found) * 18

        # URL check
        urls = re.findall(r'https?://\S+|www\.\S+', text_lower)
        if urls:
            matched_indicators.append(f"Contains Links: {len(urls)} web link(s) detected")
            score += 25
            
        # Urgency + Money combo
        if any(w in text_lower for w in SCAM_INDICATORS["urgency"]) and any(w in text_lower for w in SCAM_INDICATORS["financial"]):
            score += 20
            matched_indicators.append("High Threat Combo: Artificial Urgency + Financial Demands")

        # Clamp risk score
        risk_score = min(100, max(5, score))

        # Threat classification
        if risk_score < 25:
            threat_level = "Safe"
            scam_type = "Legitimate / Clean"
        elif risk_score < 55:
            threat_level = "Caution"
            scam_type = "Suspicious Communication"
        elif risk_score < 80:
            threat_level = "High Alert"
            scam_type = "Phishing / Social Engineering"
        else:
            threat_level = "Critical Threat"
            scam_type = "High-Risk Cyber Scam"

        # Determine scam type guess
        if "bank" in text_lower or "otp" in text_lower or "card" in text_lower:
            scam_type = "Bank / Financial Impersonation"
        elif "fedex" in text_lower or "dhl" in text_lower or "customs" in text_lower or "package" in text_lower:
            scam_type = "Courier / Delivery Scam"
        elif "lottery" in text_lower or "prize" in text_lower or "won" in text_lower:
            scam_type = "Lottery / Prize Scam"
        elif "support" in text_lower or "virus" in text_lower or "anydesk" in text_lower:
            scam_type = "Tech Support / Remote Access Scam"

        warning_signs = []
        if any("urgency" in ind for ind in matched_indicators):
            warning_signs.append("Pressuring time limit designed to stop logical evaluation.")
        if any("financial" in ind for ind in matched_indicators):
            warning_signs.append("Requests or mentions sensitive banking details / OTPs.")
        if urls:
            warning_signs.append("Embedded link redirects to an unverified external website.")
        if not warning_signs:
            warning_signs.append("No obvious threat patterns detected in standard rule checks.")

        return {
            "risk_score": risk_score,
            "threat_level": threat_level,
            "scam_type": scam_type,
            "matched_tactics": matched_indicators if matched_indicators else ["Standard pattern check completed"],
            "summary": f"Text parsed with a risk rating of {risk_score}/100. Threat Classification: {threat_level}.",
            "key_warning_signs": warning_signs,
            "actionable_advice": "Do not click links or share OTPs. Verify caller/sender through official phone numbers listed on legitimate websites.",
            "engine_used": "Built-in Heuristic Fraud Engine (Simulation Fallback)"
        }
