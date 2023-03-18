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
    
        
    
