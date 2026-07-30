import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../constants/app_colors.dart';
import '../services/api_service.dart';

class BotChatView extends StatefulWidget {
  const BotChatView({super.key});

  @override
  State<BotChatView> createState() => _BotChatViewState();
}

class _BotChatViewState extends State<BotChatView> {
  final TextEditingController _inputController = TextEditingController();
  final List<Map<String, String>> _messages = [
    {
      'role': 'assistant',
      'content':
          'Hello! I am **Cyber Shield Bot** (RAG-Powered Security Advisor). Describe a suspicious call, message, or emergency scenario to receive verified security guidance.'
    }
  ];
  bool _isSending = false;

  void _sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    setState(() {
      _messages.add({'role': 'user', 'content': text});
      _isSending = true;
    });

    _inputController.clear();

    final botReply = await ApiService.getBotAdvice(text, _messages);

    setState(() {
      _isSending = false;
      _messages.add({'role': 'assistant', 'content': botReply});
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Quick Action Chips
        Container(
          color: Colors.white,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          child: SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                const Text('🚨 Emergency: ', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                _quickChip('🔑 Shared OTP / PIN'),
                const SizedBox(width: 8),
                _quickChip('🌐 Clicked Fake Link'),
                const SizedBox(width: 8),
                _quickChip('📞 Fake Police Call'),
                const SizedBox(width: 8),
                _quickChip('💸 Money Transferred Scam'),
              ],
            ),
          ),
        ),

        // Chat Messages List
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _messages.length,
            itemBuilder: (context, index) {
              final msg = _messages[index];
              final isUser = msg['role'] == 'user';
              return Align(
                alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
                child: Container(
                  margin: const EdgeInsets.only(bottom: 12),
                  padding: const EdgeInsets.all(16),
                  constraints: const BoxConstraints(maxWidth: 600),
                  decoration: BoxDecoration(
                    color: isUser ? AppColors.primaryBlue : Colors.white,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(color: Colors.black.withOpacity(0.04), blurRadius: 6),
                    ],
                  ),
                  child: Text(
                    msg['content']!,
                    style: GoogleFonts.notoSans(
                      color: isUser ? Colors.white : AppColors.textDark,
                      fontSize: 14,
                      height: 1.4,
                    ),
                  ),
                ),
              );
            },
          ),
        ),

        // Input Field
        Container(
          padding: const EdgeInsets.all(16),
          color: Colors.white,
          child: Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _inputController,
                  decoration: InputDecoration(
                    hintText: 'Describe suspicious incident or ask security advice...',
                    fillColor: AppColors.backgroundLight,
                    filled: true,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(24),
                      borderSide: BorderSide.none,
                    ),
                    contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                  ),
                  onSubmitted: _sendMessage,
                ),
              ),
              const SizedBox(width: 12),
              CircleAvatar(
                backgroundColor: AppColors.primaryBlue,
                radius: 24,
                child: _isSending
                    ? const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2),
                      )
                    : IconButton(
                        icon: const Icon(Icons.send, color: Colors.white, size: 20),
                        onPressed: () => _sendMessage(_inputController.text),
                      ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _quickChip(String label) {
    return ActionChip(
      label: Text(label, style: GoogleFonts.notoSans(fontSize: 12, fontWeight: FontWeight.w600)),
      backgroundColor: AppColors.primaryBlue.withOpacity(0.08),
      side: const BorderSide(color: AppColors.primaryBlue),
      onPressed: () => _sendMessage(label),
    );
  }
}
