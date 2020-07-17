def missing_char(str, n):
  front = str[0:n]
  back = str[n+1:]
  return front+back


print(missing_char("hello",2))