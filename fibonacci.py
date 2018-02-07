print("It's the Fibonacci")
def main():
    start,_next = 0,1
    
    n = eval(input("Enter a number for the Fibonacci: "))
    print("Calculating...")
    
    for i in range(n):
        temp = start + _next
        start = _next
        _next = temp
        print(start)
        
    print("Your Fibonacci is:",start)
    print("")
    main()
    
main()
