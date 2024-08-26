# Write a program that continuously takes input from the user and prints "Goodbye!" when the user types "exit"


def exit():
    while True:
        Ask = input("Type your input: ")
        if Ask == "exit" or Ask == "Exit":
            print("Goobye!")
            break

exit()            