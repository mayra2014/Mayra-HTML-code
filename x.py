f=open("newfile.txt","x")
f.close()
import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
file=open("newfile.txt","a")
file.write("hello world\n")
file.write("welcome to codingal\n")
file.write("python programming\n")
file.close()