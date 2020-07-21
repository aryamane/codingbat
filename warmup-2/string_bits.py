def string_bits(str):
  return str[::2]

print(string_bits("Heelllloo"))

# their solution

# def string_bits(str):
#   result = ""
#   # Many ways to do this. This uses the standard loop of i on every char,
#   # and inside the loop skips the odd index values.
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result



# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".