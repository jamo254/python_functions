# Tuples in Python
# name = ()

first_tuple = (2, 4, 8, 10)
print(first_tuple)

# Mixed datatypes
second_tuple = ("Ubri", 34, 56, "Russia.me")
print(second_tuple)

#create nested tuples
nested_tuples  = ("Ubri", [123, 45,66], ("Me", "not you"))
print(nested_tuples)

# Accessing tuple items
access = nested_tuples[1]
print(access)

access_negative = nested_tuples[-1]
print(access_negative)

#Print out index 2

#Learn how to slice tuples

#Learn Tuple methods

print("#############")
#Iterating thought tuples
programming_languages = ("Python", "C++", "Java", "Dart")

for language in programming_languages:
    if language == "Python":
        print("I am learn ", language)
    else:
        print(language)
        
print("###############")    
#Checking whether an item exists
print("C++" in programming_languages)
# Check whether Python exists in the tuple

#What are the advantages of Tuples over Lists in Python