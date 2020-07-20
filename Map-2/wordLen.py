def wordLen(list1):
    dict1 = {}.fromkeys(list1,0)
    visited = []


    for i in range(len(list1)):
        if list1[i] not in visited:
            dict1.update( {  list1[i] : len(list1[i]) })
            visited.append(list1[i])

    
    return dict1


print(wordLen(["a", "bb", "a", "bb"]) )
#→ {"bb": 2, "a": 1}
print(wordLen(["this", "and", "that", "and"]) )
#→ {"that": 4, "and": 3, "this": 4}
print(wordLen(["code", "code", "code", "bug"]) )
#→ {"code": 4, "bug": 3}