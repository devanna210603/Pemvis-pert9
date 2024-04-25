import tkinter as tk
from tkinter import messagebox

def tes_tombol():
    messagebox.showinfo("Info", "Berhasil Menginput Nama Anda Terima Kasih!")

# Inisialisasi root window
root = tk.Tk()
root.geometry("500x500")
root.title("Aplikasi GUI Sederhana")

# Membuat frame utama
Frameku = tk.Frame(root, bg='green', padx=5, pady=5)
Frameku.pack(fill=tk.BOTH, expand=True)

# Tombol
Tombolku = tk.Button(Frameku, text="Input", bg='gray', fg='white', command=tes_tombol)
Tombolku.pack(pady=10)

# Entry widget
Entryku = tk.Entry(Frameku, bg='lightgreen', bd=2, relief=tk.SOLID)
Entryku.pack(pady=10, fill=tk.X)

# Canvas
C = tk.Canvas(Frameku, bg="white", height=250, width=400, bd=2, relief=tk.SOLID)
coord = 50, 50, 350, 200
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(50, 50, 200, 200, fill='blue')
C.pack(pady=10)

# Label Frame
label_frame = tk.LabelFrame(Frameku, text="Label Frame", bg='lightgreen', padx=10, pady=10)
label_frame.pack(pady=10, fill=tk.X)

var = tk.StringVar()
label = tk.Label(label_frame, textvariable=var, bg='lightgreen', fg='black', font=("Arial", 12))
var.set("Hey!? Coba pilih kesukaanmu")
label.pack()

# Checkboxes
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(Frameku, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, bg='lightgreen', font=("Arial", 12))
C2 = tk.Checkbutton(Frameku, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, bg='lightgreen', font=("Arial", 12))
C1.pack(pady=5)
C2.pack(pady=5)

# ListBox
Lb1 = tk.Listbox(Frameku)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()


root.mainloop()
