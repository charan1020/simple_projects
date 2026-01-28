num=5
a=6
b=7
age=25
temperature=22
user_role="admin"
print("positive" if num>0 else "negative")
result="even" if a%2==0 else "odd"
max_num=a if a>b else b
min_num=a if a<b else b
status="adult" if age>=18 else "minor"
weather="warm" if temperature>=20 else "cold"
access_level="Full Access" if user_role=="admin" else "limited Access"
print(access_level)