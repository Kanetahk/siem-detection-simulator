import tkinter as tk

def b_clicked():
    print("a")

root = tk.Tk()
root.title("SIEM Detection Simulator")

b = tk.Button(root, text="Generate log", command=b_clicked)
b.pack()

root.mainloop()