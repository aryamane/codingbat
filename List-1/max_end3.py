#generalized
def max_end3(nums):
  if nums[0] > nums[-1]:
    for i in range(len(nums)):
      nums[i] = nums[0]
      
  else:
    for i in range(len(nums)):
      nums[i]=nums[-1]
  return nums

#their
# def max_end3(nums):
#   big = max(nums[0], nums[2])
#   nums[0] = big
#   nums[1] = big
#   nums[2] = big
#   return nums

print(max_end3([1, 2, 3]) )
print(max_end3([11, 5, 9]) )
print(max_end3([2, 11, 3]) )