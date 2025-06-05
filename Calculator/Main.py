#this one is the main page that takes in what the user wants, and outputs math
import TimeCalculator as TC
import normalmath as NM

print("Hello, welcome to the Calculator app. \nThis app can either do basic math, or calculate time.")

choice = input("For Math, please press 1. For Time, please press 2.\n")

choice = int(choice)

if choice == 1:
    num1 = input("Please input your first number")
    num1 = int(num1)
    num2 = int(input("Please Input your second number"))
    operator = input("Please input your operator")
    mathAns = NM.yaku(num1, num2, operator)
    print(mathAns)

elif choice==2:
    print("You have selected to convert time. How many Mins would you like to convert to Hours?")
    minsToConvert = input()
    convertedHours, remainingMins = TC.MinToHour(minsToConvert)
    print(f"{minsToConvert} is {convertedHours} hours and {remainingMins} mins")

else:
    print("Error, please reset the program")