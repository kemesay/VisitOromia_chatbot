# This files contains your custom actions which can be used to run
# custom Python code.
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"
from ast import Import
# from tkinter import Button, Menu
from typing import Any, Text, Dict, List, Union
# from rasa_core.agent import Agent
from rasa_sdk import Action, Tracker
import time
# from rasa import Action
# from telegram import MenuButton, InlineKeyboardButton, update, KeyboardButton, replymarkup
# from telegram.ext import(callbackcontext, Filters   ,Updater, CommandHandler, callbackqueryhandler, CallbackContext)

from rasa_sdk.interfaces import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
# from rasa.core import FormAction

from rasa_sdk.forms import FormValidationAction
# from chatdb import DataUpdate 
# import webbrowser 
# from js2py.pyjs import *
# from translate import Translator
# from pafy import youtube_dl
# import pafy
# import tmp
# import telegram


# from googleapiclient.discovery import build
# from googletrans import Translator
#from textblob import TextBlob
#from iso639 import languages
# TOKEN '5219022598:AAHTKsAb9mI10CW0e2TgBA5YtDkoBAYPbLI'
# bot = telegram.bot(TOKEN)
# print(bot.get_me())
#  if bot.get_updates():
#     chat_id = bot.get_updates()(-1).message.chat_id
#     video = 'https://youtu.be/kBRkY5EUzZw'
#     bot.send_video(chat_id, video)    
# class ActionFirstName(Action):
#           def name(self) -> Text: 
#                              """Unique identifier of the form"""
#                              return "action_last_name"

#           def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                  dispatcher.utter_message(utter_message="utter_last_name")
#                  return [SlotSet('firstN',tracker.latest_message['text'])]

# class ActionFeedback(Action): 
#         def name(self) -> Text: 
#                    return "action_feedback"

#         def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                                   dispatcher.utter_message(template="utter_feedback")
#                                   return [SlotSet('lastN',tracker.latest_message['text'])]


# class ActionSubmit(Action): 
#         def name(self) -> Text: 
#                       return "action_submit"

#         def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                         DataUpdate(tracker.get_slot("firstN"),  tracker.get_slot("lastN"),tracker.get_slot("feedback")) 
#                         dispatcher.utter_message("Thanks for the valuable feedback. ") 
#                         return []
                    

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, List, Dict, Any

class ActionSubmitFeedback(Action):
    def name(self) -> Text:
        return "action_submit_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return []

                         
# class Actionmenu(Action):
     
#     def name(self) -> Text:
#         return "menuction_exercise"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
#         buttons =[
#             {"payload":"/otc", "title": "OTC (Oromia Commission Tourism)"},
#             {"payload":"/visitoromia", "title": "Visit Oromia"},
#             {"payload":"/covid", "title": "Covid_19 Information"},
#             {"payload":"/live_chat", "title": "Connect With Agent"},
#             {"payload":"/request_form", "title": "Feedback"},
#             {"payload":"/Language_setting", "title": "Select your Language"},
#             {"payload":"/gallery", "title": "Gallery"}  
#         ]
        
#         intent = tracker.latest_message['intent'].get('name')
#         if intent == "/start":
#          dispatcher.utter_message(text="I can Help you with the following concept", buttons=buttons)
  
#         return [] 

class Actionoda(Action):
     
    def name(self) -> Text:
        return "odaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Oda_Nabe_ji8BqOX.jpg")
  
        return []
    
class Actionctuma(Action):
         
    def name(self) -> Text:
        return "ctumaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Cafe_Tuma.jpg")  
        return []
    
class Actionbtown(Action):
         
    def name(self) -> Text:
        return " btownaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=HtGAJyMfago")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Bishoftu.jpg")
  
        return []
    
class Actionlakeharsade(Action):
         
    def name(self) -> Text:
        return " lakeharsadeaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Lake_Hora_Harsade.jpg")
  
        return []

class Actionlakebishoftu(Action): 
         
    def name(self) -> Text:
        return " lakebishoftuaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/lake_bishoftu_Dream_Land_Resort.jpg")
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Other_Attractions_in_Bishoftu_Town.jpg")
  
        return []
    
class Actionlbabogaya(Action):
         
    def name(self) -> Text:
        return " babogayaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Lake_Babogaya.jpg")
  
        return []

class Actionlakekuriftu(Action):
         
    def name(self) -> Text:
        return "kuriftuaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []

class ActionLkilole(Action):
         
    def name(self) -> Text:
        return "lkiloleaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Lake_Kilole.jpg")
  
        return []
    
class Actionlmagarisa(Action):
         
    def name(self) -> Text:
        return "lmagarisaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionlmzuqala(Action):
         
    def name(self) -> Text:
        return "zuqalaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []

class Actionlmyarar(Action):
         
    def name(self) -> Text:
        return "myararaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(image="https://otc.visitoromia.org/uploads/route_image/Mountain_Yarar.jpg")
  
        return []
    
    
class Actionadama(Action):
         
    def name(self) -> Text:
        return "adamaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=dkSxsSwCeRA")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []  

class Actionoromomartyr(Action):
         
    def name(self) -> Text:
        return "omartyraction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []  
    
class Actiongarhotspring(Action):
         
    def name(self) -> Text:
        return "garhotspringaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []
    
class Actionboku(Action):
         
    def name(self) -> Text:
        return "bokuaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
  
        return []
    
class Actionlsodarespa(Action):
         
    def name(self) -> Text:
        return "sodarespaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondhera(Action):
         
    def name(self) -> Text:
        return "dheraaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondambal(Action):
         
    def name(self) -> Text:
        return "dambalaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=we4areB_wQA")
   
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionlangano(Action):
         
    def name(self) -> Text:
        return "langanoaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionabijata(Action):
         
    def name(self) -> Text:
        return "abijataaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=3AuYjdZ3KqU")
        
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionmanageshasuba(Action):
         
    def name(self) -> Text:
        return "subaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=2esV9zdieZ8")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=38uWcycFa3o")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=F20NHKh-P54")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=jsavm7HvGwc")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=Bu8OF-Sc8Cg")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionfinfi_alemchurch(Action):
         
    def name(self) -> Text:
        return "fin_alem_churchaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionchilimogaji(Action):
         
    def name(self) -> Text:
        return "chilimogajiaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondandi(Action):
         
    def name(self) -> Text:
        return "dandiaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionambo(Action):
         
    def name(self) -> Text:
        return "amboaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=N4WLHdqMTt8")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=yCfpGnaFwPA")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionwhenchi(Action):
         
    def name(self) -> Text:
        return "wenchiaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=g4eL-ojRR74")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=TSKIfUaohZE")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=wQS9cJjDfYU")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=Wz_LcylAt8M")

        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []

class Actionadadimariam(Action):
         
    def name(self) -> Text:
        return "adadimariamaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=Wc64lfh8JdA")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=IIHMlklIysc")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=k62Rl9zSnqE")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []

class Actionmugar_valley(Action):
         
    def name(self) -> Text:
        return "mugar_valleyaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        dispatcher.utter_message(attachment= "https://youtu.be/GB-UhaijKO4")
        dispatcher.utter_message(attachment="https://youtu.be/GB-UhaijKO4")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    

class Actiondebra_libanos(Action):
         
    def name(self) -> Text:
        return "debra_libanosyaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=mpaRVOaEGYE")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=wvQES92POPQ")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=-3Ro7Y0ORFU")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=34Tl1SKMLNU")
        
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return [] 
    
class Actionportugues_bridge(Action):
         
    def name(self) -> Text:
        return "portugues_bridgeaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://www.youtube.com/watch?v=-3Ro7Y0ORFU")
        dispatcher.utter_message(attachment= "https://www.youtube.com/watch?v=mDBT7WTZemk")
        dispatcher.utter_message(attachment="https://youtu.be/4X9jjM6iGK8")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/one.png")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return [] 
    
    
class Actionguha_tsion_mariam(Action):
         
    def name(self) -> Text:
        return "guha_tsion_mariamaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionsankalle_wild(Action):
         
    def name(self) -> Text:
        return "sankalle_wildaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionforest_scenery(Action):
         
    def name(self) -> Text:
        return "forest_sceneryaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionmee_boko(Action):
         
    def name(self) -> Text:
        return "mee_bokoaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
    
class Actionaround_borana(Action):
         
    def name(self) -> Text:
        return "around_boranaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiontown_mega_yabelo(Action):
         
    def name(self) -> Text:
        return "town_mega_yabeloaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionbokes(Action):
         
    def name(self) -> Text:
        return "bokesaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiongalana_abaya(Action):
         
    def name(self) -> Text:
        return "galana_abayaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []

class Actionwallame_hot_spring(Action):
         
    def name(self) -> Text:
        return "wallame_hot_springaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []

class Actiongibe_gorge(Action):
         
    def name(self) -> Text:
        return "gibe_gorgeaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionjimma(Action):
         
    def name(self) -> Text:
        return "jimmaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionaba_jifar_palace(Action):
         
    def name(self) -> Text:
        return "aba_jifar_palaceaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiontropical_forest_jimma_illuababora(Action):
         
    def name(self) -> Text:
        return "tropical_forest_jimma_illuababoraaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionfalls_around_jimma_Hu(Action):
         
    def name(self) -> Text:
        return "falls_around_jimma_Huaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionsor_water_fall(Action):
         
    def name(self) -> Text:
        return "sor_water_fallaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiongore_town(Action):
         
    def name(self) -> Text:
        return "gore_townaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionmuseums_arsi_asala(Action):
         
    def name(self) -> Text:
        return "museums_arsi_asalaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionanole_martyr_monument(Action):
         
    def name(self) -> Text:
        return "anole_martyr_monumentaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionarsi_mountains_national_park(Action):
         
    def name(self) -> Text:
        return "arsi_mountains_national_parktaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondodola_adaba_forest(Action):
         
    def name(self) -> Text:
        return "dodola_adaba_forestaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionbale_moountains_national_park(Action):
         
    def name(self) -> Text:
        return "bale_moountains_national_parkaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionsanate(Action):
         
    def name(self) -> Text:
        return "sanateaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionmada_walabu(Action):
         
    def name(self) -> Text:
        return "mada_walabuaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionsof_umar_cafe(Action):
         
    def name(self) -> Text:
        return "sof_umar_cafeuaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondire_sheikh_hussein(Action):
         
    def name(self) -> Text:
        return "dire_sheikh_husseinaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionwabe_gorge(Action):
         
    def name(self) -> Text:
        return "wabe_gorgeaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionasabo_mountains_monestrye(Action):
         
    def name(self) -> Text:
        return "asabo_mountains_monestryaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionjalo_kunni_mukhtar_forest(Action):
         
    def name(self) -> Text:
        return "jalo_kunni_mukhtar_forestaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionoda_bultum(Action):
         
    def name(self) -> Text:
        return "oda_bultumaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionburka_kobtu_sama_hot_spring(Action):
         
    def name(self) -> Text:
        return "burka_kobtu_sama_hot_springaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class ActionChororapithecus(Action):
         
    def name(self) -> Text:
        return "Chororapithecusaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionharala_ruins(Action):
         
    def name(self) -> Text:
        return "harala_ruinsaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondindin_forest(Action):
         
    def name(self) -> Text:
        return "dindin_forestaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionchalanko_oromo_martyr_memorial_monumentt(Action):
         
    def name(self) -> Text:
        return "chalanko_oromo_martyr_memorial_monumentaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondire_dawa(Action):
         
    def name(self) -> Text:
        return "dire_dawaaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionbabile_elephant_sanctuary(Action):
         
    def name(self) -> Text:
        return "babile_elephant_sanctuaryaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionunique_rock_formation_babile(Action):
         
    def name(self) -> Text:
        return "unique_rock_formation_babileaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionmountain_kundudo(Action):
         
    def name(self) -> Text:
        return "mountain_kundudoaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actiondima_cave(Action):
         
    def name(self) -> Text:
        return "dima_caveaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(image="http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png")
  
        return []
    
class Actionoromo_cave(Action):
         
    def name(self) -> Text:
        return "oromo_caveaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
        return []
    
class Actionhistorical_mosques(Action):
         
    def name(self) -> Text:
        return "historical_mosquesaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
  
        return []
    
class Actionoda_buluk_gada_site(Action):
         
    def name(self) -> Text:
        return "oda_buluk_gada_siteaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
  
        return []
    
class Actionfincha_dam(Action):
         
    def name(self) -> Text:
        return "fincha_damaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
  
        return []
    
class Actionbareda_angar_water_fall(Action):
         
    def name(self) -> Text:
        return "bareda_angar_water_fallaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
  
        return []
    
class Actiondhati_walal_park(Action):
         
    def name(self) -> Text:
        return "dhati_walal_parkaction_exercise"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
  
        return []
    
class Actionketo_water_fall(Action):
         
    def name(self) -> Text:
        return "keto_water_fallaction_exercise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(attachment="https://youtu.be/kBRkY5EUzZw")
   
  
        return []
    
class Actionwalal_shabal(Action): 
    def name(self) -> Text:
        return "walal_shabalaction_exercise"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        dispatcher.utter_message("wait... Loading images and Video")
        dispatcher.utter_message(text="https://youtu.be/kBRkY5EUzZw")
        dispatcher.utter_message(text="https://youtu.be/GB-UhaijKO4")        
        return []
    
class Actiongalleryimage(Action):
         
    def name(self) -> Text:
        return "gallery_pictures"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        image_urls = [
            
            "https://otc.visitoromia.org/uploads/culture/4_9pkdryi.jpg", 
            "https://otc.visitoromia.org/uploads/culture/32.jpg",

            "https://otc.visitoromia.org/uploads/culture/34.jpg",
            "https://otc.visitoromia.org/uploads/culture/27.jpg",
            "https://otc.visitoromia.org/uploads/culture/26_u4kJaI5.jpg", 
            "https://otc.visitoromia.org/uploads/culture/22.jpg",
            "https://otc.visitoromia.org/uploads/culture/28_MSmJHAl.jpg",
            
            "http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png",
            "https://otc.visitoromia.org/uploads/route_image/Mountain_Yarar.jpg",
            "https://otc.visitoromia.org/uploads/culture/2_fLUMPXw.png", 
            "https://otc.visitoromia.org/uploads/route_image/Lake_Kilole.jpg", 
            "http://otc.visitoromia.org/uploads/svg/one.png", 
            "https://otc.visitoromia.org/uploads/route_image/Lake_Babogaya.jpg", 
            "https://otc.visitoromia.org/uploads/route_image/oromo_cultural_center.jpg",
            "https://otc.visitoromia.org/uploads/route_image/lake_bishoftu_Dream_Land_Resort.jpg",
            "https://otc.visitoromia.org/uploads/route_image/EUGpz_BXsAM1PQ6.jpg",
            "https://otc.visitoromia.org/uploads/route_image/lake_dembel.jpg",
            "https://otc.visitoromia.org/uploads/route_image/Lake_Langano_Resort_Area.jpg",
            "https://otc.visitoromia.org/uploads/route_image/photo_2022-03-10_16-34-33_Xp8TkQf.jpg",
            "https://otc.visitoromia.org/uploads/route_image/Lake_Magarisa.jpg", 
            "https://otc.visitoromia.org/uploads/route_image/Mountain_Chuqala_Ziquala.jpg",
 
            "https://otc.visitoromia.org/uploads/route_image/Cafe_Tuma.jpg", 
            "https://otc.visitoromia.org/uploads/route_image/Oda_Nabe_ji8BqOX.jpg",
            "http://otc.visitoromia.org/uploads/svg/photo_2022-03-03_11.15.31.png",
            "https://otc.visitoromia.org/uploads/route_image/Other_Attractions_in_Bishoftu_Town.jpg",
            "https://otc.visitoromia.org/uploads/route_image/Bishoftu.jpg" ,
            "http://otc.visitoromia.org/uploads/uploads/cropWabe-Shebelle-1-2000x1024.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-40-26.jpg",
            "http://otc.visitoromia.org/uploads/uploads/pjimage_2_OlJ1Cq5.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-43-54.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-43-13.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-58-26.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_02-00-12.jpg",
            "http://otc.visitoromia.org/uploads/uploads/cropWabe-Shebelle-1-2000x1024.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-45-16.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-54-33.jpg",
            "http://otc.visitoromia.org/uploads/uploads/photo_2022-03-20_01-55-05.jpg",
            "https://otc.visitoromia.org/uploads/activity/Pilgrimage_GabubCr.jpg"    
        ]
        for image_url in image_urls:
            dispatcher.utter_message(image=image_url)
        return []
     

        
        # return []
    
class Actiongalleryvideos(Action):
         
    def name(self) -> Text:
        return "gallery_videos"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[EventType]:
        # dispatcher.utter_message("wait... Loading Video")
        videos = [    
                    {"title": "Video 1", "src": "https://www.youtube.com/watch?v=TpkVjMEWzTs"},
                    {"title": "Video 2", "src": "https://www.youtube.com/watch?v=vwRchLuFruo"},

                    {"title": "Video 3", "src": "https://www.youtube.com/watch?v=4-TWBOku6eQ"},
                    {"title": "Video 4", "src": "https://www.youtube.com/watch?v=HXWwgu1gaNk"},
                    {"title": "Video 5", "src": "https://www.youtube.com/watch?v=vrRv61GWkCQ"},
                    {"title": "Video 6", "src": "https://www.youtube.com/watch?v=V05YU6RfHCE"},
                    {"title": "Video 7", "src": "https://www.youtube.com/watch?v=2ZGFpy6fEhA"}, 
                       
                    {"title": "Video 8", "src": "https://www.youtube.com/watch?v=jsavm7HvGwc"}, 
                    {"title": "Video 9", "src": "https://www.youtube.com/watch?v=dkSxsSwCeRA"},
                    {"title": "Video 10", "src": "https://www.youtube.com/watch?v=TSKIfUaohZE"},
                    {"title": "Video 11", "src": "https://www.youtube.com/watch?v=Bu8OF-Sc8Cg"} ,
                    {"title": "Video 12", "src": "https://www.youtube.com/watch?v=wQS9cJjDfYU"},
                    {"title": "Video 13", "src": "https://www.youtube.com/watch?v=vwRchLuFruo"},
                    {"title": "Video 14", "src": "https://www.youtube.com/watch?v=b2B4iYuHzuA"},

                   ]

        for video in videos:
            msg = {
                "type": "video",
                "payload": {
                    "title": video["title"],
                    "src": video["src"]
                }
            }
            # time.sleep(5)

            dispatcher.utter_message(text="Check this video", attachment=msg)

        return []
        
        
        

        
        # return []
# class ActionDetectLanguage(Action):

#     def get_lang(tracker):
#       lang = tracker.slots['language'].title()
#       return lang

#     def get_lang_index(tracker):
#       lang_list = ['English', 'French', 'Arabic', 'Armenian'] # Same as slot values, language is a categorical slot

#       return lang_list.index(get_lang(tracker))

# # dispatcher.utter_message(text = ...)
#     def get_text_from_lang(tracker, utter_list = []):
#        lang_index = get_lang_index(tracker)

#        if not utter_list: # No text was given for any language
#           utter_list.append('[NO TEXT DEFINED]')

#        if lang_index >= len(utter_list): # No text was given for current language
#          lang_index = 0

#        return utter_list[lang_index]

# # dispatcher.utter_message(template = ...)
#     def get_template_from_lang(tracker, template):
#         return template + '_' + get_lang(tracker)

# # dispatcher.utter_message(buttons = ...)
#     def get_buttons_from_lang(tracker, titles = [], payloads = []):
#         lang_index = get_lang_index(tracker)
#         buttons    = []

#         if lang_index >= len(payloads): # No text was given for current language
#            lang_index = 0
    
#         for i in range(min(len(titles[lang_index]), len(payloads))): # Build each button
#             buttons.append({'title': titles[lang_index][i], 'payload': payloads[i]})

#         return buttons
    
#     text = get_text_from_lang( tracker,['Choose a language:','Choisissez une langue:',':اختر لغة','Ընտրեք լեզու ՝'])

#     buttons = [
#     {
#     'title': 'English',  'payload': '/set_language{"language": "English"}'},
#     {
#     'title': 'Français', 'payload': '/set_language{"language": "French"}'},
#     {
#     'title': 'عربي',     'payload': '/set_language{"language": "Arabic"}'},
#     {
#     'title': 'հայերեն',  'payload': '/set_language{"language": "Armenian"}'}]
       
#     dispatcher.utter_message(text = text, buttons = buttons)
    
#     template = get_template_from_lang(tracker, 'utter_ask_service_type')
#     buttons  = get_buttons_from_lang(tracker, [['Wireless', 'Internet', 'DSL Internet', 'CableVision TV'],
#                                                 ['Sans Fil', 'Internet', 'Internet DSL', 'CableVision TV'],
#                                                 ['لاسلكي','إنترنت','DSL إنترنت','تلفزيون الكابل'],
#                                                 ['Անլար', 'Ինտերնետ', 'DSL ինտերնետ', 'CableVision TV']],['/inform_service_type{"service_type": "wireless"}',
#                                                                                                           '/inform_service_type{"service_type": "internet"}',
#                                                                                                           '/inform_service_type{"service_type": "dsl"}',
#                                                                                                           '/inform_service_type{"service_type": "cablevision"}'])

# dispatcher.utter_message(template = template, buttons = buttons)

   

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         text = tracker.latest_message.get("text")

#         langcode = TextBlob(text).detect_language()

#         langname = languages.get(alpha2=langcode).name
#         langname = langname if "(" not in langname else langname.split(" ")[0]

#         return [SlotSet("langcode", langcode), SlotSet("langname", langname)]



###################################################################################################

# from argparse import Action
# from asyncore import dispatcher
# from os import link
# from typing import Text, List, Any, Dict
# from typing_extensions import Self
# from matplotlib.pyplot import text

# from rasa_sdk import Tracker, FormValidationAction
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# class ActionHelloOromia(Action):
#     def name(Self)-> Text:
#         return " Hello Oromia"
# #     def run (self, dispatcher:CollectingDispatcher, 
# #              tracker:Tracker,domaain:Dict[Text, Any])  ->List[Dict[Text, Any]]:
# #              Link= "http:/www.oromiatourismcommission.et/"
# #              dispatcher.utter_responses("utter_location_request", tracker, link= Link)
                      
# #              return[]
# ####################################################################################################
# #                     Strore and Fetch Data from the data base                                      #
# #                                                                                                   #
# #####################################################################################################

# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/
# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List, Union

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import EventType
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction

# from store_data import DataStore, FetchData
# from store_data import FetchData


# class ActionSaveData(Action):

#     def name(self) -> Text:
#         return "action_save_data"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         DataStore(tracker.get_slot("name"), tracker.get_slot("number"), tracker.get_slot("email"),tracker.get_slot("occupation"))
#         dispatcher.utter_message(text="Data Stored Successfully.")

#         return []

# class ActionFetchData(Action):

#     def name(self) -> Text:
#         return "action_fetch_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         output=FetchData(tracker.latest_message['entities'][0]['value'], tracker.latest_message['entities'][1]['value'])
#         dispatcher.utter_message(text="This is the data that you asked for, \n{}".format(",".join(output)))

#         return []

# class FormDataCollect(FormAction):
#     def name(self) -> Text:
#         return "Form_Info"

#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["name","number","email","occupation"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "name":[self.from_text()],
#             "number":[self.from_entity(entity="number")],
#             "email":[self.from_entity(entity="email")],
#             "occupation":[self.from_text()]
#         }

#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:

#         dispatcher.utter_message("Here are the information that you pr. Do you want to save it?\nName: {0},\nMobile Number: {1},\nEmail: {2},\nOccupation: {3}".format(
#             tracker.get_slot("name"),
#             tracker.get_slot("number"),
#             tracker.get_slot("email"),
#             tracker.get_slot("occupation"),

#         ))
#         return []



# ##########################################################################################################
# #This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List, Union

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import EventType
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction

# from excel_data_store_read import DataStore, FetchData


# class ActionSaveData(Action):

#     def name(self) -> Text:
#         return "action_save_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         DataStore(tracker.get_slot("name"),
#             tracker.get_slot("number"),
#             tracker.get_slot("email"),
#             tracker.get_slot("occupation"))
#         dispatcher.utter_message(text="Data Stored Successfully.")

#         return []

# class ActionFetchData(Action):

#     def name(self) -> Text:
#         return "action_fetch_data"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         output=FetchData(tracker.latest_message['entities'][0]['value'],
#                          tracker.latest_message['entities'][1]['value'])
#         dispatcher.utter_message(text="This is the data that you asked for, \n{}".format(",".join(output)))

#         return []

# class FormDataCollect(FormAction):
#     def name(self) -> Text:
#         return "Form_Info"

#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["name","number","email","occupation"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "name":[self.from_text()],
#             "number":[self.from_entity(entity="number")],
#             "email":[self.from_entity(entity="email")],
#             "occupation":[self.from_text()]
#         }

#     def submit(
#         self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any],) -> List[EventType]:

#         dispatcher.utter_message("Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1},\nEmail: {2},\nOccupation: {3}".format(
#             tracker.get_slot("name"), tracker.get_slot("number"), tracker.get_slot("email"), tracker.get_slot("occupation"),

#         ))
#         return []


######################################################################################################
######################################################################################################



class ActionFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm sorry, Can you please rephrase or provide more information? \n my Default language is English and others are under maintain.")
        return []