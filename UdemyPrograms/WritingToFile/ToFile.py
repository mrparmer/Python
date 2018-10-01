# Writing to
# myfile = open("employees.txt", "w")
# myfile.write("Mike, John, Marshall")
# myfile.close()

# Appending to
# myfile = open("employees.txt", "a")
# myfile.write("\nMatt\nLeigh\nElizabeth")
# myfile.close()

#Reading and Appending
# myfile = open("employees2.txt", "a+") #a+ is append but also allows reading the file.
# myfile.seek(0)#to reset cursor position to the top of the file.
# myfile.read() #reads file contents amd moves the cursor back to the end of the file
# myfile.write("\nCharles")
# myfile.close()

#Writing list to file with conversion.
numbers = [1, 2, 3]
file = open("numbers.txt", "w") #Creates file, flags as writable
for i in numbers: #loop that iterates through the list
    file.write(str(i) + "\n") #writes i as string with a new line after each entry
file.close()
