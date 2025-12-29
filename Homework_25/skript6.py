count =0
print("Enter sentence")
sentence=input()
for letter in sentence:
    count = 0
    for ltr in sentence:
        if ltr==letter:
            count+=1
    print(f"Letter  {letter}  repeats,  {count}  times")