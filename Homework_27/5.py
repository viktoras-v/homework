def strSort(s):
    return sorted(s, key=len)

words = ["apple", "fig", "banana", "kiwi", "cherry"]
sorted = strSort(words)
print(sorted)
