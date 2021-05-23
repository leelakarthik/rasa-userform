
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction,Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import re


class ValidateUserForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_form"
    
    # def required_slots(tracker:Tracker) -> List[Text]:
    #     return ["name","fname","age","phonenumber", "email"]

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate name value."""
        # print(f"name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            if "my name is " in slot_value:
                slot_value = slot_value[11:]
            elif "my father name is " in slot_value:
                slot_value = slot_value[18:]    
            return {"name": slot_value}
    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `age` value."""
        # print(f"age given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) >=3:
            dispatcher.utter_message(text=f"Iam so happy to talk to a centurian!!, I'm assuming you mis-spelled.")
            return {"age": None}
        else:
            return {"age": slot_value}
    def validate_phonenumber(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phonenumber` value."""

        # print(f"phonenumber given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) == 10 :
            dispatcher.utter_message(text=f"thanks for valid mobile number!!")
            return {"phonenumber": slot_value}
        else:
            dispatcher.utter_message(text=f"Hmm, that doesn't look like a number. I'm assuming you mis-spelled.")
            return {"phonenumber": None}
      
    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex,slot_value)):
            # print(f"email given = {slot_value} length = {len(slot_value)}")
            dispatcher.utter_message(text=f"thanks for valid email address.")
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"I'm assuming you mis-spelled.")
            return {"email": None}
     
    def validate_fname(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `fname` value."""
        # print(f"father name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"fname": None}
        else:
            return {"fname": slot_value}
class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        name = tracker.get_slot("name")
        fname = tracker.get_slot("fname")
        age = tracker.get_slot("age")
        phonenumber = tracker.get_slot("phonenumber")
        email = tracker.get_slot("email")
        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []
