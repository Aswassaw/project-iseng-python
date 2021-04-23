#Project Kalkulator Sederhana

#Fungsi Penjumlahan
def penjumlahan(nilai1=0, nilai2=0):
    hasil=nilai1+nilai2
    print("Hasil Penjumlahan Dari", a, "+", b, "Adalah", hasil)
    return hasil

#Fungsi Pengurangan
def pengurangan(nilai1=0, nilai2=0):
    hasil=nilai1-nilai2
    print("Hasil Pengurangan Dari", a, "-", b, "Adalah", hasil)
    return hasil

#Fungsi Perkalian
def perkalian(nilai1=0, nilai2=0):
    hasil=nilai1*nilai2
    print("Hasil Perkalian Dari", a, "*", b, "Adalah", hasil)
    return hasil

#Fungsi Pembagian
def pembagian(nilai1=0, nilai2=0):
    hasil=nilai1/nilai2
    print("Hasil Pembagian Dari", a, "/", b, "Adalah", hasil)
    return hasil

print("Selamat Datang Di Program Kalkulator Yang Sangat Sederhana Ini")

while1 = 2
while2 = 2

while while1 is while2:

    try:
        pilihan=int(input("Silahkan Pilih Metode Perhitungan Anda:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Keluar Dari Program\nPilihan: "))

        print("="*100)

        if pilihan == 1:
            print("Anda Telah Memilih Fungsi Penjumlahan\n")
        elif pilihan == 2:
            print("Anda Telah Memilih Fungsi Pengurangan\n")
        elif pilihan == 3:
            print("Anda Telah Memilih Fungsi Perkalian\n")
        elif pilihan == 4:
            print("Anda Telah Memilih Fungsi Pembagian\n")

    except Exception as err:
        print("=" * 100)
        print(err)

    if pilihan == 1 or pilihan == 2 or pilihan == 3 or pilihan == 4:
        try:
            a=int(input("Masukkan Nilai Pertama: "))
            b=int(input("Masukkan Nilai Kedua: "))

            print("=" * 100)

            if pilihan == 1:
                penjumlahan(a,b)
            elif pilihan == 2:
                pengurangan(a,b)
            elif pilihan == 3:
                perkalian(a,b)
            elif pilihan == 4:
                pembagian(a,b)

        except Exception as err:
            print("=" * 100)
            print(err)

    elif pilihan == 5:
        print("Sampai Berjumpa Kembali! Terima Kasih Telah Berkunjung.")
        exit()
    else:
        print("Maaf, Pilihan Anda Tidak Tersedia Pada Daftar Fungsi Di Aplikasi Ini")

    print("="*100)
    try:
        pilihan2 = int(input("Apakah Anda Ingin Menghitung Lagi?\n1. Ya, Berhitung Lagi\n2. Tidak, Aku Ingin Keluar Saja\nPilihan: "))

        if pilihan2 == 1:
            print("Selamat Datang Kembali\n")
        elif pilihan2 == 2:
            print("Sampai Berjumpa Kembali! Terima Kasih Telah Berkunjung.")
            exit()
        else:
            print("Maaf, Pilihan Anda Tidak Tersedia Pada Daftar Fungsi Di Aplikasi Ini")
            print("="*100)

    except Exception as err:
            print("=" * 100)
            print(err)

    print("="*100)