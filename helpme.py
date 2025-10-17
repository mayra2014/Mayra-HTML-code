#read first line of codingal.txt
file = open("codingal.txt", "r")
print("reading first line...")
print(file.readline())
file.close()

#read first 3 lines of codingal.txt
file = open("codingal.txt", "r")
print("reading multiple lines...")
print(file.readlines(3))
file.close()

#read all lines of codingal.txt
file = open("codingal.txt", "r")
print("reading all lines...")
print(file.read())
file.close()

#write in codingal.txt
file = open("codingal.txt", "w")
file.write("I am learning python file handling.")
file.close()

#append in codingal.txt
file = open("codingal.txt", "a")
file.write("\nI am enjoying it.")
file.close()
#read all lines of codingal.txt
file = open("codingal.txt", "r")
print("reading all lines...")
print(file.read())
file.close()

#read first line of codingal.txt
file = open("codingal.txt", "r")
print("reading first line...")
print(file.readline())
file.close()

#read first 3 lines of codingal.txt
file = open("codingal.txt", "r")
print("reading multiple lines...")
print(file.readlines(3))
file.close()


