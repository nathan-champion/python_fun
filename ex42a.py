class Person:

    def __init__(self, name):
        print("I'm a person")
        self.name = name
        

class Mom(Person):

    def __init__(self, name):
        super().__init__(name)
        print("I'm a mom.")
        

class Cousin(Person):

    def __init__(self, name):
        super().__init__(name)
        print("I'm a cousin")
        

class Debbie(Mom, Cousin):
    
    def __init__(self, name):
        super().__init__(name)
        print(f"I'm Debbie.  My name is {self.name}")
        


debbie = Debbie("Goomba")