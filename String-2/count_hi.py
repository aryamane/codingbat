def count_hi(str):
  #return str.count('hi') # Solution 1
  
  #Solution 2
  count = 0
  
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count = count + 1
  
  return count

print(count_hi('abc hi hi ho'))