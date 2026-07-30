import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

class TopGovBar extends StatelessWidget {
  const TopGovBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 38,
      color: AppColors.govGreen,
      padding: const EdgeInsets.symmetric(horizontal: 24),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              const Text('🇮🇳', style: TextStyle(fontSize: 16)),
              const SizedBox(width: 8),
              Text(
                'GOVERNMENT OF INDIA  •  MINISTRY OF HOME AFFAIRS',
                style: GoogleFonts.notoSans(
                  color: Colors.white,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 0.5,
                ),
              ),
            ],
          ),
          Row(
            children: [
              Text(
                'National Cyber Crime Helpline: 1930',
                style: GoogleFonts.notoSans(
                  color: Colors.white,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(width: 16),
              const Icon(Icons.language, color: Colors.white, size: 16),
              const SizedBox(width: 4),
              Text(
                'English / हिंदी',
                style: GoogleFonts.notoSans(
                  color: Colors.white,
                  fontSize: 12,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
