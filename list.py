mylist = [1,2,3,'a','b',1.2,'c']
print(len(mylist))
print(mylist)
print(mylist[1:4]) #prints 1,2 3 position elements
print(mylist[1:]) #prints elements 2,3,a,b,1.2,c
print(mylist[:1]) #prints 0th element


#appending the element
mylist.append('z')
print(mylist)


#inserting an element at desired position
mylist.insert(0,'A')
print(mylist)

#popping an item at 0th position
popped_item= mylist.pop(0)
mylist.pop() #pop's out last item
print(popped_item)



#nested list
mylist1 = [1,2,3]
mylist2 = [4,5,6]
mylist3 = [7,8,9]

mega_list = [mylist1,mylist2,mylist3]
print(mega_list)

print(mega_list[2][1]) #to grab element 8


mylist = ['hello','hai']
print(mylist[::-1])