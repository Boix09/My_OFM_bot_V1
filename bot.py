# My_OFM_bot - V1 (minimal Telegram bot)
# Synchronous, beginner-friendly using python-telegram-bot v13.x
# IMPORTANT: Put your token in config.py before running.
import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Basic logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Load token from config.py (should define API_TOKEN variable)
try:
    from config import API_TOKEN  # create config.py and add your token there
except Exception as e:
    raise SystemExit("Please create config.py with API_TOKEN = 'your_token_here'") from e

# Handlers
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Créer un modèle", callback_data='create_model'), InlineKeyboardButton("Mon modèle", callback_data='my_model')],
        [InlineKeyboardButton("Faceswap vidéo", callback_data='faceswap'), InlineKeyboardButton("Aide", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Bienvenue sur <b>My_OFM_bot</b> 🤖\nChoisissez une option ci-dessous :", reply_markup=reply_markup, parse_mode='HTML')

def help_cmd(update: Update, context: CallbackContext):
    help_text = (
        "My_OFM_bot V1 - commandes disponibles:\n"
        "/start - afficher le menu principal\n"
        "/help - afficher cette aide\n\n"
        "V1 est un MVP : les options 'Créer un modèle', 'Mon modèle' et 'Faceswap' sont pour l'instant des placeholders."
    )
    update.message.reply_text(help_text)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data
    if data == 'create_model':
        query.edit_message_text("Créer mon modèle 🚧\nFonctionnalité en développement. Bientôt tu pourras nommer et définir ton modèle virtuel.")
    elif data == 'my_model':
        query.edit_message_text("Mon modèle 👩‍💻\nAucun modèle enregistré pour le moment. Utilise 'Créer un modèle' dès qu'elle sera disponible.")
    elif data == 'faceswap':
        query.edit_message_text("Faceswap vidéo 🎭\nCette fonctionnalité arrivera dans une prochaine version (V4).")
    elif data == 'help':
        query.edit_message_text("Aide 📘\nUtilise /help pour voir les commandes. Pour l'instant V1 est un squelette prêt pour évoluer.")

def error_handler(update: object, context: CallbackContext):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_error_handler(error_handler)

    # Start the Bot
    print("Starting My_OFM_bot V1...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
