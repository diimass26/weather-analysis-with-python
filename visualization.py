import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari CSV untuk analisis
df = pd.read_csv("weather_data.csv")

# Set gaya seaborn
sns.set(style="whitegrid")

# Membuat visualisasi distribusi suhu dari masing-masing kota
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date Time", y="Temperature", hue="City", data=df, marker="o")
plt.title("Distribusi Suhu dari Masing-Masing Kota")
plt.xlabel("Tanggal dan Waktu")
plt.ylabel("Suhu (°C)")
plt.xticks(rotation=45)  # Memutar label sumbu x agar mudah dibaca
plt.tight_layout()
plt.show()

# Plot frekuensi pola cuaca
plt.figure(figsize=(10, 6))
sns.countplot(x="Description", data=df, palette="viridis", order=df["Description"].value_counts().index)
plt.title("Frekuensi Pola Cuaca")
plt.xlabel("Deskripsi Cuaca")
plt.ylabel("Jumlah")
plt.xticks(rotation=45)
plt.show()