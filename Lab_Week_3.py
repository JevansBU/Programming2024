#16/10/24
#Lists Exercise

'''my_list = [15,23,32,46]
print(my_list[0])
print(my_list[3])
print(my_list[0:2])

result = my_list[0] + my_list[3] #Adds 15 & 46 from the list
my_list.append(result) #Adds 'result' to the end of the list
print(my_list)'''

#PRACTRICE EXAMPLE ^^^^^
#Excerice 1 VVV

list1 = [10, 2.5, 'bean', 6 + 4, 'toast']
print(len(list1))
list1.append(20) #Adds onto the end of the list
list1.insert(0,'butter') #Adds wherever you want to add (at the start in this case)
list1.remove(20)
print(len(list1))
print(list1[0])
list1[1] = 'eggs'
print(type(list1))
tuple1 = tuple(list1)
print(type(tuple1))
print(tuple[0])
print(len(tuple1))
#tuple1[0] = 10     Impossible as tuples are immutable, need to change back to list if need to change
tuple2 = [8, 30, 57, 28, 67]
tuple2 = tuple(tuple2) #convert from list to tuple data type
merge_tuple = tuple1 + tuple2 #Add the two tuples to make one
print(merge_tuple)
newList = list(merge_tuple)
print(type(newList))
newSet = set(newList) #Convert the tuple list to a set
print(len(newSet))
print(newSet)
newSet.add('mushroom') #Add 'mushroom' onto the end of the set
newSet.add(8) #Duplications are not allowed, so when you print list you wont see this on the end of the list
print(newSet)
Set2 = [2, 9, 2, 1]
print()
newSet = list(newSet)
Set2 = list(Set2)
finalSet = newSet + Set2 #Changed both Sets into lists so i can merge together and print
print(finalSet)
