def wordAppend(list1):
    visited = []
    result = ""

    for i in range(len(list1)):
        if list1[i] in visited and  visited.count(list1[i])%2==1:
            result=result+list1[i]
            visited.append(list1[i])

        else:
            visited.append(list1[i])
    return result


print(wordAppend(["a", "b", "a"]) )
#→ "a"
print(wordAppend(["a", "b", "a", "c", "a", "d", "a"]) )
#→ "aa"
print(wordAppend(["a", "", "a"]) )
#→ "a"

print(wordAppend(["not", "and", "or", "and", "this", "and", "or", "that", "not"]) )
#→ "andornot"

print(wordAppend(["xx", "xx", "yy", "xx", "zz", "yy", "zz", "xx"]) )
#→ "xxyyzzxx"