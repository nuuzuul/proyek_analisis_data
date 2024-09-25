import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
#day_data = pd.read_csv("day.csv")
#hour_data = pd.read_csv("hour.csv")
day_data = pd.read_csv("dashboard/day.csv")
hour_data = pd.read_csv("dashboard/hour.csv")

# Menampilkan informasi tentang data
st.title("Dashboard Penyewaan Sepeda")

# Menampilkan ringkasan data harian
st.write("## Informasi Data Harian")
st.write(day_data.describe())

# Menampilkan ringkasan data jam
st.write("## Informasi Data Jam")
st.write(hour_data.describe())

# Menampilkan jumlah duplikasi
st.write("Jumlah duplikasi dalam data jam:", hour_data.duplicated().sum())
st.write("Jumlah duplikasi dalam data hari:", day_data.duplicated().sum())

# Mengubah kolom tanggal menjadi tipe data datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Menghitung rata-rata penyewaan sepeda berdasarkan musim
rata_rata_musim = hour_data.groupby('season')['cnt'].mean()

# Menghitung rata-rata penyewaan sepeda berdasarkan hari
day_data['day_of_week'] = day_data['dteday'].dt.day_name()
rata_rata_hari = day_data.groupby('day_of_week')['cnt'].mean()

# Menampilkan Grafik Rata-rata Penyewaan Sepeda per Musim
st.write("## Rata-rata Penyewaan Sepeda per Musim")
fig1, ax1 = plt.subplots()
rata_rata_musim.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-rata Penyewaan Sepeda')
ax1.set_title('Rata-rata Penyewaan Sepeda per Musim')
ax1.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'], rotation=0)
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Menambahkan grid horizontal
st.pyplot(fig1)

# Menampilkan Grafik Rata-rata Penyewaan Sepeda per Hari
st.write("## Rata-rata Penyewaan Sepeda per Hari")
fig2, ax2 = plt.subplots()
ax2.bar(rata_rata_hari.index, rata_rata_hari, color='salmon', edgecolor='black')
ax2.set_xlabel('Hari dalam Seminggu')
ax2.set_ylabel('Rata-rata Penyewaan Sepeda')
ax2.set_title('Rata-rata Penyewaan Sepeda per Hari')
ax2.set_xticklabels(rata_rata_hari.index, rotation=45)
ax2.grid(axis='y', linestyle='--', alpha=0.7)  # Menambahkan grid horizontal
st.pyplot(fig2)
