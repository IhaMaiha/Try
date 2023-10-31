import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Fungsi untuk menghitung tekanan
def calculate_pressure():
    try:
        force = float(force_entry.get())
        area = float(area_entry.get())
        pressure = force / area
        result_label.config(text=f"Tekanan: {pressure} N/m^2")
        plot_pressure(force, area)
    except ValueError:
        result_label.config(text="Masukkan angka yang valid")

# Fungsi untuk membuat plot
def plot_pressure(force, area):
    fig, ax = plt.subplots()
    ax.set_title("Grafik Tekanan vs. Penampang")
    ax.set_xlabel("Penampang (m^2)")
    ax.set_ylabel("Tekanan (N/m^2)")

    areas = np.linspace(0.1, 10, 100)  # Range penampang yang akan diplot
    pressures = force / areas

    ax.plot(areas, pressures)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=4, column=0, columnspan=2)

# Membuat jendela utama
root = tk.Tk()
root.title("Hukum Pascal")

# Membuat frame utama
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Label dan entry untuk input
force_label = ttk.Label(frame, text="Masukkan Gaya (N):")
force_label.grid(row=0, column=0, padx=5, pady=5)
force_entry = ttk.Entry(frame)
force_entry.grid(row=0, column=1, padx=5, pady=5)

area_label = ttk.Label(frame, text="Masukkan Penampang (m^2):")
area_label.grid(row=1, column=0, padx=5, pady=5)
area_entry = ttk.Entry(frame)
area_entry.grid(row=1, column=1, padx=5, pady=5)

# Tombol hitung
calculate_button = ttk.Button(frame, text="Hitung Tekanan", command=calculate_pressure)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Hasil teks
result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()