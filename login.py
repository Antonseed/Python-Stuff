import os
import json
import sys
from getpass import getpass


# Functions--------------------------------------------------------------------
def quitProgram():
    print("Exiting...")
    exit()


usrInp = input("Would you like the simple(1) or json log-in(2)? (type '1' or '2'): ")
if usrInp == "1":
    # Simple login--------------------------------------------------------------------------------------------
    usrName = "admin"
    usrPass = "admin"
    i = 0
    while i < 1:
        usrInp = input("please enter your username: ")
        usrPsw = getpass(prompt="please enter your password: ")
        print(usrPass)
        if usrInp == usrName:
            if usrPsw == usrPass:
                print("Welcome")
                i = 1
        else:
            print("Incorrect details, please try again")
            usrInp = input("Please enter your Email: ")
            pswInp = input("Please enter your Password: ")

    i = 0
    while i < 1:
        comInp = input("Please type a command: ")

        if comInp == "exit" or comInp == "quit":
            quitProgram()
        elif comInp == "hi" or comInp == "hello":
            print("hello, " + usrName)
elif usrInp == "2":
    # Login using JSON-------------------------------------------------------------------------------------

    # Variable
    user_credentials = "cred.json"
    i = 0

    # Load json file
    if os.path.isfile(user_credentials):
        print("Loading credentials...")
        with open('cred.json') as jsonFile:
            data = json.load(jsonFile)
        print("Credentials Loaded! ")

    usrName = data["Name"]
    usrPass = data["Password"]
    print("Name: " + usrName)
    print("Pass: " + usrPass)

    while i < 1:
        usrInp = input("please enter your username: ")
        usrPsw = input("please enter your password: ")
        if usrInp == data["Name"]:
            if usrPsw == data["Password"]:
                print("Welcome")
                i = 1
        else:
            print("Incorrect details, please try again")
            usrInp = input("Please enter your Email: ")
            pswInp = input("Please enter your Password: ")

    i = 0
    while i < 1:
        comInp = input("Please type a command: ")

        if comInp == "exit" or comInp == "quit":
            quitProgram()
        elif comInp == "hi" or comInp == "hello":
            print("hello" + usrName)
