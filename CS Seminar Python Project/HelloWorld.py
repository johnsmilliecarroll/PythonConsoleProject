# References: https://ozzmaker.com/add-colour-to-text-in-python/ for color
# https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid to brush up on dates and
# validation
mycol = 37
print("Hello World")
print("type \"exit\" to close the program at any time")
ans1 = input("What is your first name? ")
# for every input we first check if they want to exit
if ans1 == "exit":
    exit()
ans2 = input("What is your last name? ")
if ans2 == "exit":
    exit()
ans3 = input("Hello " + ans1 + " " + ans2 + "! What is your favorite conventional color? ")
if ans3 == "exit":
    exit()
# uppercase the input so capitalization doesn't effect validation
elif ans3.upper() == "BLACK":
    mycol = 30
elif ans3.upper() == "BLUE":
    mycol = 34
elif ans3.upper() == "RED":
    mycol = 31
elif ans3.upper() == "GREEN":
    mycol = 32
elif ans3.upper() == "YELLOW":
    mycol = 33
elif ans3.upper() == "ORANGE":
    mycol = 33
elif ans3.upper() == "PURPLE":
    mycol = 35
elif ans3.upper() == "WHITE":
    mycol = 38
elif ans3.upper() == "GRAY":
    mycol = 37
else:
    print("I didn't write code for that color. Hope you like gray!")
# print statements will now be colored with whatever they picked
print("\033[0;" + str(mycol) + "mLooks great on you, " + ans1 + " " + ans2 + "!")
print("\033[0;" + str(mycol) + "mWhen is your birthday?")
# start while loop with a bool that will only be complete when a properly formatted date is provided
invaliddate = True
while invaliddate:
    ans4 = input("Please give me a date in valid m/d/yyyy format. ")
    if ans4 == "exit":
        exit()
    else:
        mylist = ans4.split("/")
    if len(mylist) != 3:
        # error message is bold and red
        print("\033[1;31mThat's not a valid input.")
    else:
        import datetime

        # test the input to see if it is in the proper format
        try:
            mydate = datetime.datetime(int(mylist[2]), int(mylist[0]), int(mylist[1]))
            invaliddate = False
        except ValueError:
            # improper format, loop around and try again
            print("\033[1;31mThat's not a valid input.")
            invaliddate = True

print(
    "\033[0;" + str(mycol) + "m" + ans1 + " " + ans2 + " was born on " + mydate.strftime("%A") + ", " + mydate.strftime(
        "%B") + " " + mydate.strftime("%d") + ", " + mydate.strftime("%Y") + ".")
print("\033[1;31mYour information has been stored in a database to be used with malicious intent. Muahahaha.")
