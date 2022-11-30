c = int(input("Number of classes held: "))
a = int(input("Number of classes attended: "))
per = a/c*100
print("percentage of classes attended is: ",per)
if per<75.0:
    print("not allowed")
else:
    print("allowed for exam")
