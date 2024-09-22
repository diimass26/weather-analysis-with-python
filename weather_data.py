import requests
import csv
from datetime import datetime as dt

#setup openweathermap API
API_KEY = "3187d73f2af62a355a36ac8626103587"
CITYS = ["Tanjungpinang", "Jakarta", "Pekanbaru", "Surabaya", "Bali"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Nama file CSV
filename = "weather_data.csv"

# Cek apakah file sudah ada, jika belum buat dengan header
file_exists = False
try:
    with open(filename, 'r') as csvfile:
        file_exists = True
except FileNotFoundError:
    file_exists = False

# Membuka file CSV untuk menulis data
with open(filename, mode='a', newline='') as csvfile:
    fieldnames = ["City", "Temperature", "Humidity", "Pressure", "Wind Speed", "Description", "Date Time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Jika file belum ada, tulis header
    if not file_exists:
        writer.writeheader()

    # Loop melalui setiap kota dalam daftar
    for city_name in CITYS:
        # Menyusun URL lengkap dengan nama kota dan API key
        complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"

        # Mengirim permintaan ke URL
        response = requests.get(complete_url)

        # Mengubah respons JSON ke dalam bentuk dictionary
        weather_data = response.json()

        # Memeriksa apakah permintaan berhasil (kode status 200)
        if weather_data["cod"] == 200:
            # Mengambil data cuaca
            main = weather_data["main"]
            wind = weather_data["wind"]
            weather_description = weather_data["weather"][0]["description"]

            # Menyiapkan data untuk disimpan ke CSV
            data = {
                "City": city_name,
                "Temperature": main['temp'],
                "Humidity": main['humidity'],
                "Pressure": main['pressure'],
                "Wind Speed": wind['speed'],
                "Description": weather_description.capitalize(),
                "Date Time": dt.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Menulis baris data ke CSV
            writer.writerow(data)
        else:
            print(f"City {city_name} not found.")
