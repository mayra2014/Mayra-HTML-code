fruits=['apple','banana','cherry','date ','elderberry','orange','grape','kiwi','mango','papaya' ,'peach','pear','plum','pomegranate','raspberry','strawberry','watermelon']
print ("the lenth of the list is",len(fruits))

print("the first element is",fruits[0])
print("the last element is",fruits[-1])
fruits.append('orange')
print("the list after adding orange is",fruits)
fruits.remove('banana')
print("the list after removing banana is",fruits)
fruits.sort()
print("the list after sorting is",fruits)
print("the list in reverse order is",fruits[::-1])
print("the list in upper case is",[fruit.upper() for fruit in fruits])
print("the list in lower case is",[fruit.lower() for fruit in fruits])
