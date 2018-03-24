# CMPT 120 - Lab #6
# Jason Wilson
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")

    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        while True:
            cmd = input("What computation do you want to perform? ").lower()
            if cmd == "add" or cmd == "mult" or cmd == "sub" or cmd == "div"\
               or cmd == "quit":
                break
            else:
                print("'"+cmd+"'","is not a valid command. Try again.\n")             
        if cmd == "quit":
            break
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if cmd == "div":
                num1/num2
        except ValueError:
            print("Must use numbers\n")
            continue
        except:
            print("Cannot divide by 0\n")
            continue
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
            result = num1 - num2
        elif cmd == "mult":
            result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        print("The result is " + str(result) + ".\n")
def main():
    showIntro()
    doLoop()
    showOutro()
main()
