import sqlite3
from datetime import datetime

# ==========================================
# KONEKSI DATABASE
# ==========================================

koneksi = sqlite3.connect("data_penduduk.db")
cursor = koneksi.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS penduduk (
    nik TEXT PRIMARY KEY,
    nama TEXT NOT NULL,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    jenis_kelamin TEXT,
    alamat TEXT,
    rt_rw TEXT,
    kelurahan TEXT,
    kecamatan TEXT,
    agama TEXT,
    status_perkawinan TEXT,
    pekerjaan TEXT,
    kewarganegaraan TEXT
)
""")
koneksi.commit()

kolom_data = [
    ("nama", "Nama lengkap"),
    ("tempat_lahir", "Tempat lahir"),
    ("tanggal_lahir", "Tanggal lahir (YYYY-MM-DD)"),
    ("jenis_kelamin", "Jenis kelamin (Laki-laki/Perempuan)"),
    ("alamat", "Alamat"),
    ("rt_rw", "RT/RW"),
    ("kelurahan", "Kelurahan/Desa"),
    ("kecamatan", "Kecamatan"),
    ("agama", "Agama"),
    ("status_perkawinan", "Status perkawinan"),
    ("pekerjaan", "Pekerjaan"),
    ("kewarganegaraan", "Kewarganegaraan")
]


# ==========================================
# 1. REGISTRASI DATA PENDUDUK
# ==========================================

def registrasi():
    print("\n========== REGISTRASI PENDUDUK ==========")

    nik = input("NIK (16 digit): ").strip()

    if not nik.isdigit() or len(nik) != 16:
        print("NIK harus terdiri dari 16 digit angka!")
        return

    cursor.execute(
        "SELECT nik FROM penduduk WHERE nik = ?", (nik,)
    )

    if cursor.fetchone():
        print("NIK sudah terdaftar! Gunakan NIK berbeda.")
        return

    data = []

    for kolom, label in kolom_data:
        nilai = input(label + ": ").strip()

        if kolom == "nama" and not nilai:
            print("Nama wajib diisi!")
            return

        if kolom == "tanggal_lahir" and nilai:
            try:
                datetime.strptime(nilai, "%Y-%m-%d")
            except ValueError:
                print("Tanggal harus berformat YYYY-MM-DD!")
                return

        if kolom == "jenis_kelamin":
            if nilai not in ["Laki-laki", "Perempuan"]:
                print("Masukkan Laki-laki atau Perempuan!")
                return

        data.append(nilai)

    try:
        cursor.execute("""
            INSERT INTO penduduk (
                nik, nama, tempat_lahir, tanggal_lahir,
                jenis_kelamin, alamat, rt_rw, kelurahan,
                kecamatan, agama, status_perkawinan,
                pekerjaan, kewarganegaraan
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nik, *data))

        koneksi.commit()
        print("\nBERHASIL! Data penduduk telah disimpan.")

    except sqlite3.Error as e:
        print("Gagal menyimpan data:", e)


# ==========================================
# 2. MENAMPILKAN SEMUA DATA
# ==========================================

def tampilkan_data():
    cursor.execute("SELECT * FROM penduduk ORDER BY nama")
    semua_data = cursor.fetchall()

    print("\n========== DAFTAR DATA PENDUDUK ==========")

    if not semua_data:
        print("Belum ada data penduduk.")
        return

    labels = ["NIK"] + [item[1] for item in kolom_data]

    for nomor, data in enumerate(semua_data, start=1):
        print(f"\nDATA PENDUDUK KE-{nomor}")
        print("-" * 40)

        for label, nilai in zip(labels, data):
            print(f"{label:28}: {nilai}")

    print(f"\nTotal data penduduk: {len(semua_data)}")


# ==========================================
# 3. MENCARI DATA BERDASARKAN NIK
# ==========================================

def cari_data():
    print("\n========== CARI DATA PENDUDUK ==========")
    nik = input("Masukkan NIK yang dicari: ").strip()

    cursor.execute(
        "SELECT * FROM penduduk WHERE nik = ?", (nik,)
    )
    data = cursor.fetchone()

    if data:
        labels = ["NIK"] + [item[1] for item in kolom_data]

        print("\nDATA DITEMUKAN")
        print("-" * 40)

        for label, nilai in zip(labels, data):
            print(f"{label:28}: {nilai}")
    else:
        print("Data penduduk tidak ditemukan.")


# ==========================================
# 4. EDIT DATA PENDUDUK
# ==========================================

def edit_data():
    print("\n========== EDIT DATA PENDUDUK ==========")
    nik = input("Masukkan NIK yang akan diedit: ").strip()

    cursor.execute(
        "SELECT * FROM penduduk WHERE nik = ?", (nik,)
    )
    data_lama = cursor.fetchone()

    if not data_lama:
        print("Data penduduk tidak ditemukan!")
        return

    print("\nKosongkan input jika data tidak ingin diubah.")

    data_baru = list(data_lama[1:])

    for i, (kolom, label) in enumerate(kolom_data):
        nilai_lama = data_lama[i + 1]
        nilai = input(f"{label} [{nilai_lama}]: ").strip()

        if not nilai:
            continue

        if kolom == "tanggal_lahir":
            try:
                datetime.strptime(nilai, "%Y-%m-%d")
            except ValueError:
                print("Format tanggal salah! Edit dibatalkan.")
                return

        if kolom == "jenis_kelamin":
            if nilai not in ["Laki-laki", "Perempuan"]:
                print("Jenis kelamin tidak valid! Edit dibatalkan.")
                return

        data_baru[i] = nilai

    if not data_baru[0].strip():
        print("Nama wajib diisi!")
        return

    try:
        cursor.execute("""
            UPDATE penduduk SET
                nama = ?, tempat_lahir = ?, tanggal_lahir = ?,
                jenis_kelamin = ?, alamat = ?, rt_rw = ?,
                kelurahan = ?, kecamatan = ?, agama = ?,
                status_perkawinan = ?, pekerjaan = ?,
                kewarganegaraan = ?
            WHERE nik = ?
        """, (*data_baru, nik))

        koneksi.commit()
        print("Data penduduk berhasil diperbarui!")

    except sqlite3.Error as e:
        print("Gagal mengedit data:", e)


# ==========================================
# 5. HAPUS DATA PENDUDUK
# ==========================================

def hapus_data():
    print("\n========== HAPUS DATA PENDUDUK ==========")
    nik = input("Masukkan NIK yang akan dihapus: ").strip()

    cursor.execute(
        "SELECT nama FROM penduduk WHERE nik = ?", (nik,)
    )
    data = cursor.fetchone()

    if not data:
        print("Data penduduk tidak ditemukan!")
        return

    print("\nData yang akan dihapus:")
    print("NIK  :", nik)
    print("Nama :", data[0])

    konfirmasi = input(
        "Yakin menghapus data ini? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":
        cursor.execute(
            "DELETE FROM penduduk WHERE nik = ?", (nik,)
        )
        koneksi.commit()
        print("Data berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


# ==========================================
# 6. MENU UTAMA
# ==========================================

def menu():
    while True:
        print("\n")
        print("=" * 46)
        print("       SISTEM REGISTRASI DATA PENDUDUK")
        print("=" * 46)
        print("1. Registrasi data penduduk")
        print("2. Tampilkan semua data")
        print("3. Cari data penduduk")
        print("4. Edit data penduduk")
        print("5. Hapus data penduduk")
        print("6. Keluar")
        print("=" * 46)

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            edit_data()
        elif pilihan == "5":
            hapus_data()
        elif pilihan == "6":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Pilih menu 1 sampai 6.")


# ==========================================
# MENJALANKAN PROGRAM
# ==========================================

if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")
    finally:
        koneksi.close()
