file=open("abc.txt","r")
print(file.readlines())
file.close()

file1=open("abc.txt","w")
file1.write("HELLO WORLDDDD")
file1.close()

file2=open("abc.txt","a")
file2.write("\nHELLO INDIA")
file2.close()
