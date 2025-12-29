def find_word(sarasas,target):
    for i, word in enumerate(sarasas):
        if word == target:
            return i
    return -1


sarasas=input("Enter list of words ").split()
target=input("Enter target word")
print(find_word(sarasas, target))