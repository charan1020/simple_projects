principle=0
rate=0
time=0    
while True:
    principle=float(input("Enter the principle amount: "))
    if principle<0:
        print("Principle can't be less than or equal to 0")
    else:
        break
while True:
    rate=float(input("Enter the rate of interest: "))
    if rate<0:
        print("Rate can't be less than or equal to 0")  
    else:
        break
while True:
    time=float(input("Enter the time period: "))
    if time<0:
        print("Time can't be less than or equal to Zero")
    else:
        break
total=principle*pow((1+rate/100),time)
print(f"Balance after {time} years is: ${total:.2f}")