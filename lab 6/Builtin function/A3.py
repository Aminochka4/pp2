a = [i for i in input()]
b = a.copy()
a.reverse()
if a == b:
    print ("It is palindrome")
else:
    print("It is not palindrome")