import random as rd

"""******************************DECLARE ALL FUNCTIONS******************************"""


def ValidatePasswordLength(passLength: int) -> None:
    if passLength < 8:
        print("\nThe password's length must be greater than or equal to 8 characters!")
        exit()


def ValidateNumberPasswords(numPasswords: int) -> None:
    if numPasswords < 1:
        print("\nThe number of passwords must be greater than 1!")
        exit()


def GetCharacterNumbers(passLength: int) -> tuple:
    """Returns a tuple of four integers that correlate to the number of a specific characters in the final password"""
    n1 = rd.randint(2, passLength - 6)
    passLength -= n1

    n2 = rd.randint(2, passLength - 4)
    passLength -= n2

    n3 = rd.randint(2, passLength - 2)
    passLength -= n3

    n4 = passLength

    return (n1, n2, n3, n4)


def ConcatLists(l1: list, l2: list, l3: list, l4: list) -> list:
    """Extends l1 with all the values inside of l2-4"""
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)

    return l1


def CreateUpperList(numUpper: int) -> list:
    """Creates a list, with length of numUpper, of only uppercase characters"""
    upperList = []

    for _ in range(numUpper):
        upperList.append(chr(rd.randint(65, 90)))

    return upperList


def CreateLowerList(numLower: int) -> list:
    """Creates a list, with length of numLower, of only lowercase characters"""
    lowerList = []

    for _ in range(numLower):
        lowerList.append(chr(rd.randint(97, 122)))

    return lowerList


def CreateSpecialList(numSpecial: int) -> list:
    """Creates a list, with length of numSpecial, of only special characters"""
    specialList = []
    acceptedSpecials = "!@#$%^&*"

    for _ in range(numSpecial):
        specialList.append(acceptedSpecials[(rd.randint(0, 7))])

    return specialList


def CreateNumberList(numNumber: int) -> list:
    """Creates a list, with length of numNumber, of only numbers 0-9"""
    upperList = list((str(rd.randint(0, 9)) for _ in range(numNumber)))

    return upperList


def ScrambleCharacters(chars: list) -> str:
    """Randomly pops a character from the generated characters list and appends it to the return string"""
    scrambledPass = ""

    for i in range(len(chars) - 1, -1, -1):
        scrambledPass += chars.pop(rd.randint(0, i))

    return scrambledPass


def DisplayPassword(password: str, save: bool) -> None:
    """Print password and save to file if user desires"""
    print(password)

    if save:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n" + "\n")


def GeneratePasswords(passLength: int, saveToFile: bool, numPasswords: int) -> None:
    """Prints random passwords with at least 2 Upper, 2 lower, 2 numbers, and 2 sepecial characters"""

    # Create as many passwords as the user requested
    for _ in range(numPasswords):
        # The left most variable will typically get assigned a larger integer, hence more characters in the final password
        numSpecial, numUpper, numNumber, numLower = GetCharacterNumbers(passLength)

        generatedCharacters = ConcatLists(
            CreateUpperList(numUpper),
            CreateLowerList(numLower),
            CreateSpecialList(numSpecial),
            CreateNumberList(numNumber),
        )

        password = ScrambleCharacters(generatedCharacters)
        DisplayPassword(password, saveToFile)


"""******************************EXECUTE MAIN PROGRAM******************************"""

passLength = int(input("What is the password's max length?\n"))
ValidatePasswordLength(passLength)

numPasswords = int(input("\nHow many passowrds would you like to create?\n"))
ValidateNumberPasswords(numPasswords)

saveToFile = bool(int(input("\nWould you like this password saved in a passwords file?\nInput 1 for yes, 0 for no.\n")))

GeneratePasswords(passLength, saveToFile, numPasswords)
