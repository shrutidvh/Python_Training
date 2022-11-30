print("Program2:")
t = int(input("Enter total: "))
w = int(input("Enter width: "))
h = int(input("Enter height: "))
if w == t and h == t:
    print("Area is perfect !!")
elif w < t and h < t:
    print("Area is bad !!")
elif w > t and h > t:
    print("Area is good !!")
