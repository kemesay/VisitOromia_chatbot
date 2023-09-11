import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
from langdetect import detect

# Enable logging for debugging purposes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define states for the conversation
SELECT_LANGUAGE, INPUT_TEXT = range(2)

# Initialize the translator
translator = Translator()

# Dictionary to store user data during the conversation
user_data = {}

# Dictionary to store user states and selected languages
user_states = {}

# Start command to initiate the conversation
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.user_data.clear()
    user_id = user.id

    # Check if the user has previously selected a language
    if user_id in user_states:
        language_code = user_states[user_id]
        update.message.reply_html(
            f"Hi {user.mention_html()}!\n\n"
            f"You have selected {language_code.upper()} as your target language."
            "Please enter the text you want to translate or change your language selection:",
            reply_markup=get_language_buttons(),
        )
        return INPUT_TEXT

    update.message.reply_html(
        f"Hi {user.mention_html()}!\n\n"
        "I can translate text into different languages. "
        "Please select a language you want to translate to:",
        reply_markup=get_language_buttons(),
    )

    return SELECT_LANGUAGE

# Define the language buttons
def get_language_buttons():
    keyboard = [
        [InlineKeyboardButton("English 🇺🇸", callback_data="en")],
        [InlineKeyboardButton("Spanish 🇪🇸", callback_data="es")],
        [InlineKeyboardButton("Amharic 🇪🇹", callback_data="am")],
        [InlineKeyboardButton("Arabic AR", callback_data="ar")],

    ]
    return InlineKeyboardMarkup(keyboard)

# Callback function when a language is selected
def select_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    language_code = query.data
    user_id = update.effective_user.id

    # Store the selected language in the user_states dictionary
    user_states[user_id] = language_code

    query.edit_message_text(f"You selected {language_code.upper()}. Now, please enter the text you want to translate:")

    return INPUT_TEXT

# Translate the text
def translate_text(update: Update, context: CallbackContext):
    user = update.effective_user
    text = update.message.text
    user_id = user.id
    language_code = user_states.get(user_id, 'en')  # Default to English

    try:
        # Detect the source language
        source_language = detect(text)
        
        # Translate the text to the selected language
        translation = translator.translate(text, src=source_language, dest=language_code)
        
        update.message.reply_text(translation.text)
    except Exception as e:
        update.message.reply_text("An error occurred during translation.")

    return INPUT_TEXT

# Main function to run the bot
def main():
    # Initialize the Telegram Bot with your API token
    updater = Updater(token="6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI", use_context=True)
    dp = updater.dispatcher
    # Define the conversation handler
    dp.add_handler(ConversationHandler( entry_points=[CommandHandler("start", start)],
        states={ SELECT_LANGUAGE: [CallbackQueryHandler(select_language)],
            INPUT_TEXT: [MessageHandler(Filters.text & ~Filters.command, translate_text)],
        },
        fallbacks=[],
        per_user=True,
    ))
    # Start the bot
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
