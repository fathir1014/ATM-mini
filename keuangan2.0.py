import json
import datetime

DATA_FILE = "akun.json"
akun_aktif = None
data_semua_akun = {}

# -------------------------------
# Bagian Login dan Register
# -------------------------------

def load_data():
    global data_semua_akun
    try:
        with open(DATA_FILE, "r") as file:
            data_semua_akun = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data_semua_akun = {}

def simpan_data():
    with open(DATA_FILE, "w") as file:
        json.dump(data_semua_akun, file, indent=4)

def register():
    username = input("Buat username baru: ").strip()
    if username in data_semua_akun:
        print("❌ Username sudah digunakan!")
        return None
    password = input("Buat password: ").strip()
    data_semua_akun[username] = {
        "password": password,
        "saldo": 0,
        "transaksi": []
    }
    simpan_data()
    print("✅ Registrasi berhasil!")
    return username

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    akun = data_semua_akun.get(username)
    if akun and akun["password"] == password:
        print(f"✅ Login berhasil! Selamat datang, {username}!")
        return username
    else:
        print("❌ Username atau password salah!")
        return None

# -------------------------------
# Bagian Transaksi
# -------------------------------

def tambah_saldo():
    akun = data_semua_akun[akun_aktif]
    jenis = input("Jenis (masuk/keluar): ").strip()
    deskripsi = input("Deskripsi: ").strip()
    
    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("❌ Input jumlah tidak valid!")
        return

    if jenis == "masuk":
        akun["saldo"] += jumlah
    elif jenis == "keluar":
        if jumlah > akun["saldo"]:
            print("❌ Saldo tidak mencukupi!")
            return
        akun["saldo"] -= jumlah
    else:
        print("❌ Jenis transaksi tidak dikenal!")
        return

    transaksi = {
        "jenis": jenis,
        "deskripsi": deskripsi,
        "jumlah": jumlah,
        "tanggal": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    akun["transaksi"].append(transaksi)
    simpan_data()
    print("✅ Transaksi berhasil!")

def tampilkan_transaksi():
    akun = data_semua_akun[akun_aktif]
    print("\n=== RIWAYAT TRANSAKSI ===")
    for i, tr in enumerate(akun["transaksi"], 1):
        print(f"{i}. [{tr['tanggal']}] {tr['jenis']} - {tr['deskripsi']} - Rp{tr['jumlah']}")
    print(f"Saldo akhir: Rp{akun['saldo']}")

def lihat_saldo():
    saldo = data_semua_akun[akun_aktif]["saldo"]
    print(f"💰 Saldo anda: Rp{saldo}")

# -------------------------------
# Menu Utama
# -------------------------------

def menu_transaksi():
    while True:
        print("\n1. Tambah Transaksi")
        print("2. Lihat Riwayat Transaksi")
        print("3. Cek Saldo")
        print("4. Logout")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_saldo()
        elif pilihan == "2":
            tampilkan_transaksi()
        elif pilihan == "3":
            lihat_saldo()
        elif pilihan == "4":
            print("Logout berhasil. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid!")

# -------------------------------
# Jalankan Program
# -------------------------------

def main():
    global akun_aktif
    load_data()
    while True:
        print("\n===== SISTEM KEUANGAN LOGIN =====")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            akun = login()
            if akun:
                akun_aktif = akun
                menu_transaksi()
        elif pilihan == "2":
            akun = register()
            if akun:
                akun_aktif = akun
                menu_transaksi()
        elif pilihan == "3":
            print("Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid!")

main()
