from sys import argv
from ExamineAction import ExamineAction
from ChangeDescriptionAction import ChangeDescriptionAction
from FlagAddAction import FlagAddAction
from FlagRemoveAction import FlagRemoveAction
from FlagGuard import FlagGuard
from Guard import Guard
from InventoryAddAction import InventoryAddAction
from RemoveChoiceAction import RemoveChoiceAction
from Room import Room
from Game import Game
from Death import Death
from GoAction import GoAction
from DieAction import DieAction

file = open("rooms.txt")

num_rooms = int(file.readline())
rooms = dict()

for i in range(0, num_rooms):
    added_room = Room()
    added_room.read_from_open_file(file)
    rooms[added_room.name] = added_room

actions = dict()
actions["Go"] = GoAction()
actions["Death"] = DieAction()
actions["Examine"] = ExamineAction()
actions["Remove_Choice"] = RemoveChoiceAction()
actions["Inventory_Add"] = InventoryAddAction()
actions["Flag_Add"] = FlagAddAction()
actions["Change_Description"] = ChangeDescriptionAction()
actions["Flag_Remove"] = FlagRemoveAction()

guards = dict()
guards["Flag"] = FlagGuard()
guards["None"] = Guard()

flags = []
flags.append("Salt_Circle_Whole")
 
game = Game(rooms, actions, guards, flags)
game.play("Dungeon_Entrance")
#game.play("Crystal_Cave")