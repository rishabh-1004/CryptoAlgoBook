import sys

def sq_mul(x, y):
    exp = bin(y)
    print ("Binary value of b is:",exp)
    print ("Bit\tResult")
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        print (i-1,":\t",value,"(square)")
        if(exp[i:i+1]=='1'):
            value = value*x
            print (i-1,":\t",value,"(multiply)")
    return value

print("Square and Multiply Method to Find Squares")
base=int(input("Enter Base"))  
power=int(input("Enter Power"))  
print ("==== Calculation ====")
res=sq_mul(base,power)
print ("Result:",res)

print ("===========")