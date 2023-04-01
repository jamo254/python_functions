# Constructors

class Plane:

    def __init__(self):
        self.color = "White"
        self.price = 1000000

        self.distance()

    def distance(self):
        print("Distance")

plane1 = Plane()
print(plane1.distance())


class Person:
  
    def __init__(self, name, sex, profession, nationality):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession
        self.nationality = nationality

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex,
              'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)
    
    def country(self):
        return self.nationality
    
person = Person("Ubri", "Male", "Hacker", "Russian")
print(person.name)
print("Nationality: ", person.country())

