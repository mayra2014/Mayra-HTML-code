pup=()
print(pup)

pup=(1,2,3,4,5,6,7,8,9,10)
print(pup)

pup=(1.2, 'mayra' , 3, 'moksha', 4.5)
print(pup)

pup=('mayra' , (1,2,3), [4,5,6], 7,8,9)
print(pup)

pup=('m','a','y','r','a')
print(pup[2])
print(pup[-1])
print(pup[1:4])
print(pup[0:2])
for m in pup:
    print(m)

pup[0]='s'eema
print(pup)
# Tuple is immutable, we cannot change or update the values in tuple
# pup[1:3]=(5,6)
# print(pup)                    

