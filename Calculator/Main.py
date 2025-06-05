#this one is the main page that takes in what the user wants, and outputs math


print("Hello, welcome to the Calculator app. \nThis app can either do basic math, or calculate time.")

choice = input("For Math, please press 1. For Time, please press 2.")

choice = int(choice)

if choice == 1:


elif choice==2:


else:
    print("Error, please reset the program")