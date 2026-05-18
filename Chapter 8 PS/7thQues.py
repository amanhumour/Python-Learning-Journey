def rem(l, word):
    n = []
    for item in l: 
        if not item == word:
            n.append(item.strip(word))
    return n

l = [ "apple", "banana", "grape", "orange", "pineapple"]
print(rem(l, "a"))