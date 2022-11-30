print("Program2:")
p1,q1= map(int,input("Enter Product1: ").split())
p2,q2= map(int,input("Enter Product2: ").split())
p3,q3= map(int,input("Enter Product3: ").split())
total = (p1*q1)+(p2*q2)+(p3*q3)
if total>1500:
    total = total + (total*0.0275)
    print("Total: ",total)
else:
    print("Total: ",total)

