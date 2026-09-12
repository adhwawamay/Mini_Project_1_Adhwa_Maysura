jaringan_wifi = [
    ["WiFi Gedung C", "Gedung C", "Teknikunmul"],
    ["WiFi Lab Komputer", "Lab Komputer", "123456789"],
    ["WiFi Perpustakaan", "Perpustakaan", "Perpus.bersama"]
]

while True:
    print("SELAMAT DATANG")
    print("DI SISTEM DATA JARINGAN WIFI DI GEDUNG TEKNIK\n")
    print("1. Tambahkan Jaringan WiFi")
    print("2. Tampilkan Seluruh Jaringan WiFi")
    print("3. Ubah Jaringan WiFi")
    print("4. Hapus Jaringan WiFi")
    print("5. Keluar Dari Sistem")

    memilih_opsi = input("Pilih menu (1-5): ")
    
    if memilih_opsi == "1":
        print("\n TAMBAHKAN JARINGAN BARU")

        nama = input("Masukkan nama WiFi: ")
        lokasi = input("Masukkan lokasi WiFi: ")
        password = input("Masukkan password WiFi: ")

        data_baru = [nama, lokasi, password]
        jaringan_wifi.append(data_baru)

        print("Jaringan WiFi berhasil ditambahkan.")

    elif memilih_opsi == "2":
        print("\n DAFTAR JARINGAN WIFI YANG TERSIMPAN ")

        if len(jaringan_wifi) == 0:
            print("Belum ada data WiFi yang tersimpan.")
        else:
            for i, wifi in enumerate(jaringan_wifi, start=1):
                print(f"\nData ke-{i}")
                print(f"Nama WiFi : {wifi[0]}")
                print(f"Lokasi    : {wifi[1]}")
                print(f"Password  : {wifi[2]}")

    elif memilih_opsi == "3":
        print("\n UBAH DATA WIFI ")

        if len(jaringan_wifi) == 0:
            print("Belum ada data WiFi yang tersimpan.")
        else:
            for i, wifi in enumerate(jaringan_wifi, start=1):
                print(f"{i}. {wifi[0]} - {wifi[1]} - {wifi[2]}")

            nomor = int(input("Silahkan memilih jaringan wifi yang ingin diubah: "))

            if nomor >= 1 and nomor <= len(jaringan_wifi):
                nama_baru = input("Masukkan nama WiFi baru: ")
                lokasi_baru = input("Masukkan lokasi baru: ")
                password_baru = input("Masukkan password baru: ")

                jaringan_wifi[nomor - 1] = [
                    nama_baru,
                    lokasi_baru,
                    password_baru
                ]

                print("Data WiFi berhasil diubah.")
            else:
                print("Nomor data tidak ditemukan.")

    elif memilih_opsi == "4":
        print("\n HAPUS DATA WIFI ")

        if len(jaringan_wifi) == 0:
            print("Belum ada data WiFi yang tersimpan.")
        else:
            for i, wifi in enumerate(jaringan_wifi, start=1):
                print(f"{i}. {wifi[0]} - {wifi[1]} - {wifi[2]}")

            nomor = int(input("Silahkan memilih jaringan wifi yang ingin dihapus: "))

            if nomor >= 1 and nomor <= len(jaringan_wifi):
                jaringan_wifi.pop(nomor - 1)
                print("Data WiFi telah dihapus.")
            else:
                print("Nomor data tidak ditemukan.")

    elif memilih_opsi == "5":
        print("\nSistem berhasil dihentikan.")
        break

    else:
        print("\nMenu tidak tersedia. Silakan pilih 1-5.")