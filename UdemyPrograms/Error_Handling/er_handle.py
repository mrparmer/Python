#def string_length(mystring="hello"):
#    return len(mystring)
#if type(mystring) =! str:
#    print (len(mystring))
#else:
#    print("Sorry, integers don't have length")

# Code above this line is broken, working on finding fix

def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)
