def sum13(nums):
  result = 0
  i = 0
  j = len(nums)
  
  while i<j:
    if nums[i]==13:
      i=i+1
    else:
      result = result + nums[i]
    i = i+1
  
  return result


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]) )