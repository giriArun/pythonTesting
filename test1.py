# Dictionaries
# Like a map or hash table in other languages

cap = {}
cap["ola"] = "nitin"
cap["uber"] = "sudes"
cap["volvo"] = "sujan"

print(cap)
print(cap["ola"])
print(cap.get("BMW"))

for car in cap:
    print(car + ":" + cap[car])
    pass
    
print(cap["uber"])
