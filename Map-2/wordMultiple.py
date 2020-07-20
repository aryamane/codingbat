def wordMultiple(list1):
    dict1 = {}.fromkeys(list1,'True')


    for i in range(len(list1)):
        if list1.count(list1[i]) >= 2:
            dict1.update( {  list1[i] : 'True' })
        else:
            dict1.update( {  list1[i] : 'False' })
    
    return dict1


print(wordMultiple(["a", "b", "a", "c", "b"]) )

print(wordMultiple(["c", "b", "a"]))

# → {"a": false, "b": false, "c": false}

print(wordMultiple(["c", "c", "c", "c"]) )

#→ {"c": true}

#→ {"a": true, "b": true, "c": false}