from sys import exit
from GameAction import GameAction
from Death import Death
from Outcome import Outcome

class Game(object):

    def __init__(self, rooms, actions, guards, flags):
        self.inventory = []
        self.flags = flags
        self.rooms = rooms
        self.actions = actions
        self.current_room = None
        self.guards = guards

    def play(self, room_name):
        self.current_room = self.rooms[room_name]

        while self.current_room.name != "Death":
            outcomes = self.current_room.enter(self)
            print(len(outcomes))
            for item in outcomes:
                outcome = Outcome(item)
                current_action = self.actions[outcome.type]
                current_action.do(self, outcome)
                

            #current_action = self.actions[outcome.type]
            #current_action.do(self, outcome)
                       
            #print(current_room.name)
            #exit()
            
        self.current_room.enter(self)
            
