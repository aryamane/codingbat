def mapAB3(dict1):
    if "a" in dict1.keys() and "b" not in dict1.keys():
        dict1.update({"b":dict1['a']})

    
    if "b" in dict1.keys() and "a" not in dict1.keys():
        dict1.update({"a":dict1['b']})
    
    return dict1
    

print(dict(sorted(mapAB3({"a": "aaa", "c": "cake"}).items())))
# -> {"a": "aaa", "b": "aaa", "c": "cake"}

print(dict(sorted(mapAB3({"b": "bbb", "c": "cake"}) .items())))

#→ {"a": "bbb", "b": "bbb", "c": "cake"}

print(dict(sorted(mapAB3({"a": "aaa", "b": "bbb", "c": "cake"}).items())))

#→ {"a": "aaa", "b": "bbb", "c": "cake"}