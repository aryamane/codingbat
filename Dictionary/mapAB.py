def mapAB(dict1):

    if "a" in dict1.keys() and "b" in dict1.keys():
        dict1.update({"ab": dict1["a"]+dict1["b"]})
    
    return dict1

print(mapAB({"a": "Hi", "b": "There"}) )
#→ {"a": "Hi", "ab": "HiThere", "b": "There"}