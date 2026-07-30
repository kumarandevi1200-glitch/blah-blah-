import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';

class PortalHeader extends StatelessWidget {
  final int selectedIndex;
  final Function(int) onTabSelected;

  const PortalHeader({
    super.key,
    required this.selectedIndex,
    required this.onTabSelected,
  });

  @override
  Widget build(BuildContext context) {
    final isMobile = MediaQuery.of(context).size.width < 850;

    return Container(
      color: Colors.white,
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      decoration: BoxDecoration(
        color: Colors.white,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.05),
            blurRadius: 4,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          // Left: Emblem & Bilingual Titles
          Row(
            children: [
              // Emblem & I4C Icon Stack
              Container(
                width: 48,
                height: 48,
                decoration: BoxDecoration(
                  color: AppColors.govNavyDark,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Center(
                  child: Text('🇮🇳', style: TextStyle(fontSize: 24)),
                ),
              ),
              const SizedBox(width: 14),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'राष्ट्रीय साइबर अपराध रिपोर्टिंग पोर्टल',
                    style: GoogleFonts.notoSans(
                      fontSize: 14,
                      fontWeight: FontWeight.bold,
                      color: AppColors.textDark,
                    ),
                  ),
                  Text(
                    'National Cyber Crime Reporting Portal',
                    style: GoogleFonts.notoSans(
                      fontSize: 16,
                      fontWeight: FontWeight.w800,
                      color: AppColors.govNavyMedium,
                      letterSpacing: -0.3,
                    ),
                  ),
                ],
              ),
            ],
          ),

          // Right: Nav Menu
          if (!isMobile)
            Row(
              children: [
                _navButton(0, 'Home', Icons.home),
                _navButton(1, 'Text Scam Scanner', Icons.center_focus_strong),
                _navButton(2, 'Voice Spoof Scanner', Icons.mic),
                _navButton(3, 'Cyber Shield Bot', Icons.smart_toy),
              ],
            ),
        ],
      ),
    );
  }

  Widget _navButton(int index, String label, IconData icon) {
    final isSelected = selectedIndex == index;
    return Padding(
      padding: const EdgeInsets.only(left: 8),
      child: TextButton.icon(
        onPressed: () => onTabSelected(index),
        icon: Icon(
          icon,
          size: 18,
          color: isSelected ? AppColors.primaryBlue : AppColors.textMuted,
        ),
        label: Text(
          label,
          style: GoogleFonts.notoSans(
            fontSize: 13,
            fontWeight: isSelected ? FontWeight.bold : FontWeight.w600,
            color: isSelected ? AppColors.primaryBlue : AppColors.textDark,
          ),
        ),
        style: TextButton.styleFrom(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
          backgroundColor: isSelected ? AppColors.primaryBlue.withOpacity(0.08) : Colors.transparent,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
    );
  }
}
