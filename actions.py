# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import pandas as pd
from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa_core.events import SlotSet

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
class ActionRespondFollower(Action):
        def name(self) -> Text:
            return "action_followers_req"

        def run(self, dispatcher, tracker, domain):
            with open('D:/Dataset/Tweets #IndiaFightsCorona.json','r', encoding ='utf-8') as file:
                data=json.load(file)
            name=tracker.last_message('username')
            for i in data:
                if(i.get('name')=='Akanksha vaidya'):
                    print(i.get('followers_count'))
           
            # message= 'The followers of '+ name+ ' are ' + follower
            dispatcher.utter_message(text=name)
            return [] 