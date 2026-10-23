class Person:
    def __init__(self,name):
        self.name = name

class Bus:
    def __init__(self, max_passengers ):
        self.max_passengers= max_passengers
        self.passengers =[]


    def add_passenger(self, person):
        if len (self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} has boarded a bus.')
        else:
            print('The bus is full. No more passengers can be added. ')    

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person.name} has left the bus.')
        else:
            print(f'{person.name} is not on the bus ')


if __name__ == "__main__":

    bus1 = Bus(3)


    person1 = Person("Maria")
    person2 = Person("Juan")
    person3 = Person("Ana")
    person4 = Person("Carlos")
    person5 = Person("Maria Jose")


bus1.add_passenger(person1)
bus1.add_passenger(person2)
bus1.add_passenger(person3)
bus1.add_passenger(person4)
bus1.add_passenger(person5)


bus1.remove_passenger(person2)
bus1.remove_passenger(person3)

bus1.add_passenger(person5)
bus1.add_passenger(person4)


bus1.remove_passenger(Person("Eve"))


print(f'Current passengers on the bus: {[p.name for p in bus1.passengers]}')
