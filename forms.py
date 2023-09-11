# my_chatbot/forms.py

from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List, Union
from rasa_sdk.executor import CollectingDispatcher

class FeedbackForm(FormAction):
    def name(self) -> Text:
        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["first_name", "last_name", "email", "feedbackText"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "first_name": [self.from_text()],
            "last_name": [self.from_text()],
            "email": [self.from_text()],
            "feedbackText": [self.from_text()],
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        # Assuming you have a Spring Boot API endpoint to send the feedback
        api_endpoint = "http://localhost:9000/feedback/giveFeedback"
        feedback_data = {
            "first_name": tracker.get_slot("first_name"),
            "last_name": tracker.get_slot("last_name"),
            "email": tracker.get_slot("email"),
            "feedbackText": tracker.get_slot("feedbackText"),
        }

        # Code to send feedback_data to the Spring Boot API using requests library
        import requests
        response = requests.post(api_endpoint, json=feedback_data)

        # Handle the API response and send a message to the user
        if response.status_code == 200:
            dispatcher.utter_message("Thank you for your feedback!")
        else:
            dispatcher.utter_message("Failed to submit feedback. Please try again later.")

        return []
