import random
import webbrowser
import os
# File untuk menyimpan jumlah pemakaian
counter_file = os.path.expanduser("~/.hadiah")

# Jika file belum ada, buat dengan nilai 0
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as file:
        file.write("0")

# Ambil nilai counter
with open(counter_file, 'r') as file:
    counter = int(file.read())

# Periksa apakah sudah digunakan 3 kali
if counter >= 1:
    print("Script ini sudah digunakan")
    exit()

# Tambah counter dan simpan kembali
counter += 1
with open(counter_file, 'w') as file:
    file.write(str(counter))

# Tambahkan perintah script kamu di bawah ini
# Persentase keberhasilan
success_rate = 0.005  # 0.5%

# Jumlah total pilihan (1-1000)
total_choices = 1000

# Hitung berapa banyak nomor yang bisa benar dengan 0.5% peluang
number_of_successful_choices = int(total_choices * success_rate)

# Pilihan nomor benar diambil secara acak dari 1 hingga 1000
correct_choices = random.sample(range(1, total_choices + 1), number_of_successful_choices)

print("⟩ Welkom ⟨")
print("Pilih nomor 1-1000, nilai kesuksesan 0.5 ")

# Membaca pilihan pengguna
user_choice = int(input("Pilih nomor (1-1000): "))

# Memeriksa apakah pilihan pengguna benar
if user_choice in correct_choices:
    print("Selamat! Kamu berhasil!")
    bonus_text = "AKU%20BERHASIL%20BANG%20WEKWEKWEKWEKXUXUXUXXUXUXU8292OAKXIKJDJ022XZXOE013"
    
    # Membuat link WhatsApp dengan teks otomatis
    url = f"https://wa.me/6283841852697?text={bonus_text}"
    
    # Membuka link WhatsApp di browser
    webbrowser.open(url)
else:
    print(f"SALAH! Kamu memilih nomor {user_choice}. Coba lagi lain kali!")