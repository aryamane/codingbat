def front_times(str, n):
  if len(str) >= 3:
    return (str[:3]*n)
  else:
    return (str*n)

print(front_times("Chocolate",4))

print(front_times("Ch",5))