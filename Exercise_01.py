
#takes in a string and then outputs a copy of the string but backwards
def reverse_String(a : str) -> str:

    i = len(a)
    out = ''

    while i > 0:
        out += a[i-1]
        i-=1

    return out

#gets a user inputted string
while True:
    try:

        string : str = input("\nEnter a String: ")

        #Throws an error if the user input is just a space
        if string.isspace():
            raise ValueError

        break
    except ValueError:         
        print("That is an invalid input, please enter a string: ")

print("Reversed String: " + reverse_String(string), end='\n\n')
