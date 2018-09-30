#myList = [1, 2, 3, 4, 5]
#for i in myList:
#    print(i)

# myList = [1, 2, 3, 4, 5]
# for i in myList:
#     if i > 2:
#         print(i)

# myfile = open("fruits.txt")
# content = myfile.read()
# content = content.splitlines()
# myfile.close()
# for item in content:
#     print(len(item))

temperatures = [10, -20, 100]

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

for temp in temperatures:
    print(cel_to_fahr(temp))
