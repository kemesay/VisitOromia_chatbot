import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler

FIRST_NAME, LAST_NAME, EMAIL, FEEDBACK = range(4)

def fd_button():
    btn = [
        [KeyboardButton(text="Feedback", callback_data="feed")],
    ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder="press Buttons", one_time_keyboard=True)

def start(update: Update, context: CallbackContext):
    context.bot.send_photo(chat_id=update.effective_user.id, photo=open("visit_oromia.jpg", "rb"),
                           caption="Wel come to Oromia, the land rich in nature!")
    context.bot.send_message(chat_id=update.effective_user.id,
                             text=f"Hello Mr/Mrs. {update.effective_user.first_name} \n Wel Come to Visit Oromia Land of Diverse Beauty, Oromia!", reply_markup=fd_button())
    

def message_overtaken(update: Update, context: CallbackContext):
    print("text", update.message.text)
    
    if update.message.text == 'Feedback':
        context.bot.send_message(chat_id=update.effective_user.id, text="Great! Please enter your first name.!")
        return FIRST_NAME

def collect_feedback(update: Update, context: CallbackContext):
    user = update.message.from_user
    context.user_data['first_name'] = update.message.text
    update.message.reply_text("Great! Now, please enter your last name.")
    return LAST_NAME

def collect_last_name(update: Update, context: CallbackContext):
    context.user_data['last_name'] = update.message.text
    update.message.reply_text("Please enter your email address.")
    return EMAIL

def collect_email(update: Update, context: CallbackContext):
    context.user_data['email'] = update.message.text
    update.message.reply_text("Please enter your feedback.")
    return FEEDBACK

def save_feedback(update: Update, context: CallbackContext):
    feedback = {
        'first_name': context.user_data['first_name'],
        'last_name': context.user_data['last_name'],
        'email': context.user_data['email'],
        'feedbackText': update.message.text
    }

    # Send feedback to your Spring Boot API
    send_feedback_to_api(feedback)
    user = update.message.from_user

    update.message.reply_text(f"Thank you for your feedback, {user.first_name}! It has been submitted.")
    return ConversationHandler.END

def send_feedback_to_api(feedback):
    import requests

    api_url = 'http://localhost:9000/feedback/giveFeedback'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=feedback, headers=headers)

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Feedback submission canceled.")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text & ~Filters.command, message_overtaken)],
    states={
        FIRST_NAME: [MessageHandler(Filters.text & ~Filters.command, collect_feedback)],
        LAST_NAME: [MessageHandler(Filters.text & ~Filters.command, collect_last_name)],
        EMAIL: [MessageHandler(Filters.text & ~Filters.command, collect_email)],
        FEEDBACK: [MessageHandler(Filters.text & ~Filters.command, save_feedback)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# query_handler = CallbackQueryHandler(button)

def main():
    updater = Updater(token='6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI', use_context=True)  # Replace with your bot token
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(conv_handler)
    # dispatcher.add_handler(query_handler)
    print('Polling...')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
