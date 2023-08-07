from typing import Final

# # pip install python-telegram-bot
from telegram import update
import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackQueryHandle


# # Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m michu a bot and give information on michu. What\'s up?')

RASA_API_ENDPOINT = 'http://52.212.99.214:8443/webhooks/rest/webhook'
TOKEN='6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text
    username = update.message.from_user.username
    payload = {
        'sender': message_type,
        'message': text
    }
   
    print (f'{username}:his text=>"{text}"')
    r = requests.post(RASA_API_ENDPOINT, json=payload)

    # Get the response from the Rasa server
    response = r.json() #[0]['text']
    text = response[0]['text']
    buttons = response[0].get('buttons', [])

    # Create a list of InlineKeyboardButton objects from the button options
    keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

    # Create an InlineKeyboardMarkup object with the button options
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text,reply_markup=reply_markup)

async def handle_button_click(update, context):
    query = update.callback_query
    payload = query.data

    # Create a payload to send to the Rasa server with the button payload as user input
    payload = {
        'sender': query.message.chat_id,
        'message': payload
    }

    # Send a POST request to the Rasa API endpoint with the payload
    r = requests.post(RASA_API_ENDPOINT, json=payload)

    # Get the response from the Rasa server
    response = r.json()

    # Extract the text from the response
    text = response[0]['text']
     # Extract the buttons from the response (if available)
    buttons = response[0].get('buttons', [])

    # Create a list of InlineKeyboardButton objects from the button options
    keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

    # Create an InlineKeyboardMarkup object with the button options
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Edit the original message with the updated response from Rasa, including the buttons
    await query.edit_message_text(text, reply_markup=reply_markup)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a Rasa chatbot!")

if __name__=="__main__":
    # updater = Updater(token='6320973861:AAEO_7-FdnSnKKur2OWWX4BvVJV6-dBJzE0', use_context=True)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button_click))
    # Log all errors
    # app.add_error_handler(error)
    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
    # dispatcher = updater.dispatcher

     