def array_front9(nums):
  
  length=len(nums)
  if length > 4:
    length = 4
  for i in range(length):
    if nums[i]==9:
      return True
  
  return False

print(array_front9([1,2,3,4,56]))

print(array_front9([1,2,3,4,56]))

print(array_front9([1,2,9,4,56]))