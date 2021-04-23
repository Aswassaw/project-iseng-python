import random

#Generateing Number
number = random.randint(1, 10)
benar = False
jumlahbenar = 0

nama = input("Masukkan Nama: ")
print("Halo, Selamat Datang", nama)
print("Saya mempunyai angka antara 0 sampai 10, berapakah angka saya? Kesempatanmu untuk menebak hanya 3 kali.")

while not benar: #Selama benar adalah tidak/false
    try:
        jumlahbenar += 1
        jawab = int(input("Silahkan, masukkan angka tebakan anda: "))

        if jumlahbenar < 3:
            if jawab < number:
                print("Angka terlalu rendah, silahkan coba lagi")
            elif jawab > number:
                print("Angka terlalu tinggi, silahkan coba lagi")
            elif jawab == number:
                print("Selamat, jawaban anda benar")
                benar = True
        else:
            print("Anda Telah Kalah")
            print("Jawaban yang benar adalah", number)
            break

    except Exception as err:
            print("=" * 100)
            print(err)
            print("=" * 100)
