# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Jason Wison
# Created: 2018-02-20
def FirstandLast():
    first,last = input("Enter your first name: "),input("Enter your last name: ")
    first,last = first.lower(),last.lower()
    return [first,last]

def username(first,last):
    uname = first +'.'+ last
    return uname

def pword():
    strong = 1
    while strong == 1:
        strong = pstrong(input("Create a new password: "))
        strong = pcapcheck(strong)
    return strong

def pstrong(pa):
    while len(pa) < 8:
        print("Fool of a Took! That password is feeble! Make it longer!")
        return 1
    return pa

def pcapcheck(cap):
    if cap == 1:
        return 1
    passCoppy1,passCoppy2 = cap,cap
    passCoppy1 = passCoppy1.upper()
    passCoppy2 = passCoppy2.lower()
    if passCoppy1 == cap or passCoppy2 == cap:
        print('Your password needs UPPER and lower case characters')
        return 1
    else:
        return cap

def main():
    name = FirstandLast()
    uname = username(name[0],name[1])
    passwd = pword()
    print("The force is strong in this one...")
    print("Account configured. Your new email address is",uname + "@marist.edu")

main()
