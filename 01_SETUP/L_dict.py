# 17/09/2026

#dictionary/sets
# dictionary me bhi indexes hote hai
stu1 = {"st_name": "Ayush Aman", "Section":"L", "Marks" : 100.0}
print(stu1.get("st_name"))
print(stu1["st_name"])
#print(stu1["Ayush Aman"])

# traverse (i is just a variable)
for i in stu1:
    print(i)

for i in  stu1.items():
    print(i)

for i in  stu1.values():
    print(i)

# make a dictionary for student where you will store Name ,ERP,Address,Phone No.,Section,Branch
#print items and values.

#nsted dictionary ( dictionary ke ander dictionary)

students = {
    "st2" : {"name" : "ravi","age" : 21},
    "st3" : {"name" : "harsh","age" : 28},
    "st4" : {"name" : "riya","age" : 30},
    "st5" : {"name" : "hari","age" : 10},
}

for i in students.values():
    print(i)
    print(students["st2"]["name"])

# 18/09/2026
stu1.pop()
print(stu1.pop())
print(stu1)
print(stu1.popitem())
print(stu1)
stu1.clear()
print(stu1)
del stu1
print(stu1)


