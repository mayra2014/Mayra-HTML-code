# program to remove lines starting with any prefix.

file1 = open ('codingal.txt',
                         'r')
file2 = open ('CodingalUpdated.txt',
                         'w')
for line in file1.readlines():
        if not line.startswith('coding'):
            print(line)
            file2.write(line)
file2.close()
file1.close()