import csv

FILE_NAME = "data_mahasiswa.csv"

# =========================
# 1. Tambah Data Mahasiswa
# =========================
def tambah_data():
    nama = input("Masukkan Nama Mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nama, tugas, uts, uas])

    print("Data berhasil disimpan!\n")

# =========================
# 2. Tampilkan Semua Data
# =========================
def tampilkan_data():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print("\n=== DATA MAHASISWA ===")
            for row in reader:
                print("Nama:", row[0], "| Tugas:", row[1], "| UTS:", row[2], "| UAS:", row[3])
            print()
    except FileNotFoundError:
        print(" File belum ada!\n")

# =========================
# 3. Hitung Rata-rata Nilai
# =========================
def hitung_rata_rata():
    total = 0
    jumlah = 0

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                tugas = float(row[1])
                uts = float(row[2])
                uas = float(row[3])
                rata = (tugas + uts + uas) / 3
                total += rata
                jumlah += 1

        if jumlah > 0:
            print("Rata-rata nilai semua mahasiswa:", total / jumlah, "\n")
        else:
            print("Data kosong!\n")

    except FileNotFoundError:
        print(" File belum ada!\n")

# =========================
# 5. Cari Data Berdasarkan Nama
# =========================
def cari_data():
    cari = input("Masukkan nama mahasiswa yang dicari: ").lower()
    ditemukan = False

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if cari in row[0].lower():
                    print("\nDitemukan:")
                    print("Nama:", row[0])
                    print("Tugas:", row[1])
                    print("UTS:", row[2])
                    print("UAS:", row[3])
                    ditemukan = True

        if not ditemukan:
            print(" Data tidak ditemukan!\n")

    except FileNotFoundError:
        print(" File belum ada!\n")

# =========================
# MENU UTAMA
# =========================
def menu():
    while True:
        print("===== APLIKASI DATA MAHASISWA =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data")
        print("3. Hitung Rata-rata Nilai")
        print("4. Cari Data Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hitung_rata_rata()
        elif pilihan == "4":
            cari_data()
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print(" Pilihan tidak valid!\n")

# Jalankan program
menu()
