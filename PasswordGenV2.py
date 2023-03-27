import random as rd

lower = "abcdefghijklmopqrstuvwxyz"
upper = lower.upper()
nums = "0123456789"
symbols = "!@#$%^&*?-=_+"

combined = lower+upper+nums+symbols

# Forces the user to have a password of atleast 8 characters, but a maximum of len(combined)
passLength = min(len(combined),max(8,int(input("What is the password's max length?\n"))))

# Forces the user to have a password of atleast 8 characters
numPasswords = max(1,int(input("\nHow many passowrds would you like to create?\n")))

saveToFile = bool(int(input("\nWould you like this password saved in a passwords file?\nInput 1 for yes, 0 for no.\n")))

for i in range(numPasswords):
    password = "".join(rd.sample(combined,passLength))
    if saveToFile:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n" + "\n")