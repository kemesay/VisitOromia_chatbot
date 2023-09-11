############################################################################################
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import requests
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, Updater
import types
import time
import asyncio

# Constants
RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'
TOKEN = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'

# Start Command Handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_user.id, photo=open("visit_oromia.jpg", "rb"),
                           caption="A land of Diverse Beauty, Oromia!")
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
    app.run_polling(poll_interval=2)
    # Updater.idle()


