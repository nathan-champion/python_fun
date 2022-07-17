from posixpath import split
from sys import exit

class Choice(object):

    def __init__(self, choices):
        self.choices = choices

    def get_input(self, num_choices):
        choiceInt = -1
        while choiceInt < 1 or choiceInt > num_choices:
            choice = input("> ").strip()
            try:
                choiceInt = int(choice)
            except:
                print("Choice was: ", choice)
                if choice == 'q':
                    exit()
                else:
                    print("We didn't recognize that input.")

        return choiceInt
        
      
    def present(self, game):
        num_choices = 0
        guard = None
        guard_key = ""
        guard_value = ""
        back_choices = dict()
        for i in range(0, len(self.choices)):
            choice_text, guard_text = self.choices[i].split(';')
            if guard_text != "None":
                guard_key, guard_value = guard_text.split(':')
                try:
                    guard = game.guards[guard_key]
                except:
                    print(f"No guard specified for {guard_key}")
            else:
                guard = game.guards["None"]

            if guard.allowed(guard_value, game):
                print(f"{num_choices + 1}. {choice_text}")
                num_choices += 1
                back_choices[num_choices] = i

        

        choice = self.get_input(num_choices)
        print("Real choice:", back_choices[choice])

        return back_choices[choice]
