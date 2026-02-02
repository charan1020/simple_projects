principle=0
rate=0
time=0
while principle<=0:
    principle=float(input("Enter the principle amount: "))
    if principle<=0:
        print("Principle amount must be greater than or equal to0")
while rate<=0:
    rate=float(input("Enter the rate of interest: "))
    if rate<=0:
        print("Rate of interest must be greater than or equal to 0")
while time<=0:
    time=float(input("Enter the time in years: "))
    if time<=0:
        print("Time must be greater than or equal to0")
si=(principle*rate*time)/100
print(f"Simple Interest: {si}")
ci=principle*(1+rate/100)**time-principle
print(f"Compound Interest: {ci}")