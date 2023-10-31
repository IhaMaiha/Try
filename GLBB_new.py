import tkinter as tk
from tkinter import Label, Entry, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_glbb():
    v0 = float(entry_v0.get())
    a = float(entry_a.get())
    t = float(entry_t.get())

    time = [i for i in range(int(t) + 1)]
    displacement = [v0 * t + 0.5 * a * t**2 for t in time]

    fig, ax = plt.subplots()
    ax.plot(time, displacement)
    ax.set_xlabel('Waktu (s)')
    ax.set_ylabel('Displacement (m)')
    ax.set_title('Grafik Gerak Lurus Berubah Beraturan')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0)

# Membuat jendela tkinter
window = tk.Tk()
window.title('GLBB Plotter')

# Membuat frame
frame = tk.Frame(window)
frame.pack()

# Label dan Input untuk Kecepatan Awal (v0)
Label(frame, text="Kecepatan Awal (m/s):").grid(row=0, column=0)
entry_v0 = Entry(frame)
entry_v0.grid(row=0, column=1)

# Label dan Input untuk Percepatan (a)
Label(frame, text="Percepatan (m/s^2):").grid(row=1, column=0)
entry_a = Entry(frame)
entry_a.grid(row=1, column=1)

# Label dan Input untuk Waktu (t)
Label(frame, text="Waktu (s):").grid(row=2, column=0)
entry_t = Entry(frame)
entry_t.grid(row=2, column=1)

# Tombol untuk memplot
plot_button = Button(frame, text="Plot GLBB", command=plot_glbb)
plot_button.grid(row=3, column=0)

# Memulai GUI
window.mainloop()