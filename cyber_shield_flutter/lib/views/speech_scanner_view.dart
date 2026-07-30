import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

class SpeechScannerView extends StatefulWidget {
  const SpeechScannerView({super.key});

  @override
  State<SpeechScannerView> createState() => _SpeechScannerViewState();
}

class _SpeechScannerViewState extends State<SpeechScannerView> {
  String _selectedSample = 'Sample 1: Fake Bank Urgent Call';
  bool _isAnalyzing = false;
  Map<String, dynamic>? _analysisResult;

  final List<String> _samples = [
    'Sample 1: Fake Bank Urgent Call',
    'Sample 2: Customs Seizure Threat',
    'Sample 3: Family Emergency Impersonation',
  ];

  void _runVoiceAnalysis() {
    setState(() {
      _isAnalyzing = true;
      _analysisResult = null;
    });

    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        _isAnalyzing = false;
        _analysisResult = {
          'transcription':
              'Emergency alert from your bank security team. Your online banking account has been temporarily disabled due to suspicious login attempts. Speak your 6 digit OTP to unblock.',
          'synthetic_confidence': 88,
          'is_synthetic': true,
          'voice_nature': '⚠️ AI Cloned / Synthetic Voice Detected',
          'overall_risk_score': 92,
          'threat_level': 'Critical Threat',
          'artifacts': [
            'Phase jitter in high frequencies',
            'Artificial pitch micro-flattening',
            'Absence of human breath pauses',
          ],
        };
      });
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
              const Icon(Icons.graphic_eq, color: Colors.purple, size: 28),
              const SizedBox(width: 12),
              Text(
                'Speech & AI Voice Spoof Scanner',
                style: GoogleFonts.notoSans(
                  fontSize: 22,
                  fontWeight: FontWeight.bold,
                  color: AppColors.textDark,
                ),
              ),
            ],
          ),
          Text(
            'Upload audio clips or select test voice clips to detect AI-cloned deepfake voice signatures.',
            style: GoogleFonts.notoSans(color: AppColors.textMuted, fontSize: 13),
          ),
          const SizedBox(height: 20),

          // Upload or Select Sample Card
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.grey.shade300),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Select Test Audio Recording:', style: GoogleFonts.notoSans(fontWeight: FontWeight.bold, fontSize: 14)),
                const SizedBox(height: 10),
                DropdownButton<String>(
                  isExpanded: true,
                  value: _selectedSample,
                  items: _samples.map((String s) {
                    return DropdownMenuItem<String>(value: s, child: Text(s));
                  }).toList(),
                  onChanged: (val) {
                    if (val != null) setState(() => _selectedSample = val);
                  },
                ),
                const SizedBox(height: 16),
                SizedBox(
                  width: double.infinity,
                  height: 48,
                  child: ElevatedButton.icon(
                    onPressed: _isAnalyzing ? null : _runVoiceAnalysis,
                    icon: const Icon(Icons.analytics),
                    label: Text(
                      _isAnalyzing ? 'Analyzing Voice Forensics...' : 'Run Voice Acoustic & Fraud Forensics',
                      style: GoogleFonts.notoSans(fontWeight: FontWeight.bold),
                    ),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Forensic Results
          if (_analysisResult != null) ...[
            const SizedBox(height: 24),
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppColors.threatCritical, width: 2),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    _analysisResult!['voice_nature'],
                    style: GoogleFonts.notoSans(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: AppColors.threatCritical,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'AI Synthetic Confidence: ${_analysisResult!['synthetic_confidence']}%',
                        style: GoogleFonts.notoSans(fontWeight: FontWeight.bold),
                      ),
                      Text(
                        'Voice Threat Score: ${_analysisResult!['overall_risk_score']}/100',
                        style: GoogleFonts.notoSans(fontWeight: FontWeight.bold, color: AppColors.threatCritical),
                      ),
                    ],
                  ),
                  const Divider(height: 24),
                  Text('Speech-to-Text Transcription:', style: GoogleFonts.notoSans(fontWeight: FontWeight.bold)),
                  const SizedBox(height: 4),
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: AppColors.backgroundLight,
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text('"${_analysisResult!['transcription']}"', style: GoogleFonts.notoSans(fontStyle: FontStyle.italic)),
                  ),
                  const SizedBox(height: 12),
                  Text('Detected Acoustic Artifacts:', style: GoogleFonts.notoSans(fontWeight: FontWeight.bold)),
                  ...(_analysisResult!['artifacts'] as List).map(
                    (art) => Text('• ⚠️ $art', style: GoogleFonts.notoSans(fontSize: 13)),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }
}
