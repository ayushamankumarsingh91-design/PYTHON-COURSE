#15/09/2026

# list or tuple data structure
list1= [10,20,30,40,50,60,70,80,90,100]
list2 = ["Rungta",0.9,False,77]
print(list1)
print(list2)
tuple1= (10,20,30,40,50,60,70,80,90,100)
print(tuple1)

# built in funtion/methods in phython use (return something)
print(max(list1))
print(min(list1))
print(sum(list1))

# operations
# append : adding an element at the last of list
list1.append(110)
print(list1)
# insert's an element at particular position
print(list1.insert(6,55))
print(list1)
print(list1.count(1))
print(list1.index(20))

# how to declare a list 
#create a list having element 1 to 10 use for loop
li3 = [i for i in range(1,11)]
print(li3)
# prepare a list which is even between 50-100
li4 = [i for i in range(50,101) if i%2 ==0]
print(li4)
li5 = [i for i in range(50,101) if i%2 !=0]
print(li5)
li6 = [78,99,1010,"li4",5.0]
for i in range(len(li6)):
    print(li6[i])
    # here i signify index
for i in li6:
    print(i)
        #here i signify value
# 16/09/2026
# tupple unpacking (alag alag variable ko unpack kar dena /value assign kar dena)
st1 = ("Ravi",21,85)

name,age,per_st1 = st1
print(name)
print(age)
print(per_st1)

# swapiing value 
a = 10
b = 20

a,b = b,a
print(a)
print(b)
# this above method is only applicable in python
# tupple to list / list to tupple conversion

l1 = [1,2,2,3]
t1 = (5,56,6,7)

print(tuple(l1))
print(type(tuple(l1)))
print()
print(list(t1))
print(type(list(l1)))

# create a new list from an pre_existing tuple,where each of the new elements
#of list should be cube of the elements of tuple  if and only if the elements 
#are odd 

t2 = (56,67,99,87,31,32)
li_new = [i**3 for i in t2 if i%2 != 0]
print(li_new)

# Nsted loop ( loop ke ander loop)
#pattern based problem
#1. make 1st grid
#2. row and coulmn me relation find kare
# STAR PATTERN PRINT (*)
# right angle triangle / right angled solid traingle

#n = int(input())
#for i in range(1,n+1):
   # print("*")
    # ek loop laga ke outer loop controls rows

n = int(input())

#rows
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()

# 17/09/2026

#dictionary/sets
# dictionary me bhi indexes hote hai
stu1 = {"st_name": "Ayush Aman", "Section":L, "Marks" : 100.0}
print(stu1.get("st_name"))
print(stu1["st_name"])
print(stu1["Ayush Aman"])

# traverse (i is just a variable)
for i in stu1:
    print(i)

for i in  stu1.items():
    print(i)

for i in  stu1.values():
    print(i)

