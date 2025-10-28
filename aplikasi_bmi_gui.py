import tkinter as tk
from tkinter import messagebox

# --- Fungsi perhitungan BMI dan saran ---
def hitung_bmi():
    try:
        nama = entry_nama.get()
        gender = var_gender.get()
        umur = int(entry_umur.get())
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get())

        bmi = berat / (tinggi ** 2)

        if bmi < 18.5:
            kategori = "Kurus (Underweight)"
            status = "Kekurangan nutrisi"
            nutrisi = [
                "Protein (telur, ayam, ikan, tahu, tempe)",
                "Karbohidrat kompleks (nasi, roti gandum, kentang, oatmeal)",
                "Lemak sehat (alpukat, kacang, minyak zaitun)",
                "Susu dan produk olahannya untuk menambah kalori sehat"
            ]
            saran = "Konsumsi makanan bergizi seimbang dan makan 4–5 kali sehari dengan porsi cukup."
        elif 18.5 <= bmi < 25:
            kategori = "Normal (Ideal)"
            status = "Nutrisi seimbang"
            nutrisi = [
                "Protein sedang (daging tanpa lemak, tahu, tempe)",
                "Sayur dan buah beragam warna setiap hari",
                "Air putih cukup minimal 8 gelas/hari"
            ]
            saran = "Pertahankan pola makan seimbang dan olahraga 30 menit setiap hari."
        elif 25 <= bmi < 30:
            kategori = "Berat badan berlebih (Overweight)"
            status = "Kelebihan nutrisi"
            nutrisi = [
                "Sayur dan buah tinggi serat (brokoli, apel, wortel)",
                "Protein tanpa lemak (ikan, ayam tanpa kulit, tahu, tempe)",
                "Batasi karbohidrat sederhana (gula, nasi putih berlebih)",
                "Hindari makanan cepat saji dan gorengan"
            ]
            saran = "Kurangi kalori dan tingkatkan aktivitas fisik."
        else:
            kategori = "Obesitas"
            status = "Kelebihan nutrisi berat"
            nutrisi = [
                "Sayuran hijau dan buah segar",
                "Protein rendah lemak (ikan, dada ayam, tahu)",
                "Kurangi makanan manis dan minuman bersoda",
                "Hindari gorengan dan makanan olahan tinggi garam"
            ]
            saran = "Mulai pola hidup sehat dan konsultasikan ke ahli gizi."

        # Tampilkan hasil
        hasil = f"""
Nama: {nama}
Jenis Kelamin: {gender}
Umur: {umur} tahun
BMI: {bmi:.2f}
Kategori: {kategori}
Status Gizi: {status}

Rekomendasi Nutrisi:
- {chr(10) + '- '.join(nutrisi)}

Saran:
{saran}
"""
        messagebox.showinfo("Hasil BMI", hasil)

    except ValueError:
        messagebox.showerror("Error", "Pastikan semua data sudah diisi dengan benar!")

# --- Tampilan GUI ---
root = tk.Tk()
root.title("Aplikasi BMI (Indeks Massa Tubuh)")
root.geometry("400x450")
root.resizable(False, False)

# Label judul
label_title = tk.Label(root, text="Aplikasi BMI (Indeks Massa Tubuh)", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Input Nama
tk.Label(root, text="Nama:").pack(anchor="w", padx=20)
entry_nama = tk.Entry(root, width=40)
entry_nama.pack(padx=20, pady=2)

# Gender
tk.Label(root, text="Jenis Kelamin:").pack(anchor="w", padx=20)
var_gender = tk.StringVar(value="Laki-laki")
frame_gender = tk.Frame(root)
frame_gender.pack(anchor="w", padx=20)
tk.Radiobutton(frame_gender, text="Laki-laki", variable=var_gender, value="Laki-laki").pack(side="left")
tk.Radiobutton(frame_gender, text="Perempuan", variable=var_gender, value="Perempuan").pack(side="left")

# Umur
tk.Label(root, text="Umur (tahun):").pack(anchor="w", padx=20)
entry_umur = tk.Entry(root, width=40)
entry_umur.pack(padx=20, pady=2)

# Berat badan
tk.Label(root, text="Berat Badan (kg):").pack(anchor="w", padx=20)
entry_berat = tk.Entry(root, width=40)
entry_berat.pack(padx=20, pady=2)

# Tinggi badan
tk.Label(root, text="Tinggi Badan (meter):").pack(anchor="w", padx=20)
entry_tinggi = tk.Entry(root, width=40)
entry_tinggi.pack(padx=20, pady=2)

# Tombol Hitung
btn_hitung = tk.Button(root, text="Hitung BMI", command=hitung_bmi, bg="#4CAF50", fg="white", width=15)
btn_hitung.pack(pady=15)

# Label footer
tk.Label(root, text="© 2025 Aplikasi BMI - Dibuat oleh ChatGPT", font=("Arial", 8)).pack(side="bottom", pady=10)

root.mainloop()