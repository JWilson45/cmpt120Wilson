#pi.py
# aproximates the value of pi
import math

def main():
    
    n = int(input("Enter the number of terms to aproximate the value of pi:"))
    
    result = 0
    sign = 1
    
    for i in range(1, n * 2 + 1, 2):
        term = 4 / i * sign
        result = result + term
        sign = sign * -1
        
    print("Pi =",math.pi)
    print("Your aproximated value of pi is:" ,result)
    
    diff= result-math.pi
    
    print("The difference is:",diff)
    
    print("")
    main()
    
main()
