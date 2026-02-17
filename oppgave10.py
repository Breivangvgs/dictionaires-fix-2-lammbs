Dictionary = {
    "Ti": 10, 
    "Tjue": 20, 
    "Thirty": 30, 
    "Førti": 40, 
    "Femti": 50
    }

Dictionary.update({}) 

val = Dictionary.pop("Thirty")
Dictionary['Tretti'] = val

sorted_Dictionary = sorted(Dictionary.items(), key=lambda x: x[1])
sorted_Dictionary = dict(sorted_Dictionary)
print(sorted_Dictionary)