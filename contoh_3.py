# ==============================================================================
# SISTEM PAKAR - CONTOH 3: INFERENSI DENGAN ANTARMUKA PREMIUM & VALIDASI INPUT
# ==============================================================================
# File ini merupakan versi tercanggih dari ketiga contoh. Menggabungkan:
# 1. Logika Sistem Pakar (Basis Aturan & Mesin Inferensi).
# 2. GUI sederhana.
# 3. Fitur Validasi Input (Nama Pasien wajib diisi atau default ke Pasien Anonim).
# ==============================================================================

import tkinter as tk

# 1. BASIS ATURAN (RULE BASE)
# Kamus aturan representasi pengetahuan dokter/pakar medis.
aturan = [
    {"syarat": ["Demam", "Batuk"], "kesimpulan": "influenza"},
    {"syarat": ["Demam", "Ruam Kulit"], "kesimpulan": "campak"}
]

# 2. MESIN INFERENSI (INFERENCE ENGINE)
# Melakukan pencocokan gejala terpilih (fakta) dengan aturan IF-THEN.
def inferensi(fakta, aturan):
    hasil = []
    for rule in aturan:
        # Memastikan seluruh gejala prasyarat bernilai True pada pilihan pengguna
        syarat_terpenuhi = all(fakta.get(s, False) for s in rule["syarat"])
        if syarat_terpenuhi:
            hasil.append(rule["kesimpulan"])
    return hasil

# 3. FUNGSI CALLBACK EVENT (AKSI TOMBOL DIAGNOSA DENGAN VALIDASI)
def tombol_diagnosa():
    # .get() mengambil teks dari Entry, .strip() menghapus spasi kosong di awal/akhir
    nama_pasien = entry_nama.get().strip()
    
    # Validasi: Jika nama pasien kosong, berikan nilai default "Pasien Anonim"
    if not nama_pasien:
        nama_pasien = "Pasien Anonim"
        
    # Membaca data gejala dari variabel BooleanVar masing-masing Checkbutton
    fakta_sekarang = {gejala: var.get() for gejala, var in variabel_gejala.items()}
    
    # Melakukan eksekusi inferensi
    hasil_diagnosa = inferensi(fakta_sekarang, aturan)
    
    # Reset/bersihkan isi Text Area sebelum menuliskan hasil baru
    output_text.delete("1.0", tk.END)
    
    # Menuliskan judul dan nama pasien dengan format yang rapi
    output_text.insert(tk.END, f" Hasil Diagnosa\n")
    output_text.insert(tk.END, f" Pasien: {nama_pasien}\n")
    output_text.insert(tk.END, "─" * 45 + "\n")
    
    # Menuliskan daftar penyakit terdeteksi dengan simbol menarik
    if hasil_diagnosa:
        output_text.insert(tk.END, " Kemungkinan diagnosis penyakit:\n\n")
        for penyakit in hasil_diagnosa:
            output_text.insert(tk.END, f"  %+2s {penyakit.upper()}\n" % "🩺")
    else:
        output_text.insert(tk.END, "  Tidak ditemukan diagnosis berdasarkan gejala saat ini.\n")

# 4. --- SETUP JENDELA UTAMA (GUI WINDOW CREATION) ---
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit")
root.geometry("400x530")
root.configure(bg="#f8fafc")

# 5. HEADER BANNER PREMIUM
header_frame = tk.Frame(root, bg="#4f46e5")
header_frame.pack(fill="x", pady=(0, 15))
header_label = tk.Label(
    header_frame, 
    text="🩺 SISTEM PAKAR MEDIS", 
    font=("Segoe UI", 12, "bold"), 
    bg="#4f46e5", 
    fg="#ffffff"
)
header_label.pack(pady=15)

# 6. WIDGET INPUT NAMA PASIEN
label_nama = tk.Label(root, text="Nama Pasien:", font=("Segoe UI", 10, "bold"), bg="#f8fafc", fg="#475569")
label_nama.pack(anchor="w", padx=25, pady=(5, 4))

entry_nama = tk.Entry(
    root, 
    font=("Segoe UI", 11), 
    bg="#ffffff", 
    fg="#1e293b", 
    relief="flat", 
    highlightthickness=1, 
    highlightbackground="#cbd5e1",
    highlightcolor="#4f46e5"
)
entry_nama.pack(fill="x", padx=25, pady=(0, 15), ipady=4)

# 7. WIDGET DAFTAR PILIHAN GEJALA
label_pilih = tk.Label(root, text="Pilih Gejala yang Dirasakan:", font=("Segoe UI", 10, "bold"), bg="#f8fafc", fg="#475569")
label_pilih.pack(anchor="w", padx=25, pady=(5, 5))

daftar_gejala = ["Demam", "Batuk", "Ruam Kulit"]
variabel_gejala = {}

for gejala in daftar_gejala:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(
        root, 
        text=gejala, 
        variable=var, 
        font=("Segoe UI", 11), 
        bg="#f8fafc", 
        activebackground="#f8fafc", 
        fg="#334155", 
        activeforeground="#4f46e5",
        selectcolor="#ffffff"
    )
    chk.pack(anchor="w", padx=35, pady=2)
    variabel_gejala[gejala] = var

# 8. TOMBOL DIAGNOSA DENGAN FLAT DESIGN
btn_diagnosa = tk.Button(
    root, 
    text="Mulai Diagnosa", 
    command=tombol_diagnosa, 
    font=("Segoe UI", 11, "bold"), 
    bg="#4f46e5", 
    fg="#ffffff", 
    activebackground="#4338ca", 
    activeforeground="#ffffff", 
    bd=0, 
    cursor="hand2", 
    relief="flat"
)
btn_diagnosa.pack(fill="x", padx=25, pady=15, ipady=6)

# 9. WIDGET TEXT AREA HASIL DIAGNOSA
output_text = tk.Text(
    root, 
    height=6, 
    font=("Segoe UI", 10), 
    bg="#ffffff", 
    fg="#1e293b", 
    relief="flat", 
    highlightthickness=1, 
    highlightbackground="#e2e8f0",
    padx=10, 
    pady=10
)
output_text.pack(fill="both", expand=True, padx=25, pady=(0, 20))

# 10. LOOP UTAMA APLIKASI
root.mainloop()