# bot.py — My_OFM_bot V1 (compatible python-telegram-bot v22+)
import logging
import sys
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Charge ton token depuis config.py (crée config.py avec API_TOKEN = '...').
try:
    from config import API_TOKEN
except Exception:
    sys.exit("⚠️ Erreur: crée config.py et définis API_TOKEN = 'ton_token_ici'")

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Handlers (async pour PTB v20+)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Créer un modèle", callback_data="create_model"),
         InlineKeyboardButton("Mon modèle", callback_data="my_model")],
        [InlineKeyboardButton("Faceswap vidéo", callback_data="faceswap"),
         InlineKeyboardButton("Aide", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            "Bienvenue sur <b>My_OFM_bot</b> 🤖\nChoisissez une option ci-dessous :",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Bienvenue sur My_OFM_bot — menu ci-dessous.",
                                       reply_markup=reply_markup)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "My_OFM_bot V1 — commandes :\n"
        "/start - menu principal\n"
        "/help - voir cette aide\n\n"
        "Note: V1 est un MVP — les options 'Créer un modèle', 'Mon modèle' et 'Faceswap' sont des placeholders."
    )
    await update.message.reply_text(help_text)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data or ""
    if data == "create_model":
        await query.edit_message_text(
            "Créer mon modèle 🚧\nFonctionnalité en développement. Bientôt tu pourras nommer et définir ton modèle virtuel."
        )
    elif data == "my_model":
        await query.edit_message_text(
            "Mon modèle 👩‍💻\nAucun modèle enregistré pour le moment. Utilise 'Créer un modèle' quand disponible."
        )
    elif data == "faceswap":
        await query.edit_message_text(
            "Faceswap vidéo 🎭\nCette fonctionnalité arrivera dans une prochaine version (V4)."
        )
    elif data == "help":
        await query.edit_message_text(
            "Aide 📘\nUtilise /help pour voir les commandes. V1 est un squelette prêt pour évoluer."
        )
    else:
        await query.edit_message_text("Commande inconnue.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling an update:", exc_info=context.error)

def main():
    app = Application.builder().token(API_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    # CallbackQuery (inline buttons)
    app.add_handler(CallbackQueryHandler(button_handler))
    # error handler
    app.add_error_handler(error_handler)

    print("▶️ Démarrage My_OFM_bot V1 (PTB v22+) — running...")
    app.run_polling()

if __name__ == "__main__":
    main()

