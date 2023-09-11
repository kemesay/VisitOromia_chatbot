# import logging
# import requests
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# # Your Telegram bot's API token
# TOKEN = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'

# # Rasa API endpoint
# RASA_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Update with your Rasa server's URL

# # Initialize the Telegram Bot
# updater = Updater(token=TOKEN, use_context=True)
# dispatcher = updater.dispatcher

# # Enable logging (optional)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# # Language options
# languages = {
#     "en": "English",
#     "am": "Amharic",
#     "es": "Spanish"
# }
# # Language codes for translation
# language_codes = {
#     "en": "en",
#     "am": "am",
#     "es": "es"
# }
# # Start command handler
# def start(update: Update, context: CallbackContext):
#     user_id = update.message.chat_id
#     keyboard = [
#         [InlineKeyboardButton(languages[lang], callback_data=lang) for lang in languages.keys()]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text("Please select a language:", reply_markup=reply_markup)

# # Callback function for language selection
# def language_selection(update: Update, context: CallbackContext):
#     query = update.callback_query
#     user_id = query.message.chat_id
#     data = query.data
#     context.user_data["target_language"] = data
#     query.edit_message_text(f"Language set to {languages[data]}")

# # Handler for user messages
# def handle_message(update: Update, context: CallbackContext):
#     user_id = update.message.chat_id
#     message = update.message.text
#     target_language = context.user_data.get("target_language", "en")  # Default to English

#     # Detect the language of the user's message
#     detected_language = detect_language(message)

#     # Translate the user message to the selected target language
#     translated_message = translate_message(message, detected_language, target_language)

#     # Send the user message, detected language, and translated message
#     bot.send_message(user_id, f"User Message: {message}")
#     bot.send_message(user_id, f"Detected Language: {detected_language}")
#     bot.send_message(user_id, f"Translated Message: {translated_message}")

# # Detect the language of a message using langdetect
# def detect_language(text):
#     from langdetect import detect
#     detected_language = detect(text)
#     return detected_language

# # Translate a message to the target language using googletrans
# def translate_message(text, source_language, target_language):
#     from googletrans import Translator
#     translator = Translator()
#     translation = translator.translate(text, src=language_codes[source_language], dest=language_codes[target_language])
#     return translation.text
# # Add conversation handlers
# def main():
    
#         dispatcher.add_handler(CommandHandler('start', start))
#         dispatcher.add_handler(CallbackQueryHandler(language_selection))
#         dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
#         # Start the bot
#         updater.start_polling()
#         updater.idle()
# if __name__ == "__main__":
#     main()
    
    
    
    
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# Your Telegram bot's API token
TOKEN = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'

# Rasa API endpoint
RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'  # Update with your Rasa server's URL

# Initialize the Telegram Bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Enable logging (optional)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Language options
languages = {
    "en": "English",
    "am": "Amharic",
    "es": "Spanish"
}

# Language codes for translation
language_codes = {
    "en": "en",
    "am": "am",
    "es": "es"
}

# Start command handler
def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    keyboard = [
        [InlineKeyboardButton(languages[lang], callback_data=lang) for lang in languages.keys()]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please select a language:", reply_markup=reply_markup)

# Callback function for language selection
def language_selection(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.message.chat_id
    data = query.data
    context.user_data["target_language"] = data
    query.edit_message_text(f"Language set to {languages[data]}")

# Handler for user messages
def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    message = update.message.text
    target_language = context.user_data.get("target_language", "en")  # Default to English

    # Make a request to the RASA API
    response = get_rasa_response(message)

    # Translate and send the RASA response
    translated_response = translate_message(response, 'en', target_language)
    context.bot.send_message(user_id, f"RASA Response: {translated_response}")

# Function to get RASA response
def get_rasa_response(message):
    payload = {
        'sender': 'user',
        'message': message,
    }
    response = requests.post(RASA_API_ENDPOINT, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to get a response from RASA."

# Detect the language of a message using langdetect
def detect_language(text):
    from langdetect import detect
    detected_language = detect(text)
    return detected_language

# Translate a message to the target language using googletrans
def translate_message(text, source_language, target_language, max_retries=3):
    from googletrans import Translator
    translator = Translator()
    
    for _ in range(max_retries):
        try:
            translation = translator.translate(text, src=language_codes[source_language], dest=language_codes[target_language])
            
            if translation and translation.text:
                return translation.text
            else:
                print("Empty translation received. Retrying...")
                continue
        except Exception as e:
            print(f"Translation error: {str(e)}")
            continue
            
    return "Translation failed after multiple attempts"


def main():
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(language_selection))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
