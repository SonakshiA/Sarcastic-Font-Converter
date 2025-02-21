import random

def convertAlternateCharacters(inputString:str):
    """
    This function converts every alternate character in a string to uppercase and the remaining characters to lowercase.
    """
    outputString = ""
    for i in range(len(inputString)):
        if i % 2 == 0:
            outputString += inputString[i].lower()
        else:
            outputString += inputString[i].upper()
    return outputString

def convertRandomCharacters(inputString:str):
    """
    This functions converts random characters to uppercase and remaining to lower case
    """
    outputString = ""
    strLen = len(inputString)
    for i in range(strLen):
        if random.randint(0, 1) == 0:
            outputString += inputString[i].upper()
        else:
            outputString += inputString[i].lower()
    return outputString


if __name__ == "__main__":
    inputString = input("Enter a string: ")
    print(convertRandomCharacters(inputString))