unit=input("Enter unit to convert to (C or F): ")
temp=float(input("Enter temperature: "))
if unit=="c":
    temp=(temp-32)*(5/9)
    unit="C"
elif unit=="f":
    temp=(temp*(9/5))+32
    unit="F"
else:
    print(f"Unknown unit: {unit}")
print(f"Temperature in {unit}: {temp}")