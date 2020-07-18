def lone_sum(a, b, c):
  
    
  if a ==b and b==c and a==c:
    return 0
  
  if a !=b and b!=c and a!=c:
    return a + b + c
  
  if a==b:
    return c
  
  if b==c:
    return a
  
  if a==c:
    return b
    
  else:
    return 0



# #their
# def lone_sum(a, b, c):
#   sum = 0
#   if a != b and a != c: sum += a
#   if b != a and b != c: sum += b
#   if c != a and c != b: sum += c
  
#   return sum
  
print(lone_sum(1, 2, 3) )
print(lone_sum(3, 2, 3) )
print(lone_sum(3, 3, 3) )