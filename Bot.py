import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ⚠️ እዚህ ጋ ከ @BotFather ያገኘኸውን አዲሱን ቶከን ብቻ በነጠላ ሰረዞቹ (' ') መሃል ተካው!
BOT_TOKEN = '8705349467:AAEcCFlo8UQjnzhYDSwl7jKFyIUbPoZKA08'
bot = telebot.TeleBot(BOT_TOKEN)

players_db = {}

def generate_bingo_card():
    """Generates a standard 5x5 Bingo matrix."""
    ranges = [
        (1, 15),   # B
        (16, 30),  # I
        (31, 45),  # N
        (46, 60),  # G
        (61, 75)   # O
    ]
    card = []
    for r in ranges:
        col = random.sample(range(r[0], r[1] + 1), 5)
        card.append(col)
    
    # Transpose matrix to standard 5x5 layout
    card = list(map(list, zip(*card)))
    card[2][2] = "FREE"  # Center square is FREE
    return card

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    if chat_id not in players_db:
        players_db[chat_id] = {
            "balance": 5,
            "cards": []
        }
    
    markup = InlineKeyboardMarkup()
    # የቢንጎ መጫወቻ ዌብ አፕ ሊንክዎ
    markup.add(InlineKeyboardButton("🎮 በዌብ መተግበሪያ ይጫወቱ (Play)", web_app=telebot.types.WebAppInfo(url="https://melkshmk.github.io/telegram-bingo/")))
    
    welcome_text = (
        "👋 እንኳን ወደ MK መጻሕፍትና ቢንጎ ቦት በደህና መጡ!\n\n"
        f"💰 የጅማሮ ስጦታዎ፦ {players_db[chat_id]['balance']} ብር በካርድዎ ላይ ተጨምሯል።\n\n"
        "ጨዋታውን ለመጀመር ከታች ያለውን ቁልፍ ይጫኑ!"
    )
    bot.send_message(chat_id, welcome_text, reply_markup=markup)

if __name__ == '__main__':
    print("ቦቱ በተሳካ ሁኔታ ስራ ጀምሯል...")
    bot.infinity_polling()
