Dictionary = {"Femti": 50, "Førti": 40, "Tretti": 30, "Tjue": 20, "Ti": 10} 
sorted_Dictionary = sorted(Dictionary.items(), key=lambda x: x[1])
sorted_Dictionary = dict(sorted_Dictionary)
print(sorted_Dictionary)