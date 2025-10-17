outputfile=open("asmayra.txt","w")
inputfile=open("repeated.txt","r")
lines=set()
for i in inputfile:
    if i not in lines:
        outputfile.write(i)
        lines.add(i)
inputfile.close()
outputfile.close()
print("Duplicate lines removed. Check 'updatedfile.txt' for results.")