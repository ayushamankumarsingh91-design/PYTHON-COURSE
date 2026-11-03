# write a function to merge_add(d1,d2) and add the values of those key which are common in the given dictionary such that
#d1={'a':1,'b':9} d2={'b':10,'c':7} merge_add(d1,d2) output={'a':1,'b':19,'c':7}
#note : dictionary are of same length
#output :{'a':1,'b':19,'c':7}


# d1 = {'a':1,'b':9}
# d2 = {'b':10,'c':7}
# def merge_add(d1, d2):
#     merged = d1.copy()
#     for key, value in d2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     return merged

# print(merge_add(d1, d2))
# print(d1[b])

#sirmode
def(d1,d2):
    for i in d1 :
    for j in d2 :
        if (i==j):
        d1[i]=d1[i]+d2[j]
    else:
return d1[i] = d2{j}

# ques ka part 2 : 2 dictionaries length are different
    



