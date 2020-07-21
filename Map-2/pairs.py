def pairs(list1):
    dict1 = {}
    for i in range(len(list1)):
        dict1.update({  list1[i][0] : list1[i][-1] })
    
    return dict1



print(pairs(["code", "bug"]) )
#→ {"b": "g", "c": "e"}
print(pairs(["man", "moon", "main"]) )
#→ {"m": "n"}
print(dict(sorted(pairs(["man", "moon", "good", "night"]).items())))
# → {"g": "d", "m": "n", "n": "t"}


