import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:crypto/crypto.dart';

class ApiService {
  // Base URL for Python Backend API
  static const String baseUrl = 'http://127.0.0.1:8501';

  /// Generates a deterministic SHA-256 Idempotency Key
  static String generateIdempotencyKey(String content, String prefix) {
    final bytes = utf8.encode(content.trim().toLowerCase());
    final digest = sha256.convert(bytes).toString();
    return '$prefix:$digest';
  }

  /// Text Scam Analysis Endpoint
  static Future<Map<String, dynamic>> analyzeText(String text) async {
    final key = generateIdempotencyKey(text, 'text_scan');
    
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/analyze_text'),
        headers: {
          'Content-Type': 'application/json',
          'X-Idempotency-Key': key,
        },
        body: jsonEncode({
          'text': text,
          'idempotency_key': key,
        }),
      ).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      }
    } catch (e) {
      // Fallback offline heuristic calculation if backend server is not running directly
      return _localHeuristicAnalysis(text, key);
    }

    return _localHeuristicAnalysis(text, key);
  }

  /// Cyber Shield Bot Advice Endpoint
  static Future<String> getBotAdvice(String prompt, List<Map<String, String>> history) async {
    final key = generateIdempotencyKey(prompt, 'bot_response');

    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/bot_respond'),
        headers: {
          'Content-Type': 'application/json',
          'X-Idempotency-Key': key,
        },
        body: jsonEncode({
          'message': prompt,
          'history': history,
          'idempotency_key': key,
        }),
      ).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['response_text'] ?? 'Security advisory generated.';
      }
    } catch (e) {
      return _localBotFallback(prompt);
    }

    return _localBotFallback(prompt);
  }

  /// Local Fallback Heuristic Analysis
  static Map<String, dynamic> _localHeuristicAnalysis(String text, String key) {
    final lower = text.toLowerCase();
    int risk = 15;
    List<String> tactics = [];
    List<String> signs = [];

    if (lower.contains('urgent') || lower.contains('immediately') || lower.contains('24 hours')) {
      risk += 35;
      tactics.add('Artificial Urgency Tactics');
      signs.add('Pressuring time limit designed to induce panic');
    }

    if (lower.contains('bank') || lower.contains('otp') || lower.contains('pin') || lower.contains('card')) {
      risk += 40;
      tactics.add('Credential & OTP Harvesting');
      signs.add('Requests sensitive banking details / OTP');
    }

    if (lower.contains('http://') || lower.contains('https://') || lower.contains('bit.ly')) {
      risk += 20;
      tactics.add('Suspicious Unverified Web Link');
      signs.add('Redirects to external unverified portal');
    }

    final int riskScore = risk > 100 ? 100 : risk;
    final String level = riskScore < 30 ? 'Safe' : (riskScore < 60 ? 'Caution' : 'Critical Threat');

    return {
      'risk_score': riskScore,
      'threat_level': level,
      'scam_type': lower.contains('bank') ? 'Bank / Financial Impersonation' : 'Suspicious Communication',
      'matched_tactics': tactics.isEmpty ? ['Standard Rule Scan Completed'] : tactics,
      'key_warning_signs': signs.isEmpty ? ['No obvious threat patterns detected.'] : signs,
      'actionable_advice': 'Do not click links or share OTPs. Call National Cyber Crime Helpline 1930.',
      'idempotent_hit': false,
      'idempotency_key': key,
    };
  }

  /// Local Fallback Bot Guidance
  static String _localBotFallback(String prompt) {
    final lower = prompt.toLowerCase();
    if (lower.contains('otp') || lower.contains('pin')) {
      return '''🚨 **EMERGENCY ACTION PROTOCOL: OTP Theft / Shared PIN**

1. **Immediate Action (First 5 Minutes):** Call your bank fraud hotline immediately to block your debit/credit cards and disable NetBanking.
2. **Change Passwords:** Immediately update passwords for online banking and UPI apps from a secure device.
3. **Official Report:** File a report at https://cybercrime.gov.in or call National Helpline `1930`.

📞 **Official National Cyber Hotline:** `1930`''';
    }

    return '''🛡️ **Cyber Shield Advisor Protocol**

1. **Verify Identity:** Never trust urgent caller demands. Call customer service on official website numbers.
2. **Protect Credentials:** Never reveal OTPs, PINs, or CVV.
3. **Report Incidents:** Register complaints on `cybercrime.gov.in` or helpline `1930`.''';
  }
}
