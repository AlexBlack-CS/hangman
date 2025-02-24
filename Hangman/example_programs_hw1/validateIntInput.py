"""
    File:  validateIntInput.py
    Description:  Simple program to demonstrate try-except to validate
    an integer input from the user.   
"""

def main():
    """ Repeat prompting until user enters a valid positive integer. """
    
    while True:
        validInteger = getValidInteger("Enter a positive integer: ")
        if validInteger > 0:
            print("Great you entered a valid positive integer", validInteger)
            break
        else:
            print("Sorry, your integer must be positive!")
    


def getValidInteger(promptString):
    """ Repeat prompting until user enters a valid integer. """
    
    while True:
        try:  # tries to convert input string to an int, but if it fails
              # do "except" code; otherwise break out of the loop
            number = int(input(promptString))
            break  # only gets here if the conversion to an int was successful
        except:
            print("Invalid integer! Please retry.")
    return number

main()
