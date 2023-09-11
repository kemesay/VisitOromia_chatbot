import telegram
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
import requests
import json

# Define states for the conversation
RATE_COLLECTING = 1

# Define keyboard options
rate_keyboard  = [[InlineKeyboardButton(text="⭐", callback_data="Thanks!"), 
                                        InlineKeyboardButton(text="⭐⭐", callback_data="Thanks a lot!"), 
                                        InlineKeyboardButton(text="⭐⭐⭐", callback_data="Thank you very much!"),
                                        ],
                                        
                                       [ InlineKeyboardButton(text="⭐⭐⭐⭐", callback_data="Thank you so much!"),
                                         InlineKeyboardButton(text="⭐⭐⭐⭐⭐", callback_data="Thank you from the bottom of my heart!"),
                                         ]
                                        ]

# Helper function to send a rate to the API
def send_rate_to_api(rate, user_id, username):
    api_url = 'http://localhost:9000/api/rate/push'
    data = {
        'rate': rate,
        'userId': user_id,
        'username': username
           }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return True
    return False

# Start command handler
def start(update, context):
    user_id = update.effective_user.id
    update.message.reply_text("Welcome to the Rate Collector Bot! Please rate something:", reply_markup=InlineKeyboardMarkup(rate_keyboard, one_time_keyboard=True))
    # return RATE_COLLECTING

# Rate collecting handler
list_button_click = ["Thanks!", "Thanks a lot!", "Thank you very much!", "Thank you so much!", "Thank you from the bottom of my heart!"]

def collect_rate(update, context, query):
    query = update.callback_query
    payload = query.data
    
    user_id = update.effective_user.id
    username = update.effective_user.username
    rate = update.message.text

    rate = " "
    if payload in list_button_click:
        query.answer()
        if payload=="Thank you from the bottom of my heart!":
            rate="⭐⭐⭐⭐⭐"
        elif payload=="Thank you so much!":
           rate="⭐⭐⭐⭐"
        elif payload=="Thank you very much!":
           rate="⭐⭐⭐"
        elif payload=="Thank  a lot!":
           rate="⭐⭐"
        elif payload=="Thanks!":
           rate="⭐"
    #     valuess=(user_id, userName, values)
    #     dataser="insert into feedback(useId,userName,rating) values(%s,%s,%s)"
    #     mycursor.execute(dataser,values)
    #     mydb.commit()
        if send_rate_to_api(rate, user_id, username):
         query.edit_message_text(payload)
        else:
            update.message.reply_text("Failed to send your rate. Please try again later.")
    else:
        update.message.reply_text("Please select a valid rate from 1 to 5:")
        # return RATE_COLLECTING

# Conversation handler
def cancel(update, context):
    update.message.reply_text("Rate collection canceled.")
    # return RATE_COLLECTING

def main():
    # Create a Telegram Bot
    bot_token = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Create conversation handler
   

    dispatcher.add_handler(CommandHandler('start', start))
    # Start the bot
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CallbackQueryHandler(Filters.text, collect_rate))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
