import tkinter as tk
import sqlite3
from tkinter import messagebox

# Connect Database
conn = sqlite3.connect("databaseSiswa.db")
cursore = conn.cursor()

# Membuat Table jika Table belum di buat
cursore.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER,
                    inggris INTEGER,
                    prediksi_fakultas TEXT)''')

# Buat fungsi untuk menambahkan nilai ke tabel nilai_siswa
def tambah_nilai():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Menghitung nilai prediksi
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = 'Teknik'
    else:
        prediksi_fakultas = 'Bahasa'

    # Menambahkan nilai ke tabel nilai_siswa
    cursore.execute("INSERT INTO hasil_prediksi (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)", (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    conn.commit()



# Buat Jendela Halaman
root = tk.Tk()
root.title("Prediksi Prodi Pilihan")
root.geometry("500x500")
root.resizable(False,False)

# Label Judul
label_judul = tk.Label(root, text="Prediksi Prodi Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()


# Label Nama siswa
label_nama = tk.Label(frame_input, text="Nama Siswa")
label_nama.grid(row=0, column=0, pady=10)
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=0,column=1)

# Label Nilai Biologi
label_biologi = tk.Label(frame_input, text="Nilai Biologi")
label_biologi.grid(row=1, column=0, pady=10)
entry_biologi = tk.Entry(frame_input)
entry_biologi.grid(row=1,column=1)

# Label Nilai Fisika
label_fisika = tk.Label(frame_input, text="Nilai Fisika")
label_fisika.grid(row=2, column=0, pady=10)
entry_fisika = tk.Entry(frame_input)
entry_fisika.grid(row=2,column=1)

# Label Nilai Inggris
label_inggris = tk.Label(frame_input, text="Nilai Inggris")
label_inggris.grid(row=3, column=0, pady=10)
entry_inggris = tk.Entry(frame_input)
entry_inggris.grid(row=3,column=1)

# label keterangan data berhasil disimpam
def submit():
    tambah_nilai()
    messagebox.showinfo("Info", "Data Berhasil Disimpan")

# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=submit)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Jalankan Aplikasi
root.mainloop()
