
#Function for taking a string and sorting it in the order of the lower case, upper case, and other characters
def string_to_lowerUpper(a : str) -> str:
    lower = []
    upper = []
    other = []
    final : str = ""

    # For every character in the string
    for x in a:

        if x.islower():
            lower.append(x)

        elif x.isupper():
            upper.append(x)

        elif not x.isspace():
            other.append(x)
        #Anything else is a space

    #Adding in the characters in the order, lower case, upper case, and any other character
    for y in lower:
        final += y

    for w in upper:
        final += w
    
    for z in other:
        final += z

    return final

#
#Program Start
#

#Getting user input
while True:
    try:

        s = input("\nPlease input a string: ")

        #Throwing an error if the input is just a space
        if s.isspace():
            raise ValueError
        
        break

    except ValueError:
        print("That value is invalid, please input in a correct value")


print("lower cases first, upper next, then numbers and special characters: " + string_to_lowerUpper(s), end='\n\n')
