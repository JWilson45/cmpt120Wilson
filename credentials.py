# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Jason Wison
# Created: 2018-02-20
def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first +'.'+ last
    passwd = input("Create a new password: ")
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured. Your new email address is",uname + "@marist.edu")
main()
