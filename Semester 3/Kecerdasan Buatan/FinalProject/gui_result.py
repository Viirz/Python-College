from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import textwrap

import ctypes
# Fix scaling on Windows 10 with high DPI scaling
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Set up paths relative to this file
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    430.0,
    662.0,
    image=image_image_1
)

canvas.create_text(
    345.0,
    370.0,
    anchor="nw",
    text="Ingredients",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1342.0,
    662.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1617.0,
    y=999.0,
    width=255.0,
    height=70.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    960.0,
    150.0,
    image=image_image_3
)

# Read the text from "title.txt"
with open("title.txt", "r", encoding='utf-8') as file:
    text_title = file.read()

# Convert the first character of each word to uppercase
text_title = text_title.title()

# Wrap the text to a width of 20 characters
text_title = textwrap.fill(text_title, width=20)

# Calculate the font size based on the length of the text
font_size = min(70, 128 // (len(text_title.split()) // 2))

canvas.create_text(
    550.0,
    101.0,
    anchor="nw",
    text=text_title,
    fill="#FFFFFF",  # Set the text color to white
    font=("OpenSansRoman Bold", 95 * -1)
)

# Read the text from "ingredients.txt"
with open("ingredients.txt", "r", encoding='utf-8') as file:
    text_ingredients = file.read().splitlines()

text_ingredients = '\n'.join(text_ingredients)

# Wrap the text to a width of 20 characters
text_ingredients = textwrap.fill(text_ingredients, width=40)

canvas.create_text(
    160.0,
    443.0,
    anchor="nw",
    text=text_ingredients,
    fill="#FFFFFF",
    font=("OpenSansRoman", 25 * -1)
)

canvas.create_text(
    1219.751953125,
    370.0,
    anchor="nw",
    text="How to make\n",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 40 * -1)
)

# Read the text from "ingredients.txt"
with open("steps.txt", "r", encoding='utf-8') as file:
    text_steps = file.read().splitlines()

text_steps = '\n'.join(text_steps)

# Wrap the text to a width of 20 characters
text_steps = textwrap.fill(text_steps, width=70)

canvas.create_text(
    899.0,
    443.0,
    anchor="nw",
    text=text_steps,
    fill="#FFFFFF",
    font=("OpenSansRoman", 25 * -1)
)
window.resizable(False, False)
window.mainloop()


