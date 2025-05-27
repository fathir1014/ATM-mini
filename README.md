# ATM-mini
# 💸 Aplikasi Keuangan Sederhana (Terminal-Based)

Sebuah aplikasi terminal Python untuk mengelola transaksi keuangan pribadi. Setiap pengguna memiliki akun dengan sistem login dan password, saldo yang bisa bertambah/berkurang, serta riwayat transaksi yang tersimpan secara otomatis dalam file JSON.

##  Fitur

- **Registrasi dan Login**
  - Sistem login multi-akun dengan penyimpanan username dan password.
  
- **Manajemen Saldo**
  - Tambah dan kurangi saldo berdasarkan jenis transaksi (masuk/keluar).
  - Validasi saldo agar tidak bisa minus.

- **Riwayat Transaksi**
  - Semua transaksi disimpan lengkap dengan deskripsi, jumlah, jenis, dan tanggal.
  - Data tersimpan permanen di file `akun.json`.

- **Data Persisten**
  - Semua data disimpan dalam format JSON, tidak hilang saat program ditutup.

