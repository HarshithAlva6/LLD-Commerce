from abc import ABC
from Design.State import NewState, PaidState

class StateFactory(ABC): #"Factory" Design Pattern Used
    @staticmethod
    def get_state(label):
        states = {
            "NEW": NewState(),
            "PAID": PaidState()
        }
        return states.get(label.upper(), NewState())