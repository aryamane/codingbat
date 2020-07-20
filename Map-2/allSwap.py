def allSwap(list1):
    dict1 = {}

    for i in range(len(list1)):
        if list1[i][0] not in dict1.keys():
            dict1.update( {list1[i][0] : list1[i] } )
        
        else: 
            temp = list1[i]
            list1[i] = dict1[list1[i][0]]
            list1[list1.index(dict1[list1[i][0]])] = temp
    
    return list1

    


print(allSwap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"]) )

#→ ["ay", "by", "cy", "cx", "bx", "ax", "azz", "aaa"]