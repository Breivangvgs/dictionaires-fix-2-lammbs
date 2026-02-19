Dictionary = {
    "Ti": 10, 
    "Tjue": 20, 
    "Tretti": 30, 
    30: "Tretti", 
    "Førti": 40, 
    "Femti": 50
    } 
del Dictionary[30]


v = 20

if v in Dictionary.values():
    print(f"The value {v} exists in the dictionary.")
else:
    print(f"The value {v} does not exist in the dictionary.")

v = 40

if v in Dictionary.values():
    print(f"The value {v} exists in the dictionary.")
else:
    print(f"The value {v} does not exist in the dictionary.")


v = 60

if v in Dictionary.values():
    print(f"The value {v} exists in the dictionary.")
else:
    print(f"The value {v} does not exist in the dictionary.")

