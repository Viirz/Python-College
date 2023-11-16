import tkinter as tk
from tkinter import ttk

class ScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig("self.frame", width=canvas_width)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")

    scrolled_frame = ScrolledFrame(root)
    scrolled_frame.pack(side="top", fill="both", expand=True)

    # Add widgets to the scrolled frame
    for i in range(20):
        label = tk.Label(scrolled_frame.frame, text=f"Label {i}")
        label.pack(pady=5)

    root.mainloop()
