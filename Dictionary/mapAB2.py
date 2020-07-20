def mapAB2(dict1):

    if "a" in dict1.keys() and "b" in dict1.keys() and dict1["a"] == dict1["b"]:
        dict1.pop("a")
        dict1.pop("b")
        return dict1
    else:
        return dict1


print(mapAB2({"a": "aaa", "b": "aaa", "c": "cake"}) )
print(mapAB2({"a": "aaa", "b": "bbb"}) )
print(mapAB2({"a": "aaa", "b": "bbb", "c": "aaa"}) )