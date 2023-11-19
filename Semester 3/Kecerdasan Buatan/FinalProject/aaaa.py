from tkinter import Tk, Canvas
import textwrap

class ResultFrame:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1080x720")
        self.window.configure(bg = "#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 720,
            width = 1080,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.text_title = "your text title here"
        self.text_title = self.text_title.title()
        self.text_title = textwrap.fill(self.text_title, width=25)
        self.font_size = min(70, 128 // (len(self.text_title.split()) // 2))

        self.canvas.create_text(
            519.0,
            101.0,
            anchor="nw",
            text=self.text_title,
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", self.font_size * -1)
        )

        self.canvas.create_text(
            160.0,
            443.0,
            anchor="nw",
            text="1 Ekor Ayam Kampung (potong 12)",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 25 * -1)
        )

        self.window.resizable(False, False)
        self.window.mainloop()


result_frame = ResultFrame()