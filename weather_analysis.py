import numpy as np
import pandas as pd

# Weather dataset
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature': [30, 32, 29, 35, 33],
    'Humidity': [60, 65, 70, 55, 62],
    'Rainfall': [5, 0, 10, 0, 2]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("WEATHER TREND ANALYSIS")
print("----------------------")

# Display weather data
print("\nWeather Data:")
print(df)

# Average temperature using NumPy
avg_temp = np.mean(df['Temperature'])
print("\nAverage Temperature:", avg_temp)

# Maximum and minimum temperature
print("Maximum Temperature:", np.max(df['Temperature']))
print("Minimum Temperature:", np.min(df['Temperature']))

# Average humidity
avg_humidity = np.mean(df['Humidity'])
print("Average Humidity:", avg_humidity)

# Total rainfall
total_rainfall = np.sum(df['Rainfall'])
print("Total Rainfall:", total_rainfall)

# Hottest day
hottest_day = df.loc[df['Temperature'].idxmax(), 'Day']
print("Hottest Day:", hottest_day)

# Coldest day
coldest_day = df.loc[df['Temperature'].idxmin(), 'Day']
print("Coldest Day:", coldest_day)

# Simple weather analysis
print("\nWeather Analysis:")

if avg_temp > 30:
    print("The weather is generally hot.")
else:
    print("The weather is generally cool.")

if total_rainfall > 10:
    print("There is significant rainfall.")
else:
    print("There is low rainfall.")

print("\nProject Completed Successfully!")
