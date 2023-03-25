# Introduction to python classes
#Create class student

class Student:
    #These are are attributes
    name = "Ubri"
    age = 14
    hobby = ""

#How to use the class

#First object
stud_1 = Student()
print("Your name is = ", stud_1.name)

print("Your age is = ", stud_1.age)

#Define Hobby
stud_1.hobby = "Programming NFTS"
print("My hobby is ", stud_1.hobby)

#Another way of displaying output
print(f"Name: {stud_1.name}, age: {stud_1.age}")


#Second object
stud_2 = Student()
stud_2.age = 23
print(stud_2.age)


class Employee:
    name = ""
    age = 25
    salary = 100000
    years_of_work = 5
    
    #Creating functions
    def calculate_salary(self):
        if self.years_of_work < 5:
            return self.salary - 3000
        return self.salary
    
#Create object
empl_1 = Employee()

empl_1.name = "Ubri Hacker"
print(empl_1.name)

empl_1.years_of_work = 3
print(f"Your salary is: ${empl_1.calculate_salary()}")

#Homework Create a class Car, include all the attributes

class Car:
    #Define attributes of the car - colour, price, milage, 
    # amount_of_fuel, number_plate, year
    # function calculate the price of the car based on milage
    # calculate the amount of fuel used per hour
    brand = ""
    color = ""
    price = 1000000
    milage = 200000
    number_plate = "ru23x"
    year = 2020
    fuel_usage = 0
    distance = 0
    
    def calculate_price(self):
        if self.milage < 10000:
            return self.price + 50000
        return self.price
    
    def calculate_fuel_used(self):
        fuel_used = self.distance / self.fuel_usage
        return fuel_used
    
    # Write a function that prints out the color of the car
    def car_color(self):
        return self.color
    
    # Write a function that returns  the price of the car
    

# Create a new object

car1 = Car()
car1.price = 100000

# Fuel used
car1.distance = 1000
car1.fuel_usage = 20
car1.color = "Blue"

print("The car color is:", car1.car_color())


print("Price of fuel ", car1.calculate_fuel_used())
print("Car price ",car1.calculate_price())
        
    
    
    
        
    
