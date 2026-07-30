import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

class HeroBanner extends StatelessWidget {
  final VoidCallback onTextScanPressed;
  final VoidCallback onVoiceScanPressed;

  const HeroBanner({
    super.key,
    required this.onTextScanPressed,
    required this.onVoiceScanPressed,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 36),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(16),
        gradient: const LinearGradient(
          colors: [
            AppColors.govNavyDark,
            AppColors.govNavyMedium,
            AppColors.govNavyLight,
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        boxShadow: [
          BoxShadow(
            color: AppColors.govNavyDark.withOpacity(0.4),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Stack(
        children: [
          // Background Shield Watermark Pattern
          Positioned(
            right: -20,
            bottom: -20,
            child: Icon(
              Icons.shield_outlined,
              size: 240,
              color: Colors.white.withOpacity(0.04),
            ),
          ),
          
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Badge
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.12),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white24),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Text('🇮🇳', style: TextStyle(fontSize: 14)),
                    const SizedBox(width: 6),
                    Text(
                      'INDIAN CYBER CRIME COORDINATION CENTRE (I4C)',
                      style: GoogleFonts.notoSans(
                        color: Colors.white,
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.8,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              
              // Headline
              Text(
                'AI-Powered Cyber Security & Emergency Defense',
                style: GoogleFonts.notoSans(
                  color: Colors.white,
                  fontSize: 26,
                  fontWeight: FontWeight.w800,
                  height: 1.2,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                'Instant Fraud Text Scanning • AI Voice Spoof Analysis • Zero-Hallucination RAG Emergency Advisor',
                style: GoogleFonts.notoSans(
                  color: Colors.white70,
                  fontSize: 14,
                  fontWeight: FontWeight.w400,
                ),
              ),
              const SizedBox(height: 24),

              // Action Buttons
              Wrap(
                spacing: 12,
                runSpacing: 12,
                children: [
                  ElevatedButton.icon(
                    onPressed: onTextScanPressed,
                    icon: const Icon(Icons.search, size: 18),
                    label: Text(
                      'Scan Suspicious Text / SMS',
                      style: GoogleFonts.notoSans(fontWeight: FontWeight.bold),
                    ),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppColors.primaryBlue,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                    ),
                  ),
                  OutlinedButton.icon(
                    onPressed: onVoiceScanPressed,
                    icon: const Icon(Icons.graphic_eq, size: 18),
                    label: Text(
                      'Verify Voice Recording (Deepfake Detector)',
                      style: GoogleFonts.notoSans(fontWeight: FontWeight.bold),
                    ),
                    style: OutlinedButton.styleFrom(
                      foregroundColor: Colors.white,
                      side: const BorderSide(color: Colors.white70),
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}
