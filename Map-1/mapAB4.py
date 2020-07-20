def mapAB4(dict1):

    if "a" in dict1.keys() and "b" in dict1.keys() and "c" in dict1.keys() :
        if len(dict1["a"])> len(dict1["b"]):
            dict1.update({"c":dict1["a"]})
        if len(dict1["b"])> len(dict1["a"]):
            dict1.update({"c":dict1["b"]})

    return dict1
            


print(mapAB4({"a": "aaa", "b": "bb", "c": "cake"}) )
#→ {"a": "aaa", "b": "bb", "c": "aaa"}


print(mapAB4({"a": "aa", "b": "bbb", "c": "cake"}) )
#→ {"a": "aa", "b": "bbb", "c": "bbb"}
print(mapAB4({"a": "aa", "b": "bbb"}) )
#→ {"a": "aa", "b": "bbb", "c": "bbb"}