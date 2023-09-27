from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Location, ReplyKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Updater, CommandHandler, MessageHandler, \
    Filters, ConversationHandler, CallbackQueryHandler
import haversine as hs
import asyncio
import logging
import requests
import time
import json
import threading


running_thread = None

exit_event = threading.Event()


FIRST_NAME, LAST_NAME, EMAIL, FEEDBACK = range(4)

# Define your callback data
RASA_API_ENDPOINT = 'http://localhost:5005/webhooks/rest/webhook'
TOKEN = '6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI'
bot = Updater(token= TOKEN, use_context=True) 

LATITUDE = 0.0
LONGITUDE = 0.0
WELCOME_MESSAGE = "Hello User Please Provide Your Location"
NEAR_DESTINATION_KEYBOARD_NAME = ""
NEAR_OTC_KEYBOARD_NAME = ""
HELP = ""
MESSAGE_TO_USER = ""
LOCATION = ""
PLACE_HOLDER = ""

list_of_Destinations = [
    {'latitude': 7.647625224722821, 'longitude': 38.731213001456624},
    {'latitude': 7.615638743254676, 'longitude': 38.59388389415154},
    {'latitude': 9.711757463938003, 'longitude': 38.847613854882354},
    {'latitude': 9.089275309782645, 'longitude': 38.75844099940962},
    {'latitude': 8.79623507085179,  'longitude': 37.89363482941316},
                      ]
otc = [
    {'latitude': 8.990634168076502, 'longitude': 38.78404357187282},
   
      ]
hotels = [
    {'latitude': 8.988003282374752, 'longitude': 38.78946504509636},
    {'latitude': 9.015493806998286, 'longitude': 38.78427163451814},
    {'latitude': 9.014833807512632, 'longitude': 38.769248023770395},
    {'latitude': 9.020306059374253, 'longitude': 38.75993171603812}
      ] 

banks = [
    {'latitude': 8.991335586080913, 'longitude': 38.7822373258349},
    {'latitude': 9.003357020524302, 'longitude': 38.7813264674275},
    {'latitude': 8.547092630235948, 'longitude': 39.271115058583014},
    {'latitude': 9.008054752232862, 'longitude': 38.764944649753765}
      ]


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main_menu_keyboard():
    main_keyboard = [
        [InlineKeyboardButton(text="Distance From Info Center", request_location=True, callback_data='m1')],
        [InlineKeyboardButton(text="Nearest Destinations", request_location=True, callback_data='m2')],
        [InlineKeyboardButton(text="Nearest Hotels to You", request_location=True, callback_data='h1')],
        [InlineKeyboardButton(text="Nearest Banks to you", request_location=True, callback_data='b1')],
        [InlineKeyboardButton(text="Help", callback_data='m3')]]

    return InlineKeyboardMarkup(main_keyboard, request_location=True)

def inline_buttons():
    btn = [
        [
            KeyboardButton(text=LOCATION, request_location=True, id=1)
        ],
    ]
    # print("calculate_nearest_location")
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder=PLACE_HOLDER, one_time_keyboard=True)


def nearest_of_otc_function(update: Update, context: CallbackContext):
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    # print(query.answer())
    # print(query.data)
    
    if query.data == "m2":
        calculated_data = calculate_nearest_location(latitude=LATITUDE, longitude=LONGITUDE,
                                        destinations=list_of_Destinations, num_locations=3)
    elif query.data == "m1":
        calculated_data = calculate_nearest_location(latitude=LATITUDE, longitude=LONGITUDE,
                                                      destinations=otc, num_locations=3)
    elif query.data == "h1":
        calculated_data = calculate_nearest_location(latitude=LATITUDE, longitude=LONGITUDE,
                                                      destinations=hotels, num_locations=3)
    elif query.data == "b1":
        calculated_data = calculate_nearest_location(latitude=LATITUDE, longitude=LONGITUDE,
                                                      destinations=banks, num_locations=3)
    else:
        context.bot.send_message(chat_id=update.effective_user.id, text="Hello Help is here")
        return

    for i, nearest_destination in enumerate(calculated_data):
        lat = float(nearest_destination["latitude"])
        lng = float(nearest_destination["longitude"])
        context.bot.send_location(update.effective_user.id, latitude=lat, longitude=lng, live_period=60, heading=180,
                                  allow_sending_without_reply=True)
        if i == 2:  # Send only the first 3 nearest locations
            break

def help_function(update: Update, context: CallbackContext):
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer(text=f"Hello User provide Your Location")

    if query.data == "m3":
        query.message.reply_markdown(
            text=f"Hello {update.effective_user.first_name} Provide Your location by using the location button")
        # print(query.message.location, 'helolollollllllll')

def message_handler(update: Update, context: CallbackContext):
    global LATITUDE
    global LONGITUDE
    global MESSAGE_TO_USER
    LATITUDE = update.message.location.latitude
    LONGITUDE = update.message.location.longitude
    if update.message.location:
        logger.info("Received location: LATITUDE=%f, LONGITUDE=%f", LATITUDE, LONGITUDE)
        context.bot.send_message(chat_id=update.effective_user.id, text="Where you Go!" ,reply_markup=main_menu_keyboard())
        # context.bot.sendMessage(update.effective_user.id, text="Hello I got You The Desired Location")
        
    else:
        logger.warning("No location provided by user: %s", update.effective_user.username)
        context.bot.send_message(chat_id=update.effective_user.id, text=f"Hello {update.effective_user.first_name} You Must Provide Your Location To Get The Nearest Destination and OTC Head Office")

def calculate_nearest_location(latitude, longitude, destinations, num_locations=3):
    location_tuple1 = (latitude, longitude)
    location_distances = []
    # print("calculate_nearest_location")
    if latitude and longitude and destinations:
        for i in range(len(destinations)):
            location_tuple2 = (destinations[i]['latitude'], destinations[i]['longitude'])
            distance = hs.haversine(location_tuple1, location_tuple2)
            my_dict = {
                "destination": destinations[i],
                "distance": distance
            }
            location_distances.append(my_dict)
    location_distances.sort(key=lambda x: x['distance'])  # Sort locations by distance
    nearest_destinations = [
        entry['destination'] for entry in location_distances[:num_locations]
    ]
    return nearest_destinations
   

def inline_buttons():
    btn = [
        [
            KeyboardButton(text="Your Location", request_location=True, id=1)
        ],
    ]
    # print("calculate_nearest_location")
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder="press Buttons", one_time_keyboard=True)
def rate_me():
    
    btn = [
        [KeyboardButton(text="Rate", callback_data="rate1")],
    ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder="press Buttons", one_time_keyboard=True)

    
    
################################################################################################################################
FIRST_NAME, LAST_NAME, EMAIL, FEEDBACK = range(4)

def fd_button():
    btn = [
        [KeyboardButton(text="Feedback", callback_data="feed")],
    ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True, input_field_placeholder="press Buttons", one_time_keyboard=True)

count=0
dict_user = {}

def message_overtaken(update: Update, context: CallbackContext):
    global count  # Add this line
    users = update.message.from_user
    dict_user[users.id] = count
    # print("text from overtaken message", update.message.text )
    if update.message.text == 'Feedback':
        dict_user[users.id] = count+1
        context.bot.send_message(chat_id=update.effective_user.id, text="Great! Please enter your first name.!")
        return FIRST_NAME

def collect_feedback(update: Update, context: CallbackContext):
    global count 
    users = update.message.from_user

    dict_user[users.id] = count+2

    user = update.message.from_user
    context.user_data['first_name'] = update.message.text
    update.message.reply_text("Great! Now, please enter your last name.")
    return LAST_NAME

def collect_last_name(update: Update, context: CallbackContext):
    global count
    users = update.message.from_user
 
    dict_user[users.id] = count+3
    context.user_data['last_name'] = update.message.text
    update.message.reply_text("Please enter your email address.")
    return EMAIL

def collect_email(update: Update, context: CallbackContext):
    global count
    users = update.message.from_user
    dict_user[users.id] = count+4

    context.user_data['email'] = update.message.text
    update.message.reply_text("Please enter your feedback.")
    return FEEDBACK

def save_feedback(update: Update, context: CallbackContext):
    global count
    users = update.message.from_user
    del  dict_user[users.id]

    feedback = {
        'first_name': context.user_data['first_name'],
        'last_name': context.user_data['last_name'],
        'email': context.user_data['email'],
        'feedbackText': update.message.text
    }

    # Send feedback to your Spring Boot API
    send_feedback_to_api(feedback)
    user = update.message.from_user

    update.message.reply_text(f"Thank you for your feedback that strength me, {user.first_name}! It has been submitted and I have been working on it.")
    return ConversationHandler.END

def send_feedback_to_api(feedback):
    import requests

    api_url = 'http://localhost:9000/feedback/giveFeedback'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=feedback, headers=headers)

def cancelf(update: Update, context: CallbackContext):
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
    fallbacks=[CommandHandler('cancelf', cancelf)],
)

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
    if response.status_code == 201:
        return True
    return False
list_button_click = ["Thanks!", "Thanks a lot!", "Thank you very much!", "Thank you so much!", "Thank you from the bottom of my heart!"]

def calculate_rate(update, context):
    rate = 0.0

    query = update.callback_query
    payload = query.data
    if payload in list_button_click:
        query.answer()
        if payload=="Thank you from the bottom of my heart!":
            rate=5.0
        elif payload=="Thank you so much!":
           rate=4.0
        elif payload=="Thank you very much!":
           rate=3.0
        elif payload=="Thank a lot!":
           rate=2.0
        elif payload=="Thanks!":
           rate=1.0
    return rate

def cancel(update, context):
    update.message.reply_text("Rate collection canceled.")
    

def start(update: Update, context: CallbackContext):
    username = update.effective_user.username
    print(username)
    context.bot.send_photo(chat_id=update.effective_user.id, photo=open("visit_oromia.jpg", "rb"),
                           caption="Wel come to Oromia, the land rich in nature!")
    context.bot.send_message(chat_id=update.effective_user.id,
                             text=f"Hello Mr/Mrs. {update.effective_user.first_name} \n Wel Come to Visit Oromia Land of Diverse Beauty, Oromia!")
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
            
        text_responses.append(text)
        
        button_titles = [button['title'] for button in buttons]
        # Split button_titles into pairs of buttons
        button_pairs = [button_titles[i:i+2] for i in range(0, len(button_titles), 2)]
        
        if button_pairs:
            # Create a list of lists of KeyboardButton objects for each pair
            pair_keyboard_buttons = [[KeyboardButton(title) for title in pair] for pair in button_pairs]
            keyboard_buttons.extend(pair_keyboard_buttons)
            
    key1 = keyboard_buttons  
    key2 = fd_button().keyboard + rate_me().keyboard + inline_buttons().keyboard
    # Create a ReplyKeyboardMarkup with the keyboard buttons
    
    new_key2 = []

    # Iterate through key1 and group consecutive lists
    i = 0
    while i < len(key2):
        if i + 1 < len(key2):
            # Combine two consecutive lists into a single list
            new_row = key2[i] + key2[i + 1]
            new_key2.append(new_row)
            i += 2  # Skip the next list
        else:
            # If there's only one list left, append it as is
            new_key2.append(key2[i])
            i += 1

    # Replace key1 with the modified list
    key3=  key1 + new_key2

    reply_markup = ReplyKeyboardMarkup(key3, one_time_keyboard=True, resize_keyboard=True)
    # Send text responses along with the reply keyboard
    for text_response in text_responses:
        update.message.reply_text(text_response, reply_markup=reply_markup)


def handle_message(update: Update, context: CallbackContext):
    global count
    users = update.message.from_user
    message_type = update.message.chat.type
    text = update.message.text
    
    if text=="Feedback" and  count == 0:
        return message_overtaken(update, context)
    elif  users.id in dict_user.keys():
        
        if dict_user[users.id]==1:
            # print(dict_user)
            return collect_feedback(update, context)
        elif dict_user[users.id]==2:
            return collect_last_name(update, context)
        elif dict_user[users.id]==3:
                    
            return collect_email(update, context)
        elif dict_user[users.id]==4:
            return save_feedback(update, context)
    elif text=="Rate":
        rate_key =[[InlineKeyboardButton(text="⭐", callback_data="Thanks!"), 
                                        InlineKeyboardButton(text="⭐⭐", callback_data="Thanks a lot!"), 
                                        InlineKeyboardButton(text="⭐⭐⭐", callback_data="Thank you very much!"),
                                        ],
                                        
                                       [ InlineKeyboardButton(text="⭐⭐⭐⭐", callback_data="Thank you so much!"),
                                         InlineKeyboardButton(text="⭐⭐⭐⭐⭐", callback_data="Thank you from the bottom of my heart!"),
                                         ]
                                        ]
        
        reply_markup = InlineKeyboardMarkup(rate_key)
        update.message.reply_text("📹 Please rate me 📷", reply_markup=reply_markup)
        
    else:
        # print("rhis is double text", text)
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
            button_pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
            # Create the keyboard markup with pairs of buttons
            keyboard = [
                [InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in button_pair]
                for button_pair in button_pairs
            ]
            
            reply_markup = InlineKeyboardMarkup(keyboard)

            if entry.get('image'):
                update.message.reply_photo(entry['image'], caption=text, reply_markup=reply_markup)
            elif entry.get("attachment"):
                attachment = entry["attachment"]
                if attachment and attachment.get('type') == 'video':
                    # print("this is video", attachment)
                    payload = attachment.get('payload')
                    if payload:
                        # title = payload.get('title', 'Default Title')
                        src = payload.get('src')
                    # Send a message with the video link
                        update.message.reply_text(src, reply_markup=reply_markup)
            else:
                update.message.reply_text(text, reply_markup=reply_markup)

def stop_running_thread():
    global exit_event
    exit_event.set()  # Signal the running thread to exit gracefully

# Add a handler to stop the running thread when necessary
def handle_stop_command(update, context):
    stop_running_thread()
    update.message.reply_text("Stopped the current operation.")

user_threads = {}

def handle_button_click(update, context):
    query = update.callback_query
    payload = query.data
    user_id = update.effective_user.id
    username = update.effective_user.username
    
    # Start a new thread to handle the request
    new_thread = threading.Thread(target=process_request, args=(update, context, query, payload, user_id, username))
    new_thread.start()

# Button Click Handling
def process_request(update, context, query, payload, userId, username):
    query = update.callback_query
    payload = query.data
    userId = update.effective_user.id
    username = update.effective_user.username
    print(username)
    try:
            if payload in list_button_click:
                query.answer()
                rate = calculate_rate(update, context)
            #    print(rate,"yououououououououo")
                if send_rate_to_api(rate, userId, username):
                    query.edit_message_text(payload)
                    #  query.edit_message_text(f"{payload}, It has been submitted.")
                else:
                    context.bot.send_message(chat_id=query.message.chat_id, text="Rate is once only, Thank you!.")

            else:
                payload = {
                    'sender': query.message.chat_id,
                    'message': payload
                }
                response = requests.post(RASA_API_ENDPOINT, json=payload).json()
                # print("response", response)
                
                message = None
                chat_id =update.callback_query.message.chat_id

                for entry in response:
                    text = entry.get('text', '')
                    buttons = entry.get('buttons', [])
                    button_pairs = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
                    
                    # Create the keyboard markup with pairs of buttons
                    keyboard = [
                        [InlineKeyboardButton(button['title'], callback_data=button['payload']) for button in button_pair]
                        for button_pair in button_pairs
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    if entry.get('image'):
                # Sleep for 5 seconds before sending the image (adjust as needed)
                        time.sleep(5)
                
                        if message:
                            # If there's an existing message, edit it with the new image and caption
                            context.bot.edit_message_media( media=InputMediaPhoto(entry['image']),  reply_markup=reply_markup, chat_id=chat_id ,message_id=message.message_id )
                            
                            # message.edit_media( media=InputMediaPhoto(entry['image']),  caption=text, reply_markup=reply_markup )
                        else:
                            # If there's no existing message, send the first image
                            message = query.message.reply_photo( photo=entry['image'], caption=text, reply_markup=reply_markup )
                    elif entry.get("attachment"):
                        attachment = entry["attachment"]
                        if attachment and attachment.get('type') == 'video':
                            # print("this is video", attachment)
                            payload = attachment.get('payload')
                            if payload:
                                title = payload.get('title', 'Default Title')
                                src = payload.get('src')
                            # Send a message with the video link
                                query.edit_message_text(f"Check this video: {title}\n{src}", reply_markup=reply_markup)
                                # await time.sleep(5)
                                time.sleep(5)  # Add a delay of 5 seconds
                    else:
                        query.edit_message_text(text, reply_markup=reply_markup)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        global running_thread
        running_thread = None
        exit_event.clear()
                
def main():
    updater = Updater(token="6549938880:AAGSRCR5a6IY1qg9Y-SFp__bkkA2nOLxoHI", use_context=True)
    dp = updater.dispatcher

    # Add command handler to start the bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("location", main_menu_keyboard))
    dp.add_handler(MessageHandler(Filters.location or Filters.text, message_handler, pass_chat_data=True))
    dp.add_handler(CallbackQueryHandler(pass_chat_data=True, callback=nearest_of_otc_function, pattern="m2"))
    dp.add_handler(CallbackQueryHandler(pass_chat_data=True, callback=nearest_of_otc_function, pattern="m1"))
    dp.add_handler(CallbackQueryHandler(pass_chat_data=True, callback=nearest_of_otc_function, pattern="h1"))
    dp.add_handler(CallbackQueryHandler(pass_chat_data=True, callback=nearest_of_otc_function, pattern="b1"))
    dp.add_handler(CallbackQueryHandler(pass_chat_data=True, callback=help_function, pattern="m3"))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    # Commands
    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(CallbackQueryHandler(handle_button_click))
    dp.add_handler(CommandHandler('cancel', cancel))
    # dp.add_handler(CallbackQueryHandler(collect_rate))
    dp.add_handler(CommandHandler("stop", handle_stop_command))


    print('Polling...')
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
