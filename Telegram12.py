import telegram
from telegram.ext import Updater, MessageHandler, Filters
import requests

# Replace "YOUR_TELEGRAM_BOT_TOKEN" with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = "6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA"
RASA_API_ENDPOINT = "http://localhost:8443/webhooks/telegram/webhook"

def forward_to_rasa(update, context):
    message = update.message.text
    chat_id = update.message.chat_id

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "sender": str(chat_id),
        "message": message,
    }

    response = requests.post(RASA_API_ENDPOINT, json=payload, headers=headers)
    rasa_response = response.json()[0]['message']['text']

    update.message.reply_text(rasa_response)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_rasa))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
