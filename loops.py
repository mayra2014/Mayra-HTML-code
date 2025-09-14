num = int(input("Enter the number:"))
print("Table of ", num)
for i in range(1, 125):
 mul = num*i
 print("%d x %d = %d" % ( num,i, mul))
