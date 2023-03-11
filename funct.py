# # Finding sum of list number

def sum(numbers):
    total = 0
    
    for num in numbers:
        # total = total + num
        total += num
    return total

print("The sum: ", sum([8, 2, 3, 0, 7]))

#Findind the multiples
def multiples(numbers):
    total = 1
    
    for numb in numbers:
        total = total * numb
#     return total

# print("The multiples: ", multiples([1, 2,5,5]))

# Write a Python function to find the maximum of three numbers
# 1, 5, 6
#For two numbers
def max_two_numbers(x, y):
    
    if x > y:
        return x
    
    return y
print("This is the max number: ", max_two_numbers(5,7))

def max_three_numbers(x, y, z):
    return max_two_numbers(x, max_two_numbers(y,z)) 

print(max_three_numbers(3, 6, -10))


