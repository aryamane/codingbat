def word0(list1):
    
    return({}.fromkeys(list1,0))

print(word0(["a", "b", "a", "b"]))
print(word0(["a", "b", "a", "c", "b"]) )
#→ {"a": 0, "b": 0, "c": 0}
print(word0(["c", "b", "a"]) )
#→ {"a": 0, "b": 0, "c": 0}