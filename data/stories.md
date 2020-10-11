## happy path
* greet
  - utter_greet
  
## info_actions
* followers
  - action_followers_req
* retweets
 - action_retweet_req
 
## user_info
* days_info
  - action_info_req
  
## tweet_source
* tweet_source
  - action_tweet_source
## did_help 
* mood_great
  - utter_did_that_help
* affirm
  - utter_happy
* deny
  - utter_goodbye
  
## sad path 1
* mood_great
  - utter_did_that_help
* affirm
  - utter_happy
*affirm
  - utter_ask

## sad path 2
* greet
  - utter_greet
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye



