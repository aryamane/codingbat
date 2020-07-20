def firstChar(list1):
    dict1 = {}
    visited = []

    for i in range(len(list1)):    
        if list1[i][0] not in visited:  
            visited.append(list1[i][0]) 
            dict1.update({list1[i][0] : list1[i]}) 

        
        elif list1[i][0] in visited: 

            dict1.update({ list1[i][0]  : dict1[list1[i][0]] + list1[i] })
    
    return dict1



print(firstChar(["salt", "tea", "soda", "toast"]) )

#→ {"s": "saltsoda", "t": "teatoast"}


print(firstChar(["aa", "bb", "cc", "aAA", "cCC", "d"]) )
#→ {"a": "aaaAA", "b": "bb", "c": "cccCC", "d": "d"}

print(firstChar([]) )
#→ {}