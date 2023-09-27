import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Initialize an empty list to store selected numbers
selected_numbers = []

# Your Telegram bot token here
bot_token = 'YOUR_BOT_TOKEN'
# API endpoint URL
api_url = 'http://localhost:900/api/keno'

# Command handler to start the game
def start_game(update, context):
    # Clear the selected numbers list when starting a new game
    selected_numbers.clear()

    rate_key = [
        [InlineKeyboardButton(text=str(i), callback_data=str(i)) for i in range(1, 81)]
    ]

    reply_markup = InlineKeyboardMarkup(rate_key)
    update.message.reply_text("Select six different numbers:", reply_markup=reply_markup)

# Callback handler for button clicks
def button_click(update, context):
    query = update.callback_query
    number = int(query.data)

    if number in selected_numbers:
        # Number is already selected, unselect it
        selected_numbers.remove(number)
    elif len(selected_numbers) < 6:
        # Number is not selected, select it if less than 6 numbers are selected
        selected_numbers.append(number)

    # Update the message with the current selected numbers
    query.edit_message_text(f"Selected numbers: {selected_numbers}")

# Command handler to send selected numbers to the API
def send_to_api(update, context):
    if len(selected_numbers) == 6:
        # Send the selected numbers to the API
        response = requests.post(api_url, json={'selected_numbers': selected_numbers})

        if response.status_code == 200:
            update.message.reply_text("Numbers sent to API successfully!")
        else:
            update.message.reply_text("Failed to send numbers to API.")
    else:
        update.message.reply_text("You must select exactly six numbers before sending to API.")

def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_game))
    dp.add_handler(CallbackQueryHandler(button_click))
    dp.add_handler(CommandHandler("sendtoapi", send_to_api))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
