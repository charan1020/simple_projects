unit=input("Enter unit (C or F): ")
temp=float(input("Enter temperature: "))
if unit=='C':
    temp=(temp*9/5)+32
    print(f"Temperature in F: {temp} F")
elif unit=='F':
    temp=(temp-32)*5/9
    print(f"Temperature in C: {temp} C")
else:
    print("Invalid unit")