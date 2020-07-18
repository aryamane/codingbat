def make_ends(nums):
  new_array=[]
  new_array.append(nums[0])
  new_array.append(nums[-1])
  return(new_array)



print(make_ends([1, 2, 3]) )
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]) )