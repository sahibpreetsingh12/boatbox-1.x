## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye
* thankyou
  - utter_thankyou


## say goodbye
* goodbye
  - utter_goodbye
* thankyou
  - utter_thankyou

## ask repair_hull
* greet
    - utter_greet
* repair_hull
    - action_repair_hull
    - utter_did_that_help
* no_repair_required
    - utter_no_repair_required
* affirm
    - utter_happy
* thankyou
    - utter_thankyou




## ask repair_core
* greet
    - utter_greet
* repair_core
    - utter_repair_core
    - utter_did_that_help
* no_repair_required
    - utter_no_repair_required
* affirm
    - utter_happy
* thankyou
    - utter_thankyou

## ask out_of_scope
* out_of_scope
  - utter_out_of_scope
* thankyou
  - utter_thankyou


## ask cleaning_boat

* cleaning_boat
  - utter_cleaning_boat
  - utter_did_that_help
* no_repair_required
  - utter_no_repair_required
* thankyou
  - utter_thankyou


## interactive_story_1
* greet
    - utter_greet
* cleaning_boat{"boat_manufacturer": "mako"}
    - utter_cleaning_boat
    - utter_did_that_help
* cleaning_boat{"boat_manufacturer": "robalo"}
    - utter_cleaning_boat
    - utter_did_that_help
* thankyou
  - utter_thankyou

## no_repair_story
* greet
    - utter_greet
* repair_hull{"boat_part": "hull"}
    - action_repair_hull
    - utter_did_that_help
* no_repair_required
    - utter_no_repair_required
* thankyou
    - utter_thankyou
* goodbye
    - utter_goodbye
