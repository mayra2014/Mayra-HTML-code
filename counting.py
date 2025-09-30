file=open("rar.txt","r")
counter=0
content=file.read()
colist=content.split("\n")
for i in colist:
    if i:
        counter+=1
print("No of lines:",counter)
