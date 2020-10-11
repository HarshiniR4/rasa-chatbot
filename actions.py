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
from rasa_sdk.events import SlotSet


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
            with open('cond_dat.json','r', encoding ='utf-8') as file:
                data=json.load(file)
            message="User not found!"
            name=None
            entity=tracker.latest_message["entities"]
            for e in entity:
                if e['entity']=="username":
                    name=e['value']
                    
            follower=0
            message="Name not found!"
            for i in data:
                if(i['username']==name):
                    follower=i["followers_count"]    

                        
            message= "The number of followers of {} is {}".format(name, follower)
            dispatcher.utter_message(message)
            return [] 
        
class ActionRespondRetweet(Action):
        def name(self) -> Text:
            return "action_retweet_req"

        def run(self, dispatcher, tracker, domain):
            with open('cond_dat.json','r', encoding ='utf-8') as file:
                data=json.load(file)
            message="User not found!"
            name=None
            entity=tracker.latest_message["entities"]
            for e in entity:
                if e['entity']=="username":
                    name=e['value']
                    
            retweet=0
            message="Name not found!"
            for i in data:
                if(i['username']==name):
                    retweet=i["retweet_count"]    

                        
            message= "The number of retweets of {}'s tweet is {}".format(name, retweet)
            dispatcher.utter_message(message)
            return [] 
        
        
class ActionAccInfo(Action):
        def name(self) -> Text:
            return "action_info_req"

        def run(self, dispatcher, tracker, domain):
            with open('cond_dat.json','r', encoding ='utf-8') as file:
                data=json.load(file)
            message="User not found!"
            name=None
            entity=tracker.latest_message["entities"]
            for e in entity:
                if e['entity']=="username":
                    name=e['value']
                    
            time=None
            message="Name not found!"
            for i in data:
                if(i['username']==name):
                    time=i["user_created_at"]    
                    
            message= "The user {} created account on {}".format(name, time)
            dispatcher.utter_message(message)
            return [] 
        
class ActionTweetSource(Action):
        def name(self) -> Text:
            return "action_tweet_source"

        def run(self, dispatcher, tracker, domain):
            with open('cond_dat.json','r', encoding ='utf-8') as file:
                data=json.load(file)
            message="User not found!"
            name=None
            entity=tracker.latest_message["entities"]
            for e in entity:
                if e['entity']=="username":
                    name=e['value']
                    
            source=None
            message="Name not found!"
            for i in data:
                if(i['username']==name):
                    source=i["tweet_source"]    
                    
            message= "The user {}'s tweet source is {}".format(name, source)
            dispatcher.utter_message(message)
            return [] 