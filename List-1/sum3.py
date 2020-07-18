import functools

def sum3(nums):
  return functools.reduce(lambda x,y: x+y, nums)

print(sum3([1, 2, 3]) )
print(sum3([5, 11, 2]) )
print(sum3([7, 0, 0]) )


#solution 2
#   result = 0
  
#   for i in range(len(nums)):
#     result = result + nums[i]
  
#   return result