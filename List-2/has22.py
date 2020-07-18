def has22(nums):
  if len(nums)<=1:
    return False
  
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
                  
  return False


print(has22([1, 2, 2]) )
print(has22([1, 2, 1, 2]) )
print(has22([2, 1, 2]))