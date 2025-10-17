with open ('codingal.txt', 'r') as file1, open ('CodingalUpdated.txt', 'w') as file2:
    for line in file1:
        if not line.startswith('coding'):
            print(line)
            file2.write(line)

with open("codingal.txt","r") as file:
    data=file.readlines()
    for i in data:
        word=i.split()
        print(word)
file.close()

