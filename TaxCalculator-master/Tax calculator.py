# Made by Joshua Hillis
import re
import time
print ("Created by Joshua Hillis")
time.sleep(1.5)
while 1 == 1:
    def userinput():
        tax = input("what is the tax rate we will apply to the item?")
        price = input("what is the base price of the item?")
    try:
        tax = float(input("What is the tax rate we will apply to the item?"))
        price = float(input("What is the base price of the item?"))
    except:
        print("Please enter an integer")
        tax = float(input("What is the tax rate we will apply to the item?"))
        price = float(input("What is the base price of the item?"))

    total = str(format((round((float(tax) / 100 + 1) * float(price), 2)), '.2f'))
    print(total)
    restart = input("would you like to calculate again? (y/n)").lower()
    if restart == "y" or restart == "n":
        if restart == "y":
            userinput()
            total = str(format((round((float(tax) / 100 + 1) * float(price), 2)), '.2f'))
            print(total)
    else:
        print("please input a valid variable")
        print(restart)
    if restart == ('n'):
        quit()

