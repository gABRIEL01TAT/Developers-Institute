My_dict = {}
Word = input("Enter your word  ")
for i, letters in enumerate(Word):
    if letters not in My_dict:
        My_dict[letters] = []
    My_dict[letters].append(i)

print(My_dict)
