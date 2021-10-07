# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet,  EventType
from rasa_sdk.executor import CollectingDispatcher

from smtplib import SMTP
import requests
import json, os

# def name_cap(text):
#     tarr = text.split()
#     for idx in range(len(tarr)):
#         tarr[idx] = tarr[idx].capitalize()
#     return ' '.join(tarr)

# class action_save_cust_info(Action):
#     def name(self):
#         return 'action_save_cust_info'

#     def run(self, dispatcher, tracker, domain):
#         user_id = (tracker.current_state())["sender_id"]
#         print(user_id)
#         cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
#         cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
#         bot_position = "Mình"

#         if (cust_sex is  None):
#             cust_sex = "Bạn"

#         if (cust_sex == "anh") | (cust_sex == "chị"):
#            bot_position = "em"
#         elif (cust_sex == "cô") | (cust_sex == "chú"):
#             bot_position = "cháu"
#         else:
#             cust_sex = "Bạn"
#             bot_position = "Mình"

#         if not cust_name:
#             dispatcher.utter_template("utter_greet_with_name",tracker)
#             return []

#         print (name_cap(cust_name))
#         return [SlotSet('cust_name', " "+name_cap(cust_name)),SlotSet('cust_sex', name_cap(cust_sex)),SlotSet('bot_position', name_cap(bot_position))]

# class action_reset_slot(Action):

#     def name(self):
#         return "action_reset_slot"

#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("transfer_nick", None),SlotSet("transfer_amount", None),SlotSet("transfer_amount_unit", None)]

class GetName(Action):
	def name(self):
		return 'action_name'
		
	def run(
		self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
		
	)-> List[EventType]:
		import requests
		# fb_access_token = ("EAAGYniiVkQMBACacedTZCTM24m0UvTkqpJ30idc0e36AatOoCuYdo8UTxTQDglDNYwuNOVXYxFZBCPelLU70AnUKqPbk8ZCSxSs0yJ1VPApLjJRCzVZCU3fuwbgqzyD1SZB7ZBWVhwZCJH4JhUrk1zFrC0fvSQcfnxrRNV3OWlgrvVeYew3ZBzK4T9jV9g2GXUkZD")
		fb_access_token = ("EAALpq0lPXikBAJiPClUSEKHf3RQT7cKw2xKdsN9al78Blrdn812enytGEwKuZACAiJK4TN6mQkC6ZA2K1F2GSfLuZATcDrbBEZA99JImvJrFnCtdUjzy78Vc6DWwYMpSPdgQuNopmA4ZB7MgMwmX4dSw1M0ycHalsnmq3qkLMB7eVCFXacQiz")
		
		most_recent_state = tracker.current_state()
		sender_id = most_recent_state['sender_id']
		
		r = requests.get('https://graph.facebook.com/{}?fields=first_name,last_name&access_token={}'.format(sender_id, fb_access_token)).json()
		first_name = r["first_name"]
		last_name = r["last_name"]
		
		dispatcher.utter_message("Chào {} {} nhé, mình có thể giúp gì được cho bạn?' ".format(first_name, last_name))
		# return [SlotSet('name', first_name), SlotSet('surname', last_name)]
