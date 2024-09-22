import pandas as pd
import numpy as np

# Membaca data dari CSV untuk analisis
df = pd.read_csv("weather_data.csv")

# Rata-rata suhu dari semua kota
average_temperature = df["Temperature"].mean()
print(f"Rata-rata suhu dari semua kota: {average_temperature:.2f}°C")

# Kota dengan suhu terendah dan tertinggi
lowest_temp_city = df.loc[df["Temperature"].idxmin()]["City"]
lowest_temp = df["Temperature"].min()
highest_temp_city = df.loc[df["Temperature"].idxmax()]["City"]
highest_temp = df["Temperature"].max()
print(f"Kota dengan suhu terendah: {lowest_temp_city}({lowest_temp}°C)")
print(f"Kota dengan suhu tertinggi: {highest_temp_city}({highest_temp}°C)")

# Pola cuaca yang paling sering muncul
most_common_weather = df["Description"].mode()[0]
print(f"Pola cuaca yang paling sering muncul: {most_common_weather}")