#opening the file

test_file = open("test.txt", "r")

#reading cont
read_file = test_file.read()
print(read_file)

#Closing files
test_file.close()

#Writing to the text file

with open("test.txt", "w") as test_file2:
    
    #Write to the text file
    test_file2.write("This is me again I am ubri ")
    test_file2.write("This is Stepa and not Ubri") 
    
 
test_file2 = open("test.txt", "r")
read_file = test_file2.read()
print(read_file)
  