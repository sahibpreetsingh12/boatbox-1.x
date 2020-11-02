# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRepairHull(Action):

    def name(self) -> Text:
        return "action_repair_hull"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        part= tracker.get_slot("boat_part")

        if part=='hull':

            dispatcher.utter_message(text="We can repair your %s pls tell me something more about it"%(part))
        elif part=='core':
            dispatcher.utter_message(text="Core damage needs a professional help")

        return []
