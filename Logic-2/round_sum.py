def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  if num%10==0:
    return num
  
  if num%10>= 5 and num%10<=9:
    return num + (10-(num%10))
  
  else:
    return num - (num%10)


print(round_sum(16, 17, 18) )
print(round_sum(12, 13, 14) )
print(round_sum(6, 4, 4) )