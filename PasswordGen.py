import random as rd

passLength = int(input("What is the password's max length?\n"))
if passLength < 8:
    print("\nThe password's length must be greater than or equal to 8 characters!")
    exit()

numPasswords = int(input("\nHow many passowrds would you like to create?\n"))
if numPasswords < 1:
    print("\nThe number of passwords must be greater than 1!")
    exit()


# saveFile = bool(int(input("\nWould you like this password saved in a passwords file?\nInput 1 for yes, 0 for no.\n")))


def GeneratePassword(length: int) -> str:
    """Returns a random password with <= 1 Upper & lower & special & number"""
    numUpper = rd.randint(2, length - 6)
    length -= numUpper

    numSpecial = rd.randint(2, length - 4)
    length -= numSpecial

    numNumber = rd.randint(2, length - 2)
    length -= numNumber

    numLower = length

    generatedCharacters = ConcatLists(
        CreateUpperList(numUpper),
        CreateLowerList(numLower),
        CreateSpecialList(numSpecial),
        CreateNumberList(numNumber),
    )

    return ScrambleCharacters(generatedCharacters)


def CreateUpperList(numUpper: int) -> list:
    upperList = []

    for i in range(numUpper):
        upperList.append(chr(rd.randint(65, 90)))

    return upperList


def CreateLowerList(numLower: int) -> list:
    lowerList = []

    for i in range(numLower):
        lowerList.append(chr(rd.randint(97, 122)))

    return lowerList


def CreateSpecialList(numSpecial: int) -> list:
    specialList = []
    acceptedSpecials = "!@#$%^&*"

    for i in range(numSpecial):
        specialList.append(acceptedSpecials[(rd.randint(0, 7))])

    return specialList


def CreateNumberList(numNumber: int) -> list:
    upperList = list((str(rd.randint(0, 9)) for _ in range(numNumber)))

    return upperList


def ConcatLists(l1: list, l2: list, l3: list, l4: list) -> list:
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)

    return l1


def ScrambleCharacters(chars: list) -> str:
    scrambledPass = ""

    for i in range(len(chars) - 1, -1, -1):
        scrambledPass += chars.pop(rd.randint(0, i))

    return scrambledPass


for i in range(numPasswords):
    password = GeneratePassword(passLength)
    print(password)
