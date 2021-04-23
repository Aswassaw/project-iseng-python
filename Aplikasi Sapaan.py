from datetime import datetime

nama = input("Masukkan Namamu: ")

jam = datetime.now().hour

if jam < 10:
    sapaan = "Selamat Pagi"
elif 10 < jam < 1:
    sapaan = "Selamat Siang"
elif 15 < jam < 18:
    sapaan = "Selamat Sore"
elif 18 < jam <= 24:
    sapaan = "Selamat Malam"

print("Halo,", sapaan, nama)