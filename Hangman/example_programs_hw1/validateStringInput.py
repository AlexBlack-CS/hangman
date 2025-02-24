"""
    File:  validateStringInput.py
    Description:  Simple program to demonstrate how to validate
    user-input string is one of a set of strings.   
"""

def main():
    validStringList = ['a', 'b', 'c']
    validString = getValidString(validStringList)

def getValidString(validStringList):
    userInput = input("Please enter string from " + str(validStringList) + ": ").lower()
    while userInput not in validStringList:
        userInput = input("Invalid entry only enter from " + str(validStringList) + ": ").lower()

    print("The valid entry was '%s'" % (userInput))


main()
