from words import last_names

vowels = ['a', 'e', 'i', 'o', 'u']
for name in last_names:
    i = 0
    if name[i][0] in vowels:
        name += "way"
        print(name)
    else:
        first_letter = name[:1]
        new_name = name[1:]
        new_name += first_letter + "ay"
        print(new_name)
    i += 1