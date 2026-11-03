# s = "The cat and the hat"
# s = s.lower()
# words = s.split()
# unique_words = set(words)
# print((len(unique_words)))


# 2nd way
s = "The cat and the hat"

def unique_words_count(s):
    s = s.lower().split()
    result = len(set(s))
    return result

print(unique_words_count(s))