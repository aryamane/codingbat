def not_string(str):
  if len(str)>=3 and str.lower()[0:3] == 'not':
    return str
  else:
    return ("not " + str)


print(not_string("not bad"))

print(not_string("not"))

print(not_string("arya"))



# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.

