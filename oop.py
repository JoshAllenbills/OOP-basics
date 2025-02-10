import random

class Character:
    hair_colors = ["blonde","brunette","black","ginger","white"]
    sizes = ["tiny","medium","large"]
    special_powers = ["Flying","Invisibilty","super strength,"]


    #Constructor
    def __init__(self): 
        self.generate_character()

    def generate_character(self):
        self.hair_color = random.choice(Character.hair_colors)
        self.size = random.choice(Character.sizes)
        self.special_power = random.choice(Character.special_powers)
        self.description = (
            f"Your character has {self.hair-color} hair, "
            f"is {self.size} in size,and has the power of {self.special_power}"
        )

    def __str__(self):
        return self.description

    
char1 = Character()
char2 = Character()

print (char1)
print (char2)