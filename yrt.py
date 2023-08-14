# from typing import Final

# # # pip install python-telegram-bot
# from telegram import Update
# import requests
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackQueryHandle


# # # Lets us use the /start command
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello there! I\'m michu a bot and give information on michu. What\'s up?')
    
# RASA_API_ENDPOINT = 'http://52.212.99.214:8443/webhooks/rest/webhook'
# TOKEN='6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Get basic info of the incoming message
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
#     username = update.message.from_user.username
#     payload = {
#         'sender': message_type,
#         'message': text
#     }
   
#     print (f'{username}:his text=>"{text}"')
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json() #[0]['text']
#     text = response[0]['text']
#     buttons = response[0].get('buttons', [])

#     # Create a list of InlineKeyboardButton objects from the button options
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

#     # Create an InlineKeyboardMarkup object with the button options
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(text,reply_markup=reply_markup)

# async def handle_button_click(update, context):
#     query = update.callback_query
#     payload = query.data

#     # Create a payload to send to the Rasa server with the button payload as user input
#     payload = {
#         'sender': query.message.chat_id,
#         'message': payload
#     }

#     # Send a POST request to the Rasa API endpoint with the payload
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json()

#     # Extract the text from the response
#     text = response[0]['text']
#      # Extract the buttons from the response (if available)
#     buttons = response[0].get('buttons', [])

#     # Create a list of InlineKeyboardButton objects from the button options
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

#     # Create an InlineKeyboardMarkup object with the button options
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Edit the original message with the updated response from Rasa, including the buttons
#     await query.edit_message_text(text, reply_markup=reply_markup)


# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a Rasa chatbot!")

# if __name__=="__main__":
#     # updater = Updater(token='6320973861:AAEO_7-FdnSnKKur2OWWX4BvVJV6-dBJzE0', use_context=True)
#     app = Application.builder().token(TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     app.add_handler(CallbackQueryHandler(handle_button_click))
#     # Log all errors
#     # app.add_error_handler(error)
#     print('Polling...')
#     # Run the bot
#     app.run_polling(poll_interval=5)
#     # dispatcher = updater.dispatcher




# from typing import Final

# # # pip install python-telegram-bot
# from telegram import Update
# import requests
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackQueryHandle


# # # Lets us use the /start command
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello there! I\'m michu a bot and give information on michu. What\'s up?')
    
# RASA_API_ENDPOINT = 'http://52.212.99.214:8443/webhooks/rest/webhook'
# TOKEN='6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Get basic info of the incoming message
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
#     username = update.message.from_user.username
#     payload = {
#         'sender': message_type,
#         'message': text
#     }
   
#     print (f'{username}:his text=>"{text}"')
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json() #[0]['text']
#     text = response[0]['text']
#     buttons = response[0].get('buttons', [])

#     # Create a list of InlineKeyboardButton objects from the button options
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

#     # Create an InlineKeyboardMarkup object with the button options
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(text,reply_markup=reply_markup)

# async def handle_button_click(update, context):
#     query = update.callback_query
#     payload = query.data

#     # Create a payload to send to the Rasa server with the button payload as user input
#     payload = {
#         'sender': query.message.chat_id,
#         'message': payload
#     }

#     # Send a POST request to the Rasa API endpoint with the payload
#     r = requests.post(RASA_API_ENDPOINT, json=payload)

#     # Get the response from the Rasa server
#     response = r.json()

#     # Extract the text from the response
#     text = response[0]['text']
#      # Extract the buttons from the response (if available)
#     buttons = response[0].get('buttons', [])

#     # Create a list of InlineKeyboardButton objects from the button options
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

#     # Create an InlineKeyboardMarkup object with the button options
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Edit the original message with the updated response from Rasa, including the buttons
#     await query.edit_message_text(text, reply_markup=reply_markup)


# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a Rasa chatbot!")

# if __name__=="__main__":
#     # updater = Updater(token='6320973861:AAEO_7-FdnSnKKur2OWWX4BvVJV6-dBJzE0', use_context=True)
#     app = Application.builder().token(TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     app.add_handler(CallbackQueryHandler(handle_button_click))
#     # Log all errors
#     # app.add_error_handler(error)
#     print('Polling...')
#     # Run the bot
#     app.run_polling(poll_interval=5)
#     # dispatcher = updater.dispatcher

############################################################################################
############################################################################################
# from typing import Final
# from telegram import Update
# import requests
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackQueryHandler

# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello there! I\'m michu  bot and give information on michu. What\'s up?')

# # RASA_API_ENDPOINT =' https://aec5-197-156-76-21.ngrok.io/webhooks/rest/webhook'
# RASA_API_ENDPOINT ='http://localhost:5005/webhooks/rest/webhook'
# # RASA_API_ENDPOINT='http://52.212.99.214:8443/webhooks/rest/webhook'
# TOKEN='6309201413:AAEeTRtD1YsF_wDlPhQtdQVZjqTqVv4KOPA'
# # ACTION_ENDPOINT='http://52.212.99.214:5055/webhook'
# # ACTION_ENDPOINT='http://localhost:5055/webhook'




# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Get basic info of the incoming message
#     message_type: str = update.message.chat.type
#     text: str = update.message.text
#     video: str = update.message.video
#     image: str = update.message.photo
#     # username = update.message.from_user.username

#     payload = {
#         'sender': message_type,
#         'message': image
#     }
#     # Print a log for debugging
#     # print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
#     # print (f'{username}:his text=>"{text}"')
#     r = requests.post(RASA_API_ENDPOINT, json=payload)
#     # r1 = requests.post(ACTION_ENDPOINT, json=payload)
#     # Get the response from the Rasa server
#     response = r.json() #[0]['text']
#     print("this is video response", response)
#     # for i in range(len(response)):
#     # text = response[0]['text'] 
#     # video = response[0]['video']
#     # image = response[0]['image'] 
#     buttons = response[0].get('buttons', [])
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in buttons]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     [await update.message.reply_photo(response[i]['image'],reply_markup=reply_markup) for i in range(len(response))]
    
# async def handle_button_click(update, context):
#     query = update.callback_query
#     payload = query.data
#     payload = {
#         'sender': query.message.chat_id,
#         'message': payload
#     }
#     # Send a POST request to the Rasa API endpoint with the payload
#     r = requests.post(RASA_API_ENDPOINT, json=payload)
#     # Get the response from the Rasa server
#     response = r.json()
#     print("from buttons", response)
#     image = response[0]['image']
    
#     buttons = response[0].get('buttons', [])

#     # Create a list of InlineKeyboardButton objects from the button options
#     keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload'])] for button in buttons]

#     reply_markup = InlineKeyboardMarkup(keyboard)
#     # Edit the original message with the updated response from Rasa, including the buttons
#     await query.edit_message_text(image, reply_markup=reply_markup)
    
# if __name__=="__main__":
#     app = Application.builder().token(TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))
#     app.add_handler(CallbackQueryHandler(handle_button_click))
#     print('Polling...')
#     app.run_polling(poll_interval=2)

############################################################################################
############################################################################################
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, Updater
import types
import time
import asyncio

# Constants
RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'
TOKEN = '5464711872:AAGnZmwHMz24UAE3i8Z5Rtz4kxvVAMnekr8'

# Start Command Handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_user.id, photo=open("visit_oromia.jpg", "rb"),
                           caption="A land of Diverse Beauty!")
    await context.bot.send_message(chat_id=update.effective_user.id,
                             text=f"Hello Mr/mrs. {update.effective_user.first_name} WelCome to Visit Oromia!")
    # await update.message.reply_text("Hello there! I'm Bale Red-Fox Bot and give information on Visit Oromia. What's up?")
    message_type = update.message.chat.type
    text = update.message.text
    payload = {
        'sender': message_type,
        'message': text 
    }
    
    response = requests.post(RASA_API_ENDPOINT, json=payload).json()
    
    keyboard_buttons = []
    text_responses = []
    
    
    for entry in response:
        text = entry.get('text', '')
        buttons = entry.get('buttons', [])
        
        # Group the buttons into pairs of two buttons per line
        button_pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        
        # Create the keyboard markup with pairs of buttons
        keyboard = [
            [InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in button_pair]
            for button_pair in button_pairs
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send the message with buttons at the top
        await update.message.reply_text(text, reply_markup=reply_markup)

    
    
    

    for entry in response:
        text = entry.get('text', '')
        buttons = entry.get('buttons', [])
            
        text_responses.append(text)
        
        button_titles = [button['title'] for button in buttons]
        # Split button_titles into pairs of buttons
        button_pairs = [button_titles[i:i+2] for i in range(0, len(button_titles), 2)]
        
        if button_pairs:
            # Create a list of lists of KeyboardButton objects for each pair
            pair_keyboard_buttons = [[KeyboardButton(title) for title in pair] for pair in button_pairs]
            keyboard_buttons.extend(pair_keyboard_buttons)

    # Create a ReplyKeyboardMarkup with the keyboard buttons
    reply_markup = ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)

    # Send text responses along with the reply keyboard
    for text_response in text_responses:
        await update.message.reply_text(text_response, reply_markup=reply_markup)

# Message Handling
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    image = update.message.photo[-1].file_id if update.message.photo else None
    attachment = update.message.video.file_id if update.message.video else None

    payload = {
        'sender': message_type,
        'message': text or image or attachment
    }

    response = requests.post(RASA_API_ENDPOINT, json=payload).json()
    # print("this is response", response)
    for entry in response:
        text = entry.get('text', '')
        buttons = entry.get('buttons', [])
        keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in buttons]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if entry.get('image'):
            await update.message.reply_photo(entry['image'], caption=text, reply_markup=reply_markup)
        elif entry.get("attachment"):
            attachment = entry["attachment"]
            if attachment and attachment.get('type') == 'video':
                # print("this is video", attachment)
                payload = attachment.get('payload')
                if payload:
                    # title = payload.get('title', 'Default Title')
                    src = payload.get('src')
                # Send a message with the video link
                    await update.message.reply_text(src, reply_markup=reply_markup)

        else:
            await update.message.reply_text(text, reply_markup=reply_markup)

# Button Click Handling
async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    payload = query.data
    payload = {
        'sender': query.message.chat_id,
        'message': payload
    }
    response = requests.post(RASA_API_ENDPOINT, json=payload).json()
    for entry in response:
        text = entry.get('text', '')
        buttons = entry.get('buttons', [])
        keyboard = [[InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in buttons]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if entry.get('image'):
            # await query.message.edit_media(media=InputMediaPhoto(entry['image']), reply_markup=reply_markup)
            await query.message.reply_photo(photo=entry['image'], caption=text, reply_markup=reply_markup)
            # await query.edit_message_photo(entry['image'], caption=text, reply_markup=reply_markup)
        elif entry.get("attachment"):
            attachment = entry["attachment"]
            if attachment and attachment.get('type') == 'video':
                # print("this is video", attachment)
                payload = attachment.get('payload')
                if payload:
                    title = payload.get('title', 'Default Title')
                    src = payload.get('src')
                # Send a message with the video link
                    await query.edit_message_text(f"Check this video: {title}\n{src}", reply_markup=reply_markup)
                    # await time.sleep(5)
                    await asyncio.sleep(5)  # Add a delay of 5 seconds


        else:
            await query.edit_message_text(text, reply_markup=reply_markup)


if __name__=="__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button_click))
    print('Polling...')
    app.run_polling(poll_interval=10)
    # Updater.idle()


