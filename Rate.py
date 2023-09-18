# import telegram
# from telegram import ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
# import requests
# import json

# # Define states for the conversation
# RATE_COLLECTING = 1

# # Define keyboard options
# rate_keyboard = [['1', '2', '3', '4', '5']]

# # Helper function to send a rate to the API
# def send_rate_to_api(rate, user_id):
#     api_url = 'http://localhost:9000/api/rate/push'
#     data = {
#         'rate': rate,
#         'userId': user_id
#     }
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(api_url, data=json.dumps(data), headers=headers)
#     if response.status_code == 200:
#         return True
#     return False

# # Start command handler
# def start(update, context):
#     user_id = update.effective_user.id
#     update.message.reply_text("Welcome to the Rate Collector Bot! Please rate something:", reply_markup=ReplyKeyboardMarkup(rate_keyboard, one_time_keyboard=True))
#     return RATE_COLLECTING

# # Rate collecting handler
# def collect_rate(update, context):
#     user_id = update.effective_user.id
#     rate = update.message.text
#     if rate.isdigit() and 1 <= int(rate) <= 5:
#         if send_rate_to_api(int(rate), user_id):
#             update.message.reply_text(f"Thank you for your rating: {rate}")
#         else:
#             update.message.reply_text("Failed to send your rate. Please try again later.")
#     else:
#         update.message.reply_text("Please select a valid rate from 1 to 5:")
#         return RATE_COLLECTING

# # Conversation handler
# def cancel(update, context):
#     update.message.reply_text("Rate collection canceled.")
#     return RATE_COLLECTING

# def main():
#     # Create a Telegram Bot
#     bot_token = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'
#     updater = Updater(token=bot_token, use_context=True)
#     dispatcher = updater.dispatcher

#     # Create conversation handler
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler('start', start)],
#         states={
#             RATE_COLLECTING: [MessageHandler(Filters.text, collect_rate)],
#         },
#         fallbacks=[CommandHandler('cancel', cancel)],
#     )

#     dispatcher.add_handler(conv_handler)

#     # Start the bot
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()



###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
import telegram
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
import requests
import json

# Define states for the conversation

# Define keyboard options
rate_keyboard  = [[InlineKeyboardButton(text="⭐", callback_data="Thanks!"), 
                                        InlineKeyboardButton(text="⭐⭐", callback_data="Thanks a lot!"), 
                                        InlineKeyboardButton(text="⭐⭐⭐", callback_data="Thank you very much!"),
                                        ],
                                        
                                       [ InlineKeyboardButton(text="⭐⭐⭐⭐", callback_data="Thank you so much!"),
                                         InlineKeyboardButton(text="⭐⭐⭐⭐⭐", callback_data="Thank you from the bottom of my heart!"),
                                         ]
                                        ]
def send_rate_to_api(rate, userId, username):
    api_url = 'http://localhost:9000/api/rate/push'
    data = {
        'rate': rate,
        'userId': userId,
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

rate = " "
def calculate_rate(update, context):
    query = update.callback_query
    payload = query.data
    # rate = update.message.text

    if payload in list_button_click:
        query.answer()
        if payload=="Thank you from the bottom of my heart!":
            rate="5"
        elif payload=="Thank you so much!":
           rate="4"
        elif payload=="Thank you very much!":
           rate="3"
        elif payload=="Thank a lot!":
           rate="2"
        elif payload=="Thanks!":
           rate="1"
    return rate

def collect_rate(update, context):
    query = update.callback_query
    payload = query.data
    userId = update.effective_user.id
    username = update.effective_user.username
    rate = calculate_rate(update, context)
    if send_rate_to_api(rate, userId, username):
        query.edit_message_text(payload)
    else:
        update.message.reply_text("Failed to send your rate. Please try again later.")

def cancel(update, context):
    update.message.reply_text("Rate collection canceled.")

def main():
    # Create a Telegram Bot
    bot_token = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Create conversation handler
   

    dispatcher.add_handler(CommandHandler('start', start))
    # Start the bot
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CallbackQueryHandler(collect_rate))
    print("poilling!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
