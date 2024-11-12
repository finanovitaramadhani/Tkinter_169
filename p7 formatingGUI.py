import tkinter as tk  # Mengimpor modul tkinter sebagai tk untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox dari tkinter untuk menampilkan pesan pop-up

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasilprediksi():
    try:
        # Loop melalui setiap entry di dalam entries untuk memvalidasi input
        for entry in entries:
            nilai = int(entry.get())  # Mengambil nilai dari entry dan mengonversi ke integer
            # Memastikan nilai berada dalam rentang 0 sampai 100
            if not (0 <= nilai <= 100):
                # Menghasilkan error jika nilai di luar rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Menampilkan hasil prediksi jika input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan error jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 sampai 100.")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela aplikasi
root.geometry("500x600")  # Mengatur ukuran jendela aplikasi
root.configure(bg="pink")  # Mengatur warna latar belakang jendela

# Membuat label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("times new roman", 16))
judul_label.pack(pady=20)  # Menempatkan label judul dengan padding vertikal 20 piksel

# Membuat frame untuk menampung input nilai mata pelajaran
frame_input = tk.Frame(root, bg="pink")  # Mengatur frame dengan latar belakang yang sama dengan jendela
frame_input.pack(pady=10)  # Menempatkan frame dengan padding vertikal 10 piksel

# List untuk menyimpan setiap entry nilai
entries = []
# Loop untuk membuat label dan entry untuk 10 mata pelajaran
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="pink")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label pada grid
    
    # Membuat entry untuk setiap nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Lebar entry diatur 10 karakter
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry pada grid
    entries.append(entry)  # Menambahkan entry ke dalam list entries

# Membuat tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasilprediksi, font=("Arial", 12))
prediksi_button.pack(pady=30)  # Menempatkan tombol dengan padding vertikal 30 piksel

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="sky blue", bg="pink")
hasil_label.pack(pady=20)  # Menempatkan label hasil dengan padding vertikal 20 piksel

# Menjalankan aplikasi
root.mainloop()
