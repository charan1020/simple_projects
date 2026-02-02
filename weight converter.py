weight=float(input("Enter weight: "))
unit=input("Enter unit (kg or lb): ")
if unit=='kg':
    weight=weight*2.205
elif unit=='lb':
    weight=weight/2.205
else:
    print("Invalid unit")
print(f"Weight in pounds: {weight} {unit}")