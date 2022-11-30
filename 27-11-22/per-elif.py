s1 = int(input("Enter sub1: "))
s2 = int(input("Enter sub2: "))
s3 = int(input("Enter sub3: "))
s4 = int(input("Enter sub4: "))
s5 = int(input("Enter sub5: "))
per = (s1+s2+s3+s4+s5)/500*100
if per>35.0 and per<=65.0:
    print("Pass")
elif per>65.0 and per<=75.0:
    print("First Class")
elif per>75.0 and per<=100:
    print("Distinction")
else:
    print("Fail")



