import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';
import '../services/api_service.dart';

class TextScannerView extends StatefulWidget {
  const TextScannerView({super.key});

  @override
  State<TextScannerView> createState() => _TextScannerViewState();
}

class _TextScannerViewState extends State<TextScannerView> {
  final TextEditingController _controller = TextEditingController();
  bool _isLoading = false;
  Map<String, dynamic>? _result;

  final Map<String, String> _samples = {
    'Select Sample...': '',
    'Bank OTP Scam':
        'URGENT: Your HDFC bank account ending in 4921 has been blocked due to missing KYC. Click http://hdfc-verify-update.com immediately to unblock within 24 hours.',
    'Courier Delivery Scam':
        'FedEx Express: Package #IND9841 could not be delivered due to unpaid customs fee of \$5. Pay now at http://bit.ly/fedex-custom-pay or parcel will be returned.',
    'Prize Fraud Scam':
        'Congratulations! You have won \$50,000 in the Amazon Lucky Draw. Reply with your bank account number and UPI ID to claim your prize.',
  };

  void _scanText() async {
    final text = _controller.text.trim();
    if (text.isEmpty) return;

    setState(() {
      _isLoading = true;
      _result = null;
    });

    final res = await ApiService.analyzeText(text);

    setState(() {
      _isLoading = false;
      _result = res;
    });
  }

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Icon(Icons.center_focus_strong, color: AppColors.primaryBlue, size: 28),
              const SizedBox(width: 12),
              Text(
                'Text Scam & Phishing Scanner',
                style: GoogleFonts.notoSans(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                  color: AppColors.textDark,
                ),
              ),
            ],
          ),
          Text(
            'Scan suspicious SMS messages, WhatsApp chats, emails, or call transcripts for fraud tactics.',
            style: GoogleFonts.notoSans(color: AppColors.textMuted, fontSize: 13),
          ),
          const SizedBox(height: 20),

          // Dropdown for Sample Texts
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: Colors.grey.shade300),
            ),
            child: DropdownButtonHideUnderline(
              child: DropdownButton<String>(
                isExpanded: true,
                value: _samples.keys.first,
                items: _samples.keys.map((String key) {
                  return DropdownMenuItem<String>(
                    value: key,
                    child: Text('Load Sample: $key', style: GoogleFonts.notoSans(fontSize: 13)),
                  );
                }).toList(),
                onChanged: (String? val) {
                  if (val != null && _samples[val]!.isNotEmpty) {
                    setState(() {
                      _controller.text = _samples[val]!;
                    });
                  }
                },
              ),
            ),
          ),
          const SizedBox(height: 12),

          // Text Area Input
          TextField(
            controller: _controller,
            maxLines: 5,
            decoration: InputDecoration(
              hintText: 'Paste suspicious text, SMS, or email content here...',
              fillColor: Colors.white,
              filled: true,
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
                borderSide: BorderSide(color: Colors.grey.shade300),
              ),
            ),
          ),
          const SizedBox(height: 16),

          // Scan Button
          SizedBox(
            width: double.infinity,
            height: 48,
            child: ElevatedButton.icon(
              onPressed: _isLoading ? null : _scanText,
              icon: _isLoading
                  ? const SizedBox(
                      width: 20,
                      height: 20,
                      child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2),
                    )
                  : const Icon(Icons.search),
              label: Text(
                _isLoading ? 'Scanning Text...' : 'Scan Message for Cyber Fraud',
                style: GoogleFonts.notoSans(fontWeight: FontWeight.bold, fontSize: 15),
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.primaryBlue,
                foregroundColor: Colors.white,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
              ),
            ),
          ),

          // Analysis Output Card
          if (_result != null) ...[
            const SizedBox(height: 24),
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.grey.shade300),
                boxShadow: [
                  BoxShadow(color: Colors.black.withOpacity(0.05), blurRadius: 10),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (_result!['idempotent_hit'] == true)
                    Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: AppColors.primaryBlue.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        '⚡ Idempotent Cache Hit (Pre-computed result)',
                        style: GoogleFonts.notoSans(
                          color: AppColors.primaryBlue,
                          fontWeight: FontWeight.bold,
                          fontSize: 12,
                        ),
                      ),
                    ),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Threat Risk Score: ${_result!['risk_score']} / 100',
                        style: GoogleFonts.notoSans(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: _getThreatColor(_result!['threat_level']),
                        ),
                      ),
                      Chip(
                        label: Text(_result!['threat_level'], style: const TextStyle(color: Colors.white)),
                        backgroundColor: _getThreatColor(_result!['threat_level']),
                      ),
                    ],
                  ),
                  const Divider(height: 24),

                  Text('Scam Category: ${_result!['scam_type']}',
                      style: GoogleFonts.notoSans(fontWeight: FontWeight.bold, fontSize: 14)),
                  const SizedBox(height: 8),

                  Text('Matched Tactics & Red Flags:',
                      style: GoogleFonts.notoSans(fontWeight: FontWeight.bold, fontSize: 13)),
                  ...(_result!['matched_tactics'] as List).map(
                    (tactic) => Padding(
                      padding: const EdgeInsets.only(top: 4),
                      child: Text('• ⚠️ $tactic', style: GoogleFonts.notoSans(fontSize: 13)),
                    ),
                  ),

                  const SizedBox(height: 16),
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: AppColors.backgroundLight,
                      borderRadius: BorderRadius.circular(8),
                      border: const Border(left: BorderSide(color: AppColors.primaryBlue, width: 4)),
                    ),
                    child: Text(
                      '💡 Actionable Advice: ${_result!['actionable_advice']}',
                      style: GoogleFonts.notoSans(fontSize: 13, fontWeight: FontWeight.w600),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }

  Color _getThreatColor(String level) {
    switch (level) {
      case 'Safe':
        return AppColors.threatSafe;
      case 'Caution':
        return AppColors.threatCaution;
      default:
        return AppColors.threatCritical;
    }
  }
}
