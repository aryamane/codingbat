def topping1(dict1):
    
    if 'ice cream' in dict1.keys():
        dict1['ice cream']='cherry'

    dict1.update({'bread':'butter'})

    return dict1


print(topping1({"ice cream": "peanuts"}))
print(topping1({}))
print(topping1({"pancake": "syrup"}) )