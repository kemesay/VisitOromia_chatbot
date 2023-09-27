from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Location, ReplyKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Updater, CommandHandler, MessageHandler, \
    Filters, ConversationHandler, CallbackQueryHandler

import asyncio
import logging
import requests
import time
import json
import threading
import requests

# def main_menu_keyboard():
#     main_keyboard = [
#         [KeyboardButton(text="Spinnin Win",  callback_data='m1')],
#         [KeyboardButton(text="Keno", callback_data='h1')],
#         [KeyboardButton(text="Lotter", callback_data='b1')],
#         [KeyboardButton(text="Sport Betting",callback_data='m2')],
#         [KeyboardButton(text="W-Balance", callback_data='m3')]]
#     return ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)


# def main_menu_keyboard():
#     main_keyboard = [
#         [KeyboardButton(text="Spinning Win", callback_data="spinning_win"), 
#          KeyboardButton(text="Keno", callback_data="keno")],
#         [KeyboardButton(text="Lotter", callback_data="lotter"), 
#          KeyboardButton(text="Sport Betting", callback_data="sport_betting")],
#         [KeyboardButton(text="W-Balance", callback_data="w_balance")]
#     ]
#     return ReplyKeyboardMarkup(main_keyboard)



# def message_handler(update: Update, context: CallbackContext):
#     users = update.message.from_user
#     message_type = update.message.chat.type
#     text = update.message.text
#     # if text=="Login":
#     #             update.message.reply_text(text ="Select your Preferred Game!", reply_markup=main_menu_keyboard())
#     if text=="Spinning Win":
#                 update.message.reply_text(text ="Coming Soon")
#     elif text=="Keno":
#                 update.message.reply_text(text ="Coming Soon")
#     elif text=="Lotter":
#                         update.message.reply_text(text ="Coming Soon")
#     elif text=="Sport Betting":
#                 update.message.reply_text(text ="Coming Soon")
#     elif text=="W-Balance":
#                 update.message.reply_text(text ="Coming Soon")



# def handle_button_click(update: Update, context: CallbackContext):
#     query = update.callback_query
#     query.answer()
#     if query.data == "login":
#          context.bot.send_message(chat_id=update.effective_user.id, text="Select your Preferred Game!" ,reply_markup=main_menu_keyboard())


# # def login_button():
# #     btn = [
# #         [KeyboardButton(text="Login", callback_data="login")],
# #     ]
# #     return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder="press Buttons", one_time_keyboard=True)


# def login_button():
#     btn = [
#         [InlineKeyboardButton(text="Login", callback_data="login")],
#     ]
#     return InlineKeyboardMarkup(btn)


# def start(update: Update, context: CallbackContext):
#     username = update.effective_user.username
#     print(username)
#     context.bot.send_message(chat_id=update.effective_user.id,
#                              text=f"Hello Mr/Mrs. {update.effective_user.first_name} \n Wel come to Preferred Bot based Game!")
#     context.bot.send_message(chat_id=update.effective_user.id, text="Click the button to login!" ,reply_markup=login_button())


# def main():
#     updater = Updater(token="6622622533:AAEyHKSXzmE2sfb9Ig9zRrsfrjX98wLkDbs", use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("location", main_menu_keyboard))
#     dp.add_handler(MessageHandler(Filters.location or Filters.text, message_handler, pass_chat_data=True))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
#     dp.add_handler(CallbackQueryHandler(handle_button_click))



#     print('Polling...')
    
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()


#################################################################################################################################### Login With locally Stored Password
LOGIN_STATE = 1
MAIN_MENU_STATE = 2

# Create a dictionary to store user passwords (you should replace this with a proper authentication system)
user_passwords = {
    "Mekebede": "1234",
    "user2": "5678",
}


def login_button():
    btn = [
        [InlineKeyboardButton(text="Login", callback_data="login")],
    ]
    return InlineKeyboardMarkup(btn)


def start(update: Update, context: CallbackContext):
    username = update.effective_user.username
    print(username)
    context.bot.send_message(chat_id=update.effective_user.id,
                             text=f"Hello Mr/Mrs. {update.effective_user.first_name} \n Wel come to Preferred Bot based Game", reply_markup=login_button())


def handle_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == "login":
       return ready_to_start(update, context)



def ready_to_start(update: Update, context: CallbackContext):
    context.user_data['login_attempts'] = 0
    context.bot.send_message(chat_id=update.effective_user.id, text="Please enter your password:")
    return LOGIN_STATE

def start_login(update: Update, context: CallbackContext):
    user = update.message.from_user
    password = update.message.text
    context.user_data['login_attempts'] = 0
    context.bot.send_message(chat_id=update.effective_user.id, text="Please enter your password:")

    # Replace 'user1' with the actual user ID or username
    if user.username in user_passwords and user_passwords[user.username] == password:
        update.message.reply_text("Login successful!")
        context.user_data['login_attempts'] = 0
        return main_menu(update, context)
    else:
        context.user_data['login_attempts'] += 1
        if context.user_data['login_attempts'] >= 3:
            update.message.reply_text("Too many login attempts. Please try again later.")
            return ConversationHandler.END
        else:
            update.message.reply_text("Incorrect password. Please try again:")
            return LOGIN_STATE

# Modify the main_menu function to include the inline keyboard for login
def main_menu(update: Update, context: CallbackContext):
    main_keyboard = [
        [KeyboardButton(text="🌀 Spinning Win"), KeyboardButton(text="🗑 Keno")],
        [KeyboardButton(text=" 🎟 Lotter"), KeyboardButton(text="⚽ Sport Betting")],
        [KeyboardButton(text=" 👛 W-Balance")]
    ]
    reply_markup = ReplyKeyboardMarkup(main_keyboard)
    update.message.reply_text("Select your Preferred Game!", reply_markup=reply_markup)
    return MAIN_MENU_STATE

def message_handler(update: Update, context: CallbackContext):
    users = update.message.from_user
    message_type = update.message.chat.type
    text = update.message.text
    # if text=="Login":
    #             update.message.reply_text(text ="Select your Preferred Game!", reply_markup=main_menu_keyboard())
    if text=="🌀 Spinning Win":
                update.message.reply_text(text ="Coming Soon")
    elif text=="🗑 Keno":
                update.message.reply_text(text ="Coming Soon")
    elif text=="🎟 Lotter":
                        update.message.reply_text(text ="Coming Soon")
    elif text=="⚽ Sport Betting":
                update.message.reply_text(text ="Coming Soon")
    elif text=="👛 W-Balance":
                update.message.reply_text(text ="Coming Soon")

def main():
    updater = Updater(token="6622622533:AAEyHKSXzmE2sfb9Ig9zRrsfrjX98wLkDbs", use_context=True)
    dp = updater.dispatcher

    # Add conversation handler
    conversation_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command,ready_to_start)],
        states={
            MAIN_MENU_STATE: [CallbackQueryHandler(handle_button_click)],
            LOGIN_STATE: [MessageHandler(Filters.text & ~Filters.command, start_login)],
        },
        fallbacks=[],
    )
    dp.add_handler(conversation_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_button_click))
    dp.add_handler(MessageHandler(Filters.location | Filters.text, message_handler, pass_chat_data=True))
    print('Polling...')
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()