d1 = {"a" : -9, "b" : -10, "c" :-1}

def max_key(dict):
    max_val = (-1)*(2**32)
    for i in dict:
        if dict[i] > max_val:
            max_val = dict[i]
            max_key = i
    return max_key

print(max_key(d1))