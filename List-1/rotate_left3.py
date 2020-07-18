def rotate_left3(nums):
  new_array = []
  
  for i in range(len(nums)-1):
    new_array.append(nums[i+1])
  new_array.append(nums[0])
  
  return new_array


print(rotate_left3([1, 2, 3]) )
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))