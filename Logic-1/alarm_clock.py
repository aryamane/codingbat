def alarm_clock(day, vacation):
  if day >=1 and day <= 5 and not vacation:
    return "7:00"
  
  if day >=1 and day <= 5 and  vacation:
    return "10:00"
  
  if (day == 0 or day == 6) and (not vacation):
    return "10:00"
  
  else:
    return "off"
  

print(alarm_clock(1, False) )
print(alarm_clock(5, False) )
print(alarm_clock(0, False) )