def double_char(str):
  result_str=""
  
  for i in range(len(str)):
    result_str = result_str + str[i]*2
  
  return result_str

print(double_char("Hello"))