
"""
/*Experiment-1(a)
Name : SHIVALIKA JAIRAM PILLAI
Class :SE-COMPS-B      Roll No: 461         Batch: B3

Aim : Write a python program to swap two numbers and check if the first number is positive or negative or zero.

Program :
"""
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Number before swapping:")
print("a = ",a)
print("b = ",b) 
a,b = b,a
print("Number after swapping:") 
print("a = ",a)
print("b = ",b)

if(a<0):
    print("First number",a," is negative") 
elif(a>0):
    print("First number",a,"is positive") 
else:
    print("First number is zero")

"""
Output :
Enter first number:72
Enter second number:-38
Number before swapping:
a =  72
b =  -38
Number after swapping:
a =  -38
b =  72
First number -38  is negative
"""
