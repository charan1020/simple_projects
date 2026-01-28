temp=25
#is_raining=False
#if temp>35 or temp<0 or is_raining:
   # print("Stay inside")
#else:
 #   print("Go outside")
is_sunny=True
if temp>28 and is_sunny:
    print("It is HOT outside")
    print("IT IS SUNNY")
elif temp<0 and not is_sunny:
    print("It is COLD outside")
    print("IT IS NOT SUNNY")
elif 28> temp>0 and is_sunny:
    print("It is WARM outside")
    print("IT IS SUNNY")
elif temp>=28 and not is_sunny:
    print("It is HOT outside")
    print("IT IS CLOUDY")
elif temp<=0 and not is_sunny:
    print("It is COLD outside")
    print("IT IS CLOUDY")
else:
    print("It is COOL outside")
    print("IT IS CLOUDY")