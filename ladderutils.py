class Animal: 
    def __init__(self, eyes, hands=0, legs=0, wings=0, can_fly=False):
        self.eyes = eyes
        self.hands = hands
        self.legs = legs        
        self.wings = wings
        self.can_fly = can_fly
    
    def __str__(self):
        return (f"{self.__class__.__name__} <eyes: {self.eyes}, legs: {self.legs}"
            + (f", hands: {self.hands}" if self.hands else "")
            + (f", wings: {self.wings}" if self.wings else "")
            + (f", fly: {self.can_fly}" if self.can_fly else "") + ">")

    def fly(self):
        if self.can_fly:
            return True
        return False
    
    def walk(self):
        if self.legs > 2:
            return f"{self.__class__.__name__} can walk"
        return f"{self.__class__.__name__} cannot walk easily"

class Monkey(Animal):
    def __init__(self):
        super().__init__(eyes = 2, legs = 2, hands = 2)

class Squirrel(Animal):
    def __init__(self):        
        super().__init__(eyes = 2, legs = 4)
        
class Pigeon(Animal):
    def __init__(self):
        super().__init__(eyes = 2, legs = 2, wings = 2, can_fly = True)
        

class Eagle(Animal):
    def __init__(self):
        super().__init__(eyes = 2, legs = 2, wings = 2, can_fly = True)


class Ladder: 
    def __init__(self):
        self.ladder = {}
        
        self.ladder[3] = Monkey()
        self.ladder[5] = Squirrel()
        self.ladder[8] = Pigeon()
        self.ladder[15] = Eagle()
        self.ladder[17] = Monkey()
        
    
    def animal_at_rung(self, rung_number):
        return self.ladder.get(rung_number, None)
        
    
    def get_animal_count(self):
        return len(self.ladder)
    
    def hop(self, rung_number):
        if rung_number in self.ladder:
            animal = self.ladder.pop(rung_number)
            
            self.ladder[rung_number + 1] = animal
            return animal
        return None
    
    def __str__(self):
        ladder_representation = []
        
        for rung, animal in sorted(self.ladder.items()):
            ladder_representation.append(f"Rung {rung}: {animal}")
            
        return "\n".join(ladder_representation)
    
ladder = Ladder()
print(ladder)

ladder.hop(5)
print("\nAfter hopping:")
print(ladder)

print("\nAnimal count:", ladder.get_animal_count())
print("\nAnimal at rung 5:", ladder.animal_at_rung(5))

    
# if __name__ == "__main__":
            
#         monkey1 = Monkey()
#         squirrel1 = Squirrel()
#         pigeon = Pigeon()
#         eagle = Eagle()
#         monkey2 = Monkey()
        
#         ladder = Ladder()               
        
#         ladder.add_animal(3, monkey1)
#         ladder.add_animal(5, squirrel1)
#         ladder.add_animal(8, pigeon)
#         ladder.add_animal(15, eagle)
#         ladder.add_animal(17, monkey2)
        
#         print(ladder)
        
#         animal_at_rung_8 = ladder.get_animal_at_rung(8)
        
#         if animal_at_rung_8:
#             print(f"Animal at rung 8: {animal_at_rung_8}")
#         else:
#             print("No animal at rung 8")


