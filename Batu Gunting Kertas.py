import random

whi1 = True

while whi1 is True:

    try:
        print("Selamat Datang Di Game Batu, Gunting, Kertas!")
        pilihanAwal = int(input("Apakah Kau Ingin Langsung Bermain?\n1. Mulai Permainan\n2. Tentang Game\n3. Keluar\nPilihan: "))

        whi2 = True

        while whi2 is True:

            if pilihanAwal == 1:

                print("=" * 100)

                def fungsibgk(pilihan):
                    komputer = random.choice(["Batu", "Gunting", "Kertas"])

                    if pilihan == 1:
                        print("Anda Memilih Batu")
                        print("Komputer Memilih", komputer)
                        if komputer == "Batu":
                            print("Seimbang")
                        elif komputer == "Gunting":
                            print("Kau Menang")
                        elif komputer == "Kertas":
                            print("Kau Kalah")

                    elif pilihan == 2:
                        print("Anda Memilih Gunting")
                        print("Komputer Memilih", komputer)
                        if komputer == "Gunting":
                            print("Seimbang")
                        elif komputer == "Kertas":
                            print("Kau Menang")
                        elif komputer == "Batu":
                            print("Kau Kalah")

                    elif pilihan == 3:
                        print("Anda Memilih Kertas")
                        print("Komputer Memilih", komputer)
                        if komputer == "Kertas":
                            print("Seimbang")
                        elif komputer == "Batu":
                            print("Kau Menang")
                        elif komputer == "Gunting":
                            print("Kau Kalah")

                    else:
                        print("Maaf, Pilihan Anda Tidak Ada Dalam Daftar")

                pilihan = int(input("Masukkan Pilihan Anda: \n1. Batu\n2. Gunting\n3. Kertas\nPilihan: "))
                print("=" * 100)

                fungsibgk(pilihan)

            elif pilihanAwal == 2:
                print("=" * 100)
                print("Created By Aswassaw227\nBuild In Python 3.6")
                print("=" * 100)
                break

            elif pilihanAwal == 3:
                print("=" * 100)
                print("Terima Kasih Karena Telah Bermain, Semoga Harimu Menyenangkan")
                print("=" * 100)
                exit()

            else:
                print("=" * 100)
                print("Maaf, Pilihan Anda Tidak Ada Dalam Daftar")
                print("=" * 100)
                break

    except Exception as err:
            print("=" * 100)
            print(err)
            print("=" * 100)