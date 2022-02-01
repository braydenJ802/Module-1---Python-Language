import time
import threading
import random

class AnimalRaceManager (threading.Thread):
    """This is a class which represents a fictional race between a group of animals. 
    Every animal's positon in the race is represented by a thread object, and order of execution is determined by the speed of the animals."""
    
    def __init__(self, position, animal_type):
        """Initializes our AnimalRaceManager class."""
        threading.Thread.__init__(self)
        
        self.position = position
        self.animal_type = animal_type
  
        
    def run(self):
        """Runs our program. Executes threads."""
        execute_threads(self.animal_type, self.position, len([cls for cls in Animal.__subclasses__()]))
        print(f"Id: {self.position}, {self.animal_type} has finished the race!")




class Animal():
    """This class represents real-world animals who all have varying speeds. The individual speed of each animal has a chance of
    being lower.
    This is a parent class of a subset of animal classes. """

    #Initialize our animal
    def __init__(self, animal_type, speed=None, three_limbed=False):
        """Our parent class __init__(). Initializes our Animal Class."""
        self.speed = speed
        self.animal_type = animal_type
        self.three_limbed = three_limbed

class Dog(Animal):
    """This class represents a dog."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Dog class."""
        d = random.randrange(1, 50, 1) # 1/ 50 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 2
        else:
            speed = 4
        super().__init__("Dog", speed, three_limbed)

class Cat(Animal):
    """This class represents a cat."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Cat class."""
        d = random.randrange(1, 50, 1) # 1/ 50 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 2
        else:
            speed = 6
        super().__init__("Cat", speed, three_limbed)

class Fox(Animal):
    """This class represents a fox."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Fox class."""
        d = random.randrange(1, 100, 1) # 1/ 100 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 6
        else:
            speed = 9
        super().__init__("Fox", speed, three_limbed)

class Turtle(Animal):
    """This class represents a turtle."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Turtle class."""
        d = random.randrange(1, 1000, 1) # 1/ 1000 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 1.5
        else:
            speed = 2
        super().__init__("Turtle", speed, three_limbed)

class Bunny(Animal):
    """This class represents a bunny."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Bunny class."""
        d = random.randrange(1, 125, 1) # 1/ 125 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 4
        else:
            speed = 7
        super().__init__("Bunny", speed, three_limbed)

class Antelope(Animal):
    """This class represents an antelope."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Antelope class."""
        d = random.randrange(1, 200, 1) # 1/ 200 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 5
        else:
            speed = 12
        super().__init__("Antelope", speed, three_limbed)
    
class Cheetah(Animal):
    """This class represents a cheetah."""
    def __init__(self, speed=None, three_limbed=False):
        """Initializes our Cheetah class."""
        d = random.randrange(1, 450, 1) # 1/ 450 chance of being three_limbed
        if d == 13:
            three_limbed = True
            speed = 13
        else:
            speed = 18
        super().__init__("Cheetah", speed, three_limbed)




def execute_threads(animal_type, wait, i):
    
    while i:
        time.sleep(wait)
        print(f"\n {animal_type} is running! ")
        i -= 1


    
    