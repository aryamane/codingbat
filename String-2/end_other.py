def end_other(a, b):
  
  #Solution 1
  # len_a = len(a)
  
  # len_b = len(b)
  
  # if a[-len_b:].lower() == b.lower() or b[-len_a:].lower() == a.lower():
  #   return True
  # else:
  #   return False
    
  # Solution 2
  
  a = a.lower()
  b = b.lower()
  
  return(b.endswith(a) or a.endswith(b))
  
print(end_other('abc','xyzabc'))