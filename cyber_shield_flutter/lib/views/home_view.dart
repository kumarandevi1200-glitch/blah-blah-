import 'package:flutter/material.dart';
import '../widgets/top_gov_bar.dart';
import '../widgets/portal_header.dart';
import '../widgets/hero_banner.dart';
import '../widgets/action_cards.dart';
import 'text_scanner_view.dart';
import 'speech_scanner_view.dart';
import 'bot_chat_view.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  int _currentTab = 0;

  void _onTabSelected(int index) {
    setState(() {
      _currentTab = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          // Top Government Bar
          const TopGovBar(),
          
          // Portal Header Navigation
          PortalHeader(
            selectedIndex: _currentTab,
            onTabSelected: _onTabSelected,
          ),

          // View Content Container
          Expanded(
            child: IndexedStack(
              index: _currentTab,
              children: [
                // Tab 0: Main Home Portal
                SingleChildScrollView(
                  child: Column(
                    children: [
                      HeroBanner(
                        onTextScanPressed: () => _onTabSelected(1),
                        onVoiceScanPressed: () => _onTabSelected(2),
                      ),
                      const SizedBox(height: 16),
                      ActionCardsGrid(
                        onTabSelected: _onTabSelected,
                      ),
                      const SizedBox(height: 32),
                    ],
                  ),
                ),

                // Tab 1: Text Scam Scanner
                const TextScannerView(),

                // Tab 2: Speech & Voice Spoof Scanner
                const SpeechScannerView(),

                // Tab 3: Cyber Shield Bot Chat
                const BotChatView(),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
