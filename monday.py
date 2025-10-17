file1 = open('codingal.txt', 'r')
print(file1.read(6))
file1.close()

file2 = open('codingal.txt', 'r')
print(file2.readline())
file2.close()

file1 = open('codingal.txt', 'w')
file1.write("Hello, Codingal students!")
file1.close()
