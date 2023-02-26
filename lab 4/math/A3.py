import math
A = float(input("Input number of sides: "))
B = float(input("Input the length of a side: "))
print("The area of the polygon is: ",  int((((A/4) * math.pow(B, 2)) * (math.cos(math.pi/A)/math.sin(math.pi/A)))))