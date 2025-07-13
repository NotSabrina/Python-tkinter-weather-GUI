import requests
import  tkinter as tk
from tkinter import ttk
from datetime import *
import webbrowser
import matplotlib.pyplot as plt

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

        webbrowser.open(f"https://www.google.com/maps?q={garis_lintang},{garis_bujur}")

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

def cek_temperatur_weather_depan():
    key = "b25298676d454e96aae53803242812"  # API dari weatherapi.com
    lokasi_cek = Serlok.get()
    url = f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={lokasi_cek}&days=3"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tiga_hari = data['forecast']['forecastday']

        avg_temp = [hari['day']['avgtemp_c']for hari in tiga_hari]
        hari_ini = datetime.today().date()
        hari = []
        for x in range(1,4):
            besok = hari_ini + timedelta(days=x)
            hari.append(besok.strftime("%A"))
        plt.plot(hari, avg_temp)
        plt.xlabel("Day")
        plt.ylabel("Temperature(Celcius)")
        plt.show()
    else:
        print(f"Gagal mengambil data :{response.status_code}")

def cek_kondisi_weather_depan():
    key = "b25298676d454e96aae53803242812"  # API dari weatherapi.com
    lokasi_cek = Serlok.get()
    url = f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={lokasi_cek}&days=3"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tiga_hari = data['forecast']['forecastday']
        koondisi = [hari['day']['condition']['text']for hari in tiga_hari]
        kondisi.config(text=f"Kondisi :{koondisi}")
    else:
        print(f"Gagal mengambil data :{response.status_code}")

def dark_mode():
    if root["bg"] == "#242424":
        dark = True
        root.config(bg="#ebfaff")
        gambar.config(background="#ebfaff")
        lokasi.config(background="#ebfaff")
        garis_bujur.config(background="#ebfaff")
        garis_lintang.config(background="#ebfaff")
        waktu.config(background="#ebfaff")
        waktu_zona.config(background="#ebfaff")
        temperatur.config(background="#ebfaff")
        kondisi.config(background="#ebfaff")
        label.config(background="#ebfaff")
        teks.config(background="#ebfaff")

        lokasi.config(foreground="#594a8d")
        garis_bujur.config(foreground="#594a8d")
        garis_lintang.config(foreground="#594a8d")
        waktu.config(foreground="#594a8d")
        waktu_zona.config(foreground="#594a8d")
        temperatur.config(foreground="#594a8d")
        kondisi.config(foreground="#594a8d")
        label.config(foreground="#594a8d")
        teks.config(foreground="#594a8d")

        if dark == True:
            dark_mode.config(text="Dark mode")

    elif root["bg"] == "#ebfaff":
        dark = False
        root.config(bg="#242424")
        gambar.config(background="#242424")
        lokasi.config(background="#242424")
        garis_bujur.config(background="#242424")
        garis_lintang.config(background="#242424")
        waktu.config(background="#242424")
        waktu_zona.config(background="#242424")
        temperatur.config(background="#242424")
        kondisi.config(background="#242424")
        label.config(background="#242424")
        teks.config(background="#242424")

        lokasi.config(foreground="white")
        garis_bujur.config(foreground="white")
        garis_lintang.config(foreground="white")
        waktu.config(foreground="white")
        waktu_zona.config(foreground="white")
        temperatur.config(foreground="white")
        kondisi.config(foreground="white")
        label.config(foreground="white")
        teks.config(foreground="white")

        if dark == False:
            dark_mode.config(text="Light mode")

kemaren = datetime.now() - timedelta(days=1)
waktu_kemarin = kemaren.strftime("%Y-%m-%d")

root = tk.Tk()
lebar_layar1= 600
tinggi_layar1= 400
label = tk.Label(root, text="Weather APP", font=("Poppins", 20, "bold"),background="#ebfaff", foreground="#594a8d")
label.pack()

lebar_layar= root.winfo_screenwidth()
tinggi_layar= root.winfo_screenheight()
tengah_x= int(lebar_layar/2 - lebar_layar1/2)
tengah_y= int(tinggi_layar/2 - tinggi_layar1/2)
Serlok= tk.Entry(root,width=30, font="Rubik")
Serlok.pack()

teks = ttk.Label(text="Enter your location", font=("Rubik", 12), background="#ebfaff")
teks.pack()

cek = ttk.Button(root, text="Check weather", command=cek_weather)
cek.pack()

gambar_awan = tk.PhotoImage(file="image/unknown.png", height=180, width=280)
gambar = ttk.Label(root, image=gambar_awan,background="#ebfaff")
gambar.pack()
gambar.place(x=370, y=70)

lokasi = ttk.Label(root, text="Lokasi: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
lokasi.pack()
lokasi.place(x=70,y=70)

garis_lintang = ttk.Label(root, text="Garis lintang: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
garis_lintang.pack()
garis_lintang.place(x=70, y=90)

garis_bujur = ttk.Label(root, text="Garis bujur: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
garis_bujur.pack()
garis_bujur.place(x=70, y=110)

waktu_zona = ttk.Label(root, text="Waktu zona: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
waktu_zona.pack()
waktu_zona.place(x=70, y=130)

waktu = ttk.Label(root, text="Waktu: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
waktu.pack()
waktu.place(x=70, y=150)

temperatur = ttk.Label(root, text="Temperatur: ", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
temperatur.pack()
temperatur.place(x=70, y=170)

kondisi = ttk.Label(root, text="Kondisi :", justify="left", font=("Rubik", 12),background="#ebfaff", foreground="#594a8d")
kondisi.pack()
kondisi.place(x=70, y=215)

tombol_lama = ttk.Button(root, text="Yesterday", command=cek_weather_lama, width=13)
tombol_lama.pack()

dark_mode= ttk.Button(root, text="Dark mode", command=dark_mode, width=13)
dark_mode.pack()

tombol_tuju_hari = ttk.Button(root, text="3 day temperature", command=cek_temperatur_weather_depan, width=17)
tombol_tuju_hari.pack()
tombol_tuju_hari.place(x=70,y=190)

tombol_kondisi = ttk.Button(root, text="3 day condition", command=cek_kondisi_weather_depan, width=17)
tombol_kondisi.pack()
tombol_kondisi.place(x=70,y=235)

root.title("Weather python tkinter")
root.geometry(f"{lebar_layar1}x{tinggi_layar1}+{tengah_x}+{tengah_y}")
root.resizable(False, False)
root.iconbitmap("image/logo_weather.ico")
root.attributes("-topmost", 0)
root.config(bg="#ebfaff")

root.mainloop()
