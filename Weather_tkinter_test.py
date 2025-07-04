import requests
import  tkinter as tk
from tkinter import ttk
from datetime import *

def cek_weather():
    key = "b25298676d454e96aae53803242812"  # API dari weatherapi.com
    lokasi_cek = Serlok.get()
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={lokasi_cek}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        Lokasi = f"{data['location']['name']}"
        Garis_lintang = f"{data['location']['lat']}"
        Garis_bujur = f"{data['location']['lon']}"
        Waktu_zona = f"{data['location']['tz_id']}"
        Waktu = f"{data['location']['localtime']}"
        Temperatur = f" {data['current']['temp_c']}°C"
        Kondisi = f" {data['current']['condition']['text']}"

        lokasi.config(text=f"Lokasi: {Lokasi}")
        garis_lintang.config(text=f"Garis lintang: {Garis_lintang}")
        garis_bujur.config(text=f"Garis bujur: {Garis_bujur}")
        waktu_zona.config(text=f"Waktu zona: {Waktu_zona}")
        waktu.config(text=f"Waktu: {Waktu}")
        temperatur.config(text=f"Temperatur: {Temperatur}")
        kondisi.config(text=f"Kondisi: {Kondisi}")

        if "Partly cloudy" in Kondisi:
            gambar_awan.config(file="image/partly_cloudy.png")
        elif "Partly Cloudy" in Kondisi:
            gambar_awan.config(file="image/partly_cloudy.png")
        elif "Sunny" in Kondisi:
            gambar_awan.config(file="image/sunny.png")
        elif "Patchy rain nearby" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Light Rain" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Fog" in Kondisi:
            gambar_awan.config(file="image/fog.png")
        elif "Foggy" in Kondisi:
            gambar_awan.config(file="image/fog.png")
        elif "Overcast" in Kondisi:
            gambar_awan.config(file="image/overcast.png")
        elif "Storm" in Kondisi:
            gambar_awan.config(file="image/storm.png")
        elif "Heavy Rain" in Kondisi:
            gambar_awan.config(file="image/heavy_rain.png")
        elif "Moderate Rain" in Kondisi:
            gambar_awan.config(file="image/heavy_rain.png")
        elif "Sleet" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Light rain shower" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        else:
            gambar_awan.config(file="image/unknown.png")
    else:
        print("Gagal mengambil data")

def cek_weather_lama():
    key = "b25298676d454e96aae53803242812"  # API dari weatherapi.com
    lokasi_cek = Serlok.get()
    url = f"http://api.weatherapi.com/v1/history.json?key={key}&q={lokasi_cek}&dt={waktu_kemarin}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        Lokasi = f"{data['location']['name']}"
        Garis_lintang = f"{data['location']['lat']}"
        Garis_bujur = f"{data['location']['lon']}"
        Waktu_zona = f"{data['location']['tz_id']}"
        Waktu = f"{data['location']['localtime']}"
        Temperatur = f" {data['forecast']["forecastday"][0]["day"]['avgtemp_c']}°C"
        Kondisi = f" {data['forecast']["forecastday"][0]["day"]['condition']['text']}"

        lokasi.config(text=f"Lokasi: {Lokasi}")
        garis_lintang.config(text=f"Garis lintang: {Garis_lintang}")
        garis_bujur.config(text=f"Garis bujur: {Garis_bujur}")
        waktu_zona.config(text=f"Waktu zona: {Waktu_zona}")
        waktu.config(text=f"Waktu: {Waktu}")
        temperatur.config(text=f"Temperatur: {Temperatur}")
        kondisi.config(text=f"Kondisi: {Kondisi}")

        if "Partly cloudy" in Kondisi:
            gambar_awan.config(file="image/partly_cloudy.png")
        elif "Partly Cloudy" in Kondisi:
            gambar_awan.config(file="image/partly_cloudy.png")
        elif "Sunny" in Kondisi:
            gambar_awan.config(file="image/sunny.png")
        elif "Patchy rain nearby" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Light Rain" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Fog" in Kondisi:
            gambar_awan.config(file="image/fog.png")
        elif "Foggy" in Kondisi:
            gambar_awan.config(file="image/fog.png")
        elif "Overcast" in Kondisi:
            gambar_awan.config(file="image/overcast.png")
        elif "Storm" in Kondisi:
            gambar_awan.config(file="image/storm.png")
        elif "Heavy Rain" in Kondisi:
            gambar_awan.config(file="image/heavy_rain.png")
        elif "Moderate Rain" in Kondisi:
            gambar_awan.config(file="image/heavy_rain.png")
        elif "Sleet" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        elif "Light rain shower" in Kondisi:
            gambar_awan.config(file="image/light_rain.png")
        else:
            gambar_awan.config(file="image/unknown.png")
    else:
        print("Gagal mengambil data")

kemaren = datetime.now() - timedelta(days=1)
waktu_kemarin = kemaren.strftime("%Y-%m-%d")

root = tk.Tk()

lebar_layar1= 600
tinggi_layar1= 400
label = tk.Label(root, text="Weather APP", font=("Helvetica", 14))
label.pack()
lebar_layar= root.winfo_screenwidth()
tinggi_layar= root.winfo_screenheight()
tengah_x= int(lebar_layar/2 - lebar_layar1/2)
tengah_y= int(tinggi_layar/2 - tinggi_layar1/2)
Serlok= tk.Entry(root)
Serlok.pack()
ttk.Button(root, text="Check weather", command=cek_weather).pack()

gambar_awan = tk.PhotoImage(file="image/unknown.png", height=180, width=280)
gambar = ttk.Label(root, image=gambar_awan)
gambar.pack()
gambar.place(x=370, y=70)

lokasi = ttk.Label(root, text="Lokasi: ", justify="left", font=("Roboto", 12))
lokasi.pack()
lokasi.place(x=100,y=70)

garis_lintang = ttk.Label(root, text="Garis lintang: ", justify="left", font=("Roboto", 12))
garis_lintang.pack()
garis_lintang.place(x=100, y=90)

garis_bujur = ttk.Label(root, text="Garis bujur: ", justify="left", font=("Roboto", 12))
garis_bujur.pack()
garis_bujur.place(x=100, y=110)

waktu_zona = ttk.Label(root, text="Waktu zona: ", justify="left", font=("Roboto", 12))
waktu_zona.pack()
waktu_zona.place(x=100, y=130)

waktu = ttk.Label(root, text="Waktu: ", justify="left", font=("Roboto", 12))
waktu.pack()
waktu.place(x=100, y=150)

temperatur = ttk.Label(root, text="Temperatur: ", justify="left", font=("Roboto", 12))
temperatur.pack()
temperatur.place(x=100, y=170)

kondisi = ttk.Label(root, text="Kondisi :", justify="left", font=("Roboto", 12))
kondisi.pack()
kondisi.place(x=100, y=190)

tombol_lama = ttk.Button(root, text="Yesterday", command=cek_weather_lama)
tombol_lama.pack()

root.title("Weather python tkinter")
root.geometry(f"{lebar_layar1}x{tinggi_layar1}+{tengah_x}+{tengah_y}")
root.resizable(False, False)
root.iconbitmap("image/logo_weather.ico")
root.attributes("-topmost", 1)
root.mainloop()
