def same_first_last(nums):
  if len(nums)<1:
    return False
  if nums[0] == nums[-1]:
    return True
  return False

print(same_first_last([1, 2, 3]) )
print(same_first_last([1, 2, 3, 1]) )
print(same_first_last([1, 2, 1]) )