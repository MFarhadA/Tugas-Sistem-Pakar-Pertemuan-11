# ==============================================================================
# SISTEM PAKAR - CONTOH 1: INFERENSI BERBASIS KONSOL (TERMINAL)
# ==============================================================================
# File ini mendemonstrasikan implementasi dasar dari Sistem Pakar (Expert System)
# menggunakan metode representasi pengetahuan berupa "Rule-Based System" (Sistem Berbasis Aturan)
# dan mekanisme penalaran "Forward Chaining" (Pelacakan ke Depan).
#
# 1. Basis Fakta (Fact Base): Kamus data yang mewakili status pasien saat ini.
# 2. Basis Aturan (Rule Base): Aturan logika IF-THEN dari pakar medis.
# 3. Mesin Inferensi (Inference Engine): Fungsi pencocokan fakta terhadap aturan.
# ==============================================================================

# 1. BASIS FAKTA (FACT BASE)
# Menyimpan data klinis pasien saat ini dalam bentuk dictionary (kamus).
# Kunci (key) mewakili gejala, dan nilai (value) berupa Boolean (True/False).
fakta = {
    "demam": False,
    "batuk": True,
    "ruam_kulit": False
}

# 2. BASIS ATURAN (RULE BASE)
# Kumpulan aturan keputusan medis (IF-THEN) yang dirumuskan oleh seorang pakar.
# - "syarat": Gejala-gejala yang wajib ada (bernilai True) agar aturan terpenuhi.
# - "kesimpulan": Diagnosis penyakit yang ditarik jika seluruh syarat bernilai True.
aturan = [
    {
        "syarat": ["demam", "batuk"],
        "kesimpulan": "influenza"  # JIKA demam=True DAN batuk=True, MAKA kesimpulan=influenza
    },
    {
        "syarat": ["demam", "ruam_kulit"],
        "kesimpulan": "campak"     # JIKA demam=True DAN ruam_kulit=True, MAKA kesimpulan=campak
    }
]

# 3. MESIN INFERENSI (INFERENCE ENGINE)
# Fungsi logis untuk mencocokkan Basis Fakta dengan Basis Aturan guna menarik kesimpulan.
def inferensi(fakta, aturan):
    hasil = []  # List penampung kesimpulan diagnosa yang berhasil ditarik
    for rule in aturan:
        # all() memastikan semua gejala dalam rule["syarat"] memiliki nilai True di Basis Fakta.
        # fakta.get(s, False) digunakan untuk mencari gejala. Jika tidak ditemukan, dianggap False.
        syarat_terpenuhi = all(fakta.get(s, False) for s in rule["syarat"])
        
        # Jika seluruh syarat dalam aturan terpenuhi, simpan kesimpulannya
        if syarat_terpenuhi:
            hasil.append(rule["kesimpulan"])
    return hasil  # Mengembalikan daftar kesimpulan penyakit yang terdeteksi

# 4. EKSEKUSI PROSES INFERENSI
# Memanggil fungsi inferensi dengan parameter 'fakta' dan 'aturan' yang sudah didefinisikan.
diagnosa = inferensi(fakta, aturan)

# 5. FORMAT DAN TAMPILKAN OUTPUT HASIL
# Mengecek apakah daftar hasil diagnosa terisi atau kosong, lalu mencetaknya ke terminal.
if diagnosa:
    print("Kemungkinan diagnosis:")
    for d in diagnosa:
        print(f"- {d}")
else:
    print("Tidak ditemukan diagnosis berdasarkan fakta saat ini.")