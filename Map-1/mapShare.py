def mapShare(dict1):

    if "a" in dict1.keys():
        dict1.update({"b":dict1['a']})
    
    dict1.pop("c")

    return dict1


print(dict(sorted(mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}).items()))) #→ {"a": "aaa", "b": "aaa"}
print(dict(sorted(mapShare({"b": "xyz", "c": "ccc"}).items()))) #→ {"b": "xyz"}
print(dict(sorted(mapShare({"a": "aaa", "c": "meh", "d": "hi"}).items()))) #→ {"a": "aaa", "b": "aaa", "d": "hi"}