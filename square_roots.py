import math

num = float(input("Enter a number to find its square root: "))

if num < 0:
    print("Square root of negative numbers is not real.")
else:
    result = math.sqrt(num)
    
    print("The square root of", num, "is:", result)