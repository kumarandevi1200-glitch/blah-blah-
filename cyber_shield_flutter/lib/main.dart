import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'constants/app_colors.dart';
import 'views/home_view.dart';

void main() {
  runApp(const CyberShieldPortalApp());
}

class CyberShieldPortalApp extends StatelessWidget {
  const CyberShieldPortalApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'National Cyber Crime Reporting Portal',
      theme: ThemeData(
        scaffoldBackgroundColor: AppColors.backgroundLight,
        primaryColor: AppColors.primaryBlue,
        textTheme: GoogleFonts.notoSansTextTheme(),
        useMaterial3: true,
      ),
      home: const HomeView(),
    );
  }
}
