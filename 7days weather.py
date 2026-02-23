import requests
from datetime import datetime,timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os
today=datetime.now()
week_ago=today-timedelta(days=7)
start_date=week_ago.strftime("%Y-%m-%d")
end_date=today.strftime("%Y-%m-%d")
url=f"https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
response=requests.get(url)
data=response.json()
print(data)

#daily data
daily_data=data["daily"]
df=pd.DataFrame({'date':daily_data['time'],'max_temp':daily_data['temperature_2m_max'],'min_temp':daily_data['temperature_2m_min']})
df['date']=pd.to_datetime(df['date'])
print(df)

#create a plot
plt.figure(figsize=(10,6))
plt.plot(df['date'],df['max_temp'],label='Max Temperature')
plt.plot(df['date'],df['min_temp'],label='Min Temperature')

plt.xlabel('Date')
plt.ylabel("Temperature (c)")
plt.title('paris Weather -past 7 days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart.png')
plt.grid(True)
plt.show()

#create data folder if it doesnt exist
if not os.path.exists('data'):
    os.makedirs('data')

#save to CSV
df.to_csv('data/weather_data.csv',index=False)
print("data saved successfully")