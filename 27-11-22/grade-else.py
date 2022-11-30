print("Program1:")
s1,s2,s3,s4,s5 = map(int,input("Enter Marks: ").split())
per = (s1+s2+s3+s4+s5)/500*100
if per>90.0 and per<=100:
    print("you got A+")
elif per>80.0 and per<=90:
    print("A")
elif per>70.0 and per<80.0:
    print("B+")
elif per>60.0 and per<70.0:
    print("B")
elif per>50.0 and per<60.0:
    print("C")
elif per<50.0:
    print("You are Fail :(")
