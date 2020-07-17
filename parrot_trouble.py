def parrot_trouble(talking, hour):
  # if talking and (hour<7 or hour>20):
  #   return True
  # else:
  #   return False
  return(talking and (hour<7 or hour>20))

print(parrot_trouble(True,21))