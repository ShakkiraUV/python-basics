
my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))
#properties of list
#1.ordered
fruits=['apple','banana']
print(fruits)
fruits=['banana','apple']
print(fruits)
#2.allows duplicates
fruits=['banana','apple','banana']
print(fruits)
#3.heterogeneous:can store any data type
mixed=[1,'hello',3.14,True]
print(mixed)
l=[1,2,3,4,5]
print(l)
print(type(l))
l1=[3,'hello',4,None,'A',[1,2,3,4],True,2+1j]
print(l1)
print(type(l1))
#4.mutable:elements can change
my_list=[1,2,3]
my_list[0]=100
print(my_list)
#slicing and indexing
l=["hello","hi",23,45.6,True,12,78,False,[1,2,3,4,5,6]]
print(l[3])