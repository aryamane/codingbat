import functools
def big_diff(nums):
  smallest_num = functools.reduce(lambda x,y : x if x<y else y, nums)
  largest_num = functools.reduce(lambda x,y : x if x>y else y, nums)
  return largest_num-smallest_num
  
  
print(big_diff([10, 3, 5, 6]) )
print(big_diff([7, 2, 10, 9]) )
print(big_diff([2, 10, 7, 2]) )