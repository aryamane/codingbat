def wordCount(list1):
    dict1 = {}.fromkeys(list1,0)
    visited_values = []

    for i in range(len(list1)):
        if list1[i] not in visited_values:
            dict1.update( {  list1[i] : list1.count(list1[i])} )
            visited_values.append(list1[i])
    
    return dict1


print(wordCount(["a", "b", "a", "c", "b"]) )

#→ {"a": 2, "b": 2, "c": 1}


print(dict(sorted(wordCount(["c", "b", "a"]).items())))

#→ {"a": 1, "b": 1, "c": 1}

print(wordCount(["c", "c", "c", "c"]))

# → {"c": 4}