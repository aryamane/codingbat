def sum67(nums):
  six = False
  result = 0
  for i in range(len(nums)):
    
    if nums[i]==6:
      six = True
    
    if not six:
      result = result + nums[i]
    
    if six and nums[i]== 7:
      six = False
    

  
  return result


print(sum67([1, 2, 2]) )
print(sum67([1, 2, 2, 6, 99, 99, 7]) )
print(sum67([1, 1, 6, 7, 2]))