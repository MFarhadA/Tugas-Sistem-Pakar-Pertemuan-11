# ==============================================================================
# SISTEM PAKAR - CONTOH 2: INFERENSI BERBASIS ANTARMUKA GRAFIS (GUI TKINTER)
# ==============================================================================
# File ini menggabungkan logika dasar Sistem Pakar (Basis Aturan & Mesin Inferensi)
# dengan GUI sederhana menggunakan library bawaan Python: Tkinter.
#
# Alur Kerja Program:
# 1. Pengguna memilih gejala secara visual melalui Checkbutton di jendela aplikasi.
# 2. Pengguna menekan tombol "Diagnosa" untuk menjalankan pencocokan aturan.
# 3. Aplikasi membaca status setiap Checkbutton, melakukan inferensi forward chaining,
#    dan memperbarui teks hasil diagnosis secara dinamis di dalam aplikasi.
# ==============================================================================

import tkinter as tk

# 1. BASIS ATURAN (RULE BASE)
# Representasi pengetahuan pakar medis menggunakan list dictionary.
aturan = [
    {"syarat": ["Demam", "Batuk"], "kesimpulan": "influenza"},
    {"syarat": ["Demam", "Ruam Kulit"], "kesimpulan": "campak"}
]

# 2. MESIN INFERENSI (INFERENCE ENGINE)
# Fungsi logis untuk memeriksa apakah kombinasi gejala pasien memenuhi syarat dalam aturan.
def inferensi(fakta, aturan):
    hasil = []
    for rule in aturan:
        # Memeriksa apakah semua gejala prasyarat bernilai True di fakta_sekarang
        syarat_terpenuhi = all(fakta.get(s, False) for s in rule["syarat"])
        if syarat_terpenuhi:
            hasil.append(rule["kesimpulan"])
    return hasil

# 3. FUNGSI CALLBACK EVENT (AKSI TOMBOL DIAGNOSA)
# Fungsi ini dipanggil ketika pengguna menekan tombol "Diagnosa".
def tombol_diagnosa():
    # Mengambil fakta medis saat ini langsung dari variabel penampung Checkbutton (True/False)
    fakta_sekarang = {gejala: var.get() for gejala, var in variabel_gejala.items()}
    
    # Melakukan proses penalaran inferensi
    hasil_diagnosa = inferensi(fakta_sekarang, aturan)
    
    # Menghapus output lama pada widget Text (dari baris 1 karakter 0 sampai akhir)
    output_text.delete("1.0", tk.END)
    
    # Menuliskan kembali hasil diagnosa terbaru ke widget Text
    if hasil_diagnosa:
        output_text.insert(tk.END, "Kemungkinan diagnosis:\n")
        for penandis in hasil_diagnosa:
            output_text.insert(tk.END, f"- {penandis}\n")
    else:
        output_text.insert(tk.END, "Tidak ditemukan diagnosis berdasarkan fakta saat ini.")

# 4. --- MEMBUAT WINDOW UTAMA APLIKASI (GUI SETUP) ---
# Menginisialisasi jendela utama aplikasi Tkinter
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit")
root.geometry("400x380")

# Label Judul Pilihan Gejala
label_pilih = tk.Label(root, text="Pilih Gejala!", font=("Arial", 14, "bold"))
# pack() menempatkan widget ke dalam window dengan posisi teratur
label_pilih.pack(anchor="w", padx=20, pady=10)

# 5. PEMBUATAN CHECKBUTTON DINAMIS
# Mendefinisikan daftar gejala klinis yang dapat dipilih oleh pasien
daftar_gejala = ["Demam", "Batuk", "Ruam Kulit"]
# Variabel penampung objek BooleanVar dari Tkinter untuk menyimpan nilai True/False tiap gejala
variabel_gejala = {}

for gejala in daftar_gejala:
    # BooleanVar digunakan Tkinter untuk memantau status aktif/tidak aktif Checkbutton secara langsung
    var = tk.BooleanVar()
    # Membuat komponen Checkbutton secara dinamis
    chk = tk.Checkbutton(root, text=gejala, variable=var, font=("Arial", 11))
    chk.pack(anchor="w", padx=40, pady=2)
    # Menyimpan referensi variabel BooleanVar ke dalam dictionary pencatat gejala
    variabel_gejala[gejala] = var

# 6. TOMBOL SUBMIT DIAGNOSA
# Membuat tombol diagnosa yang akan memicu eksekusi fungsi 'tombol_diagnosa' ketika diklik
btn_diagnosa = tk.Button(root, text="Diagnosa", command=tombol_diagnosa, font=("Arial", 11), bg="#d9d9d9")
btn_diagnosa.pack(pady=15)

# 7. WIDGET HASIL (TEXT BOX OUTPUT)
# Widget Text multi-baris yang digunakan untuk menampilkan hasil evaluasi sistem pakar
output_text = tk.Text(root, height=6, width=45, font=("Arial", 11))
output_text.pack(padx=20, pady=10)

# 8. MENJALANKAN LOOP UTAMA GUI
# Menjaga jendela aplikasi tetap terbuka dan responsif terhadap input pengguna
root.mainloop()