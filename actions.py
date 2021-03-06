# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRepair(Action):

    def name(self) -> Text:
        return "action_repair"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        part= tracker.get_slot("boat_part")

        if part=='hull':

            dispatcher.utter_message(text="""There are two scenarios where a %s can be damaged – one is when the
      hull is damaged above the waterline, the second when it is damaged below the
      waterline.For first scenario take it out and dry it thoroughly.For hull repair,
      a basic fibreglass repair kit is used, using which the damaged section is removed
      in a circular cut. The part can be then patched using either fibreglass and
      the proper adhesives or the putties available."""%(part))
        elif part=='core':
            dispatcher.utter_message(text="""%s damage needs a professional help I would say pls visit a boat 
            repair shop near you"""%(part))

        return []
