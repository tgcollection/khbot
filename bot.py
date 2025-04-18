from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

BOT_TOKEN = '7945088452:AAFQr_MlSonhEIeBQ6SJbd5Ob9JdiO7H_YU'

# Dictionary to store last welcome message ID per chat
last_welcome_message = {}

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.chat_member.chat.id

    # Delete previous welcome message if exists
    if chat_id in last_welcome_message:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_welcome_message[chat_id])
        except Exception as e:
            print(f"Failed to delete message: {e}")

    for member in update.chat_member.new_chat_members:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ JOIN PREMIUM", url="https://t.me/koleksiheboh")],
            [InlineKeyboardButton("📢 INFO ADMIN", url="https://anggur88aura.pro/")]
        ])

        welcome_text = (
            f"👋 Selamat datang, {member.full_name}!\n\n"
            "SELAMAT BERGABUNG DI GRUP KOLEKSI HEBOH!\n"
            "Untuk kalian yang ingin join premium langsung KLIK LINK DIBAWAH!\n"
            "Admin asli hanya yang tertera di grup saja!\n\n"
            "⚠️ *Note:* Jika ada yang transaksi di luar admin grup, hal tersebut diluar tanggung jawab kami!"
        )

        sent_message = await context.bot.send_message(
            chat_id=chat_id,
            text=welcome_text,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

        # Store message ID for future deletion
        last_welcome_message[chat_id] = sent_message.message_id

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    print("Bot is running...")
    app.run_polling()
