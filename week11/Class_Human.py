class Head:
    def __init__(self, eyes=2, nose=1, mouth=1):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth 
    
    def look (self,direction):
        return f'The head is looking towards {direction}.'
    
    def speak (self, words):
        return f'The mouth says:"{words}".'
    
class Hand:
    def __init__(self, fingers=5):
        self.fingers = fingers

    def grab(self, item):
        return f'The  hands grabs "{item}".'

class Arm :
    def __init__(self, hand):
        self.hand = hand

    def flex (self):
        return 'The arm flexes.'
        
class Feet:
    def __init__(self,toes=5):
        self.toes = toes

    def step(self):
        return 'The foot takes a step.'

class Leg: 
    def __init__(self, feet):
        self.feet = feet 

    def walk (self, direction):    
        return f'The leg walks towards {direction}.'
    
class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.vital_organs = ['"heart", "lungs", "stomach", "liver"']

    def breathe(self):
        return"The torso inhales ans exhales."
    
class Human:
    def __init__ (self, name):
        self.name = name 
        self.head = Head()
        self.left_hand = Hand()
        self.right_hand = Hand()
        self.left_arm = Arm(self.left_hand)
        self.right_arm = Arm(self.right_hand)
        self.left_feet = Feet()
        self.right_feet = Feet()
        self.left_leg = Leg(self.left_feet)
        self.right_leg = Leg(self.right_feet)
        self.torso = Torso(self.head, self.left_arm, self.right_arm,self.left_leg, self.right_leg )

    def greet (self, other_human):
        return f'{self.name} greets {other_human.name}.'
    
    def walk(self,direction):
        return f'{self.name} walks towards {direction} using their right hand.'
    
    def grab_item (self, item,hand="right"):
        if hand.lower() == "right":
            return f'{self.name} grabs "{item}" with their right hand.'
        elif hand.lower() == "left":
            return f'{self.name} grabs "{item}" with their left hand.'
        else:
            return "Please specify 'right' or 'left for the hand."
        
        
if __name__ == '__main__':

    person1 = Human('Alice')
    person2 = Human ('Bob')


    print(person1.torso.head.look ('The horizon'))
    print(person1.torso.left_arm.hand.grab ('a flower'))
    print(person2.torso.right_leg.feet.step())
    print(person1.greet(person2))
    print(person2.walk ('the north'))
    print(person1.grab_item ('a ball'))
    print(person2.torso.breathe())