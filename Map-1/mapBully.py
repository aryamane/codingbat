def mapBully(dict1):

    dict1.update({"b":dict1['a']})

    dict1.update({"a":""})

    return dict1



print(mapBully({"a": "candy", "b": "dirt"}) )

print(mapBully({"a": "candy"}) )
print(mapBully({"a": "candy", "b": "carrot", "c": "meh"}))