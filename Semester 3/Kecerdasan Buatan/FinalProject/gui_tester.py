import tkinter as tk
from pathlib import Path

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.configure(bg="#FFC25F")

        self.canvas = tk.Canvas(
            self.root,
            bg="#FFC25F",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def create_widgets(self):
        image_bg_sayur = tk.PhotoImage(file=self.relative_to_assets("bg_sayur.png"))
        self.bg_sayur = self.canvas.create_image(
            959.0,
            253.0,
            image=image_bg_sayur
        )

        self.canvas.create_text(
            531.0,
            53.0,
            anchor="nw",
            text="LET US COOK!",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 128 * -1)
        )

        entry_image_1 = tk.PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            960.0,
            281.0,
            image=entry_image_1
        )
        self.entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman", 35 * -1)
        )
        self.entry_1.place(
            x=489.0,
            y=235.0,
            width=942.0,
            height=80.0
        )

        image_bg_putih = tk.PhotoImage(file=self.relative_to_assets("bg_putih.png"))
        bg_putih = self.canvas.create_image(
            960.0,
            734.0,
            image=image_bg_putih
        )

        button_kambing_image = tk.PhotoImage(file=self.relative_to_assets("button_kambing.png"))
        self.button_kambing = tk.Button(
            image=button_kambing_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_clicked("button_kambing"),
            relief="flat",
            bg="white",
            activebackground="white"
        )
        self.button_kambing.place(
            x=536.0,
            y=444.0,
            width=300.0,
            height=82.0
        )

        # Add other buttons similarly

        self.canvas.create_text(
            66.0,
            574.0,
            anchor="nw",
            text="Result",
            fill="#9E9E9E",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        button_result_image = tk.PhotoImage(file=self.relative_to_assets("button_result.png"))
        self.button_result1 = tk.Button(
            image=button_result_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.button_clicked("button_result1"),
            relief="flat",
            bg="white",
            activebackground="white"
        )
        self.button_result1.place(
            x=66.0,
            y=676.0,
            width=390.0,
            height=329.0
        )

        # Add other result buttons similarly

        self.root.resizable(False, False)

    def button_clicked(self, button_name):
        print(f"{button_name} clicked")


if __name__ == "__main__":
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\File Coding\Python College\Semester 3\Kecerdasan Buatan\build\assets\frame0")

    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
