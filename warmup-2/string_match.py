def string_match(a, b):
  if len(a) < 2:
    return 0
  if len(b) < 2:
    return 0
  
  count = 0
  
  shorter = min(len(a),len(b))
  
  for i in range(shorter-1):
    if a[i:i+2]  == b[i:i+2]:
      count = count + 1
  
  return count


print(string_match("ppyttthooon","ppythoon"))


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.




