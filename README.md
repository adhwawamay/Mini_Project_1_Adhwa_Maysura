# Mini_Project_1_Adhwa_Maysura
Nama : Adhwa Maysura<br>
Nim : 2609116103<br>
kelas : C

# Sistem Kelola Jaringan WiFi Di Fakultas Teknik
Berikut merupakan hasil dari flowchart sistem berdasarkan tema tersebut.

<img width="3767" height="1892" alt="minpro1" src="https://github.com/user-attachments/assets/db602717-eebb-42dd-b262-10763cd6dc99" />

#

Kemudian ini adalah hasil dari sistem yang saya buat melalui python.

<img width="1920" height="503" alt="1 minpro" src="https://github.com/user-attachments/assets/299ebd29-83cb-4f8d-b9fc-433fd3e20204" />

- Pertama sistem membuat sebuah list **jaringan_wifi**, yang di dalamnya sudah terdata 3 jaringan wifi seperti pada gambar tersebut. Setiap jaringan wifi terdiri dari 3 informasi yaitu:
1. Nama WiFi
2. Lokasi
3. Password

- Kemudian sistem akan menampilkan menu utama, sistem menjalankan **while true**, yang artinya menu akan terus ditampilkan berulang-ulang hingga pengguna memilih salah satu dari menu yang tersedia.
- Menu yang ditapilkan adalah:
1. Tambahkan Jaringan WiFi
2. Tampilkan Seluruh Jaringan WiFi
3. Ubah Jaringan WiFi
4. Hapus Jaringan WiFi
5. Keluar Dari Sistem


## Menu 1

<img width="1920" height="338" alt="2 minpro" src="https://github.com/user-attachments/assets/3fc66b20-2cde-49c6-b2b7-fb6abed53553" />

- Jika pengguna memilih menu 1 (Tambahkan Wifi). Kemudian Sistem akan mengarahkan pengguna untuk mengisi:
1. Nama WiFi
2. Lokasi WiFi
3. Password WiFi<br>
Yang nantinya data tersebut disimpan oleh sistem kedalam jaringan_wifi. Setelah berhasil sistem akan menampilkan "Jaringan WiFi berhasil ditambah." lalu kembali ke menu utama.

## Menu 2

<img width="1920" height="357" alt="3 minpro" src="https://github.com/user-attachments/assets/070c4ea2-53c9-4b30-868e-952aedeb3247" />

- Jika pengguna memilih menu ke-2 (Menampilkan Seluruh Jaringan WiFi.), Pertama sistem akan mengecek jumlah data WiFi yang tersimpan, jika tidak ada sistem akan menampilkan "Belum ada data WiFi yang tersimpan.". Setelah seluruh data berhasil ditampilkan sistem akan kembali ke menu utama.

## Menu 3

<img width="960" height="375" alt="4 Minpro" src="https://github.com/user-attachments/assets/36bfb73e-93ee-4b33-96d5-0c5b154bcc27" />

- Jika pengguna memilih menu ke-3 (Ubah Jaringan WiFi.), sistem akan mengecek apakah terdapat data WiFi, jika tidak sistem akan otomatis menampilkan "Belum ada data WiFi yang tersimpan."
- Namun, jika seluruh data ditampilkan. Kemudian pengguna dapat memilih nomor data yang ingin diubah, setelah pengguna memilih data WiFi yang ingin diubah. Sistem akan mengarahkan pengguna untuk memasukkan nama, lokasi, dan password WiFi yang baru. Dan data berhasil diubah. Dan sistem akan kembali ke menu utama.
- Jika nomor data WiFi tidak sesuai, sistem akan mengeluarkan "Nomor data tidak ditemukan.", dan sistem akan langsung kembali ke menu utama.

## Menu 4

<img width="1920" height="492" alt="5 minpro" src="https://github.com/user-attachments/assets/329c3333-45f0-425f-b0cd-8dcd4ee41635" />

- Pada menu ke-4 (Hapus Jaringan WiFi.) sama seperti menu ke-3 (Ubah Jaringan WiFi.). Sistem terlebih dahulu mengecek apakah terdapat data WiFi, jika iya maka sistem akan menampilkan seluruh data WiFi. kemudian pengguna dipersilahkan untuk memilih nomor data WiFi yang ingin dihapus, setelah data WiFi yang pengguna pilih berhasil terhapus, maka sistem akan menampilkan "Data WiFi telah terhapus.", dan sistem akan kembali ke menu utama.
- Kalau nomor yang dipilih tidak tersedia, sistem akan menampilkan "Nomor data tidak ditemukan.". Dan sistem akan kembali ke menu utama.

## Menu 5

<img width="1920" height="218" alt="6 minpro" src="https://github.com/user-attachments/assets/28acc05d-ccc5-4cfa-a50c-9d975f748372" />

- Saat pengguna memilih menu ke-5 (Keluar Dari Sistem.), lalu sistem akan menampilkan "Sistem berhasil dihentikan", kemudian sistem **break** akan dijalan dengan kata lain **break** berfungsi untuk menghentikan perulangan dari **while true**, sehingga menu tidak ditampilkan lagi dan sistem selesai (berakhir)
- Ketika pengguna memasukkan nomor yang tidak terdapat dalam menu, sistem akan menjalankan bagian **else** dan menampilkan "Menu tidak tersedia. Silahkan pilih 1-5." lalu sistem akan kembali ke menu utama.

# Proses saat program dijalankan (Run)
### Menu utama

<img width="542" height="280" alt="1 run" src="https://github.com/user-attachments/assets/5e400bcf-851c-4650-94e3-ae07e23e7acf" />

### Menu ke-1

<img width="537" height="437" alt="2 run" src="https://github.com/user-attachments/assets/fa37fce3-1184-4b85-8b94-4ca8952dca16" />

### Menu ke-2

<img width="611" height="858" alt="3 run" src="https://github.com/user-attachments/assets/44695203-15e5-48ed-a307-915d9e6691c5" />

### Menu ke-3

<img width="649" height="581" alt="4 run" src="https://github.com/user-attachments/assets/97dbbc0d-40c6-41b4-b288-a098eefe7567" />

**Jika pengguna salah input di daftar data WiFi**

<img width="614" height="488" alt="5 run" src="https://github.com/user-attachments/assets/d24ae7c8-de63-46ba-95fd-e6e128f8a824" />

### Menu ke-4

<img width="641" height="491" alt="6 run" src="https://github.com/user-attachments/assets/4e94b94d-fd63-4e67-b020-7bd66c86dd83" />

**Jika pengguna salah input di daftar data WiFi**

<img width="603" height="456" alt="7 run" src="https://github.com/user-attachments/assets/6112b1e5-ae10-4999-b75d-80f6cd6291f1" />

### Menu ke-5

<img width="744" height="351" alt="8 run" src="https://github.com/user-attachments/assets/35f0ed54-7a1b-450b-9a31-a7af2e0f1a69" />

#
Ini adalah hasil dari flowchart & sistem yang saya buat. Terimakasih telah membaca seluruh isi readme ini :D
