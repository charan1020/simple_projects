weight=float(input("Enter weight: "))
unit=input("Enter unit (kg or lbs): ")
if unit=="kg":
    weight=weight*2.20462
    unit="lbs"
elif unit=="lbs":
    weight=weight/2.20462
    unit="kg"
else:
    print(f"Unknown unit: {unit}")
print(f"Weight in {unit}: {weight}")