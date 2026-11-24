class Animal:
    def __init__(self, name ):
        self.name = name

    def make_sound(self):
        print('Generic animal sound')

    def display_name(self):
        print(f'My name is {self.name}')


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof! Woof!")

    def display_breed(self):
        print(f"My bread is {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color 

    def make_sound(self):
        print("Meow! Meow!")

    def display_color(self):
        print(f"My color is {self.color}")


if __name__ == '__main__':
    my_animal = Animal('Critter')
    my_animal.make_sound()
    my_animal.display_name()

    my_dog = Dog('Buddy', 'Golden Retriever')
    my_dog.make_sound()
    my_dog.display_name()
    my_dog.display_breed()

    my_cat = Cat('Whiskers', 'Gray')
    my_cat.make_sound()
    my_cat.display_name()
    my_cat.display_color ()