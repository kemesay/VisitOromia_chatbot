from typing import Final

# # pip install python-telegram-bot
from telegram import Update
import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackQueryHandler

# print('Starting up bot...')

# RASA_API_ENDPOINT = 'http://63.34.199.220:4020/webhooks/rest/webhook'

# TOKEN: Final ='5543393201:AAHr4nv_cVAZ0UV8ek56v_MZ78TueCxEoQg'  #'5861865205:AAFuE2Ik6XWWLkir39KRw-9fXMciqYL89FQ'
# BOT_USERNAME: Final = '@your_bot_user'


# # RASA_API_ENDPOINT = 'http://<EC2-instance-IP>:5005/webhooks/rest/webhook'

# def handle_message(update, context):
#     # Get the user's message from the update object
#     user_message = update.message.text

#     # Create a payload to send to the Rasa server
#     payload = {
#         'sender': update.message.chat_id,
#         'message': user_message
#     }

#     # Send a POST request to the Rasa API endpoint with the payload
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json()[0]['text']

#     # Send the response back to the user via Telegram
#     context.bot.send_message(chat_id=update.effective_chat.id, text=response)


# # Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m michu a bot and give information on michu. What\'s up?')

# # Lets us use the /help command
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Try typing your question comman questioning way and I will do my best to respond!')

# # Lets us use the /custom command
# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('This is a custom command, you can ask info about michu you want here.')


# def handle_response(text: str) -> str:
#     # Create your own response logic
#     print('This is text',text)
#     processed: str = text.lower()
#     print(processed,'This is procced')

#     if 'hello' in processed:
#         return 'Hey there!'

#     if 'how are you' in processed:
#         return 'I\'m good!'

#     if 'i love python' in processed:
#         return 'Remember to subscribe!'

#     return 'I don\'t understand'

RASA_API_ENDPOINT = 'http://52.212.99.214:8443/webhooks/rest/webhook'
TOKEN='6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text
    username = update.message.from_user.username
    # user=update.message.from_user
    #printn("this is user detail", user)
    payload = {
        'sender': message_type,
        'message': text
    }
    # Print a log for debugging
    #print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
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

    # Send the response back to the user via Telegram, including the buttons
   # context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)
#     # React to group messages only if users mention the bot directly
#     if message_type == 'group':
#         # Replace with your bot username
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             return  # We don't want the bot respond if it's not mentioned in the group
#     else:
#         response: str = handle_response(text)

#     # Reply normal if the message is in private
#     print('Bot:', response)
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

# # Log errors
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')


# # Run the program
# if __name__ == '__main__':
#     app = Application.builder().token(TOKEN).build()

#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     # Messages
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Log all errors
#     app.add_error_handler(error)

#     print('Polling...')
#     # Run the bot
#     app.run_polling(poll_interval=5)


# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#import telegram
#from telegram.ext import Updater, CommandHandler, MessageHandler, filters


# def handle_message(update, context):
#     # Get the user's message from the update object

#     user_message = update.message.text

#     # Create a payload to send to the Rasa server
#     payload = {
#         'sender': update.message.chat_id,
#         'message': user_message
#     }

#     # Send a POST request to the Rasa API endpoint with the payload
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json()[0]['text']

#     # Send the response back to the user via Telegram
#     context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a Rasa chatbot!")

# def handle_message(update, context):
#     # Send the user's message to the Rasa server and get the response
#     ...

#     # Send the response back to the user via Telegram
#     context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__=="__main__":
    # updater = Updater(token='6320973861:AAEO_7-FdnSnKKur2OWWX4BvVJV6-dBJzE0', use_context=True)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    # app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button_click))
    # Log all errors
    # app.add_error_handler(error)
    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)
    # dispatcher = updater.dispatcher

     # Log all errors
#     app.add_error_handler(error)

#     print('Polling...')
#     # Run the bot
#     app.run_polling(poll_interval=5)

    # start_handler = CommandHandler('start', start)
    # message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

    # dispatcher.add_handler(start_handler)
    # dispatcher.add_handler(message_handler)

    # updater.start_polling()
    # updater.idle()

# if __name__== "__main__":
#     main()






