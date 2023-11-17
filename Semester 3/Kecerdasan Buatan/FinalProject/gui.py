
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, NW, Checkbutton, IntVar, messagebox
from tkinter.font import Font
import textwrap
import pandas as pd

# Fix scaling on Windows 10 with high DPI scaling
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Set up paths relative to this file
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

# Import class CleaningData from cleaningdata.py file 
from cleaningdata import CleaningData

# Make instance from CleaningData class 
data = CleaningData()

# Create the data frames from CleaningData class
ayamdata = data.ayam()
ayamdata_backup = data.ayam_backup()
kambingdata = data.kambing()
kambingdata_backup = data.kambing_backup()
sapidata = data.sapi()
sapidata_backup = data.sapi_backup()
ikandata = data.ikan()
ikandata_backup = data.ikan_backup()
udangdata = data.udang()
udangdata_backup = data.udang_backup()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Take the data from dataframe and diplay it on the button
def button_ayam_clicked():
    hide_result()
    # Check if ayamdata is empty
    if ayamdata.empty:
        messagebox.showinfo("Information", "Tidak ada data yang bisa ditampilkan.")
        return

    # Select up to 4 random rows from ayamdata
    num_rows = min(4, len(ayamdata))
    random_rows = ayamdata.sample(num_rows)

    # Get the title from these rows
    titles = random_rows['Title'].tolist()

    # Wrap the text
    titles = [textwrap.fill(title, width=20) for title in titles]

    # Set the text of the buttons
    buttons = [button_result1, button_result2, button_result3, button_result4]
    for i in range(4):
        if i < len(titles):
            buttons[i].config(
                text=titles[i], font=("OpenSansRoman", 16, "bold"), fg="white",
                compound='center')
        else:
            buttons[i].config(text="")

    showbuttonresult()

def button_kambing_clicked():
    hide_result()
    # Check if kambingdata is empty
    if kambingdata.empty:
        messagebox.showinfo("Information", "Tidak ada data yang bisa ditampilkan.")
        return

    # Select up to 4 random rows from kambingdata
    num_rows = min(4, len(kambingdata))
    random_rows = kambingdata.sample(num_rows)

    # Get the title from these rows
    titles = random_rows['Title'].tolist()

    # Wrap the text
    titles = [textwrap.fill(title, width=20) for title in titles]

    # Set the text of the buttons
    buttons = [button_result1, button_result2, button_result3, button_result4]
    for i in range(4):
        if i < len(titles):
            buttons[i].config(
                text=titles[i], font=("OpenSansRoman", 16, "bold"), fg="white",
                compound='center')
        else:
            buttons[i].config(text="")

    showbuttonresult()

def button_sapi_clicked():
    hide_result()
    # Check if sapidata is empty
    if sapidata.empty:
        messagebox.showinfo("Information", "Tidak ada data yang bisa ditampilkan.")
        return

    # Select up to 4 random rows from sapidata
    num_rows = min(4, len(sapidata))
    random_rows = sapidata.sample(num_rows)

    # Get the title from these rows
    titles = random_rows['Title'].tolist()

    # Wrap the text
    titles = [textwrap.fill(title, width=20) for title in titles]

    # Set the text of the buttons
    buttons = [button_result1, button_result2, button_result3, button_result4]
    for i in range(4):
        if i < len(titles):
            buttons[i].config(
                text=titles[i], font=("OpenSansRoman", 16, "bold"), fg="white",
                compound='center')
        else:
            buttons[i].config(text="")

    showbuttonresult()

def button_ikan_clicked():
    hide_result()
    # Check if ikandata is empty
    if ikandata.empty:
        messagebox.showinfo("Information", "Tidak ada data yang bisa ditampilkan.")
        return

    # Select up to 4 random rows from ikandata
    num_rows = min(4, len(ikandata))
    random_rows = ikandata.sample(num_rows)

    # Get the title from these rows
    titles = random_rows['Title'].tolist()

    # Wrap the text
    titles = [textwrap.fill(title, width=20) for title in titles]

    # Set the text of the buttons
    buttons = [button_result1, button_result2, button_result3, button_result4]
    for i in range(4):
        if i < len(titles):
            buttons[i].config(
                text=titles[i], font=("OpenSansRoman", 16, "bold"), fg="white",
                compound='center')
        else:
            buttons[i].config(text="")

    showbuttonresult()

def button_udang_clicked():
    hide_result()
    # Check if udangdata is empty
    if udangdata.empty:
        messagebox.showinfo("Information", "Tidak ada data yang bisa ditampilkan.")
        return

    # Select up to 4 random rows from udangdata
    num_rows = min(4, len(udangdata))
    random_rows = udangdata.sample(num_rows)

    # Get the title from these rows
    titles = random_rows['Title'].tolist()

    # Wrap the text
    titles = [textwrap.fill(title, width=20) for title in titles]

    # Set the text of the buttons
    buttons = [button_result1, button_result2, button_result3, button_result4]
    for i in range(4):
        if i < len(titles):
            buttons[i].config(
                text=titles[i], font=("OpenSansRoman", 16, "bold"), fg="white",
                compound='center')
        else:
            buttons[i].config(text="")

    showbuttonresult()

def showbuttonresult():
    if button_result1.cget("text"):
        button_result1.place(
            x=66.0,
            y=676.0,
            width=390.0,
            height=329.0
        )
    if button_result2.cget("text"):
        button_result2.place(
            x=539.0,
            y=676.0,
            width=390.0,
            height=329.0
        )
    if button_result3.cget("text"):
        button_result3.place(
            x=1012.0,
            y=676.0,
            width=390.0,
            height=329.0
        )
    if button_result4.cget("text"):
        button_result4.place(
            x=1485.0,
            y=676.0,
            width=390.0,
            height=329.0
        )

# filter button is used to trasision from main menu to filter menu
def button_filter1_clicked():
    button_ayam.place_forget()
    button_kambing.place_forget()
    button_sapi.place_forget()
    button_ikan.place_forget()
    button_udang.place_forget()
    button_filter.place_forget()
    hide_result()
    textresult.place_forget()

    button_back.place(
    x=1550.0,
    y=900.0,
    width=300.0,
    height=82.0
    )

    show_cb()

def hide_result():
    button_result1.place_forget()
    button_result2.place_forget()
    button_result3.place_forget()
    button_result4.place_forget()

def show_cb():
    checkbputih.place(anchor="s", relx=0.1, rely=0.45, x=0, y=0)
    checkbmerah.place(anchor="s", relx=0.1, rely=0.525, x=0, y=0)
    checklada.place(anchor="s", relx=0.1, rely=0.6, x=0, y=0)
    checkmerica.place(anchor="s", relx=0.1, rely=0.675, x=0, y=0)
    checksantan.place(anchor="s", relx=0.25, rely=0.45, x=0, y=0)
    checkbbombay.place(anchor="s", relx=0.25, rely=0.525, x=0, y=0)
    checkcabe.place(anchor="s", relx=0.25, rely=0.6, x=0, y=0)
    cheackketumbar.place(anchor="s", relx=0.25, rely=0.675, x=0, y=0)
    checkjahe.place(anchor="s", relx=0.4, rely=0.45, x=0, y=0)
    checkwortel.place(anchor="s", relx=0.4, rely=0.525, x=0, y=0)
    checklengkuas.place(anchor="s", relx=0.4, rely=0.6, x=0, y=0)
    checkkunyit.place(anchor="s", relx=0.4, rely=0.675, x=0, y=0)
    checkgaram.place(anchor="s", relx=0.55, rely=0.45, x=0, y=0)
    checkgula.place(anchor="s", relx=0.55, rely=0.525, x=0, y=0)
    checkkemiri.place(anchor="s", relx=0.55, rely=0.6, x=0, y=0)
    checktomat.place(anchor="s", relx=0.55, rely=0.675, x=0, y=0)
    checkkacang.place(anchor="s", relx=0.7, rely=0.45, x=0, y=0)
    checkjamur.place(anchor="s", relx=0.7, rely=0.525, x=0, y=0)
    checkpenyedap.place(anchor="s", relx=0.7, rely=0.6, x=0, y=0)
    checktempe.place(anchor="s", relx=0.7, rely=0.675, x=0, y=0)
    checktelur.place(anchor="s", relx=0.85, rely=0.45, x=0, y=0)
    checkbuncis.place(anchor="s", relx=0.85, rely=0.525, x=0, y=0)
    checkjeruknipis.place(anchor="s", relx=0.85, rely=0.6, x=0, y=0)
    checktahu.place(anchor="s", relx=0.85, rely=0.675, x=0, y=0)

# back button is used to trasision from filter menu to main menu
def botton_back_clicked():
    button_back.place_forget()
    hide_cb()
    show_button_pokok()
    
def hide_cb():
    checkbputih.place_forget()
    checkbmerah.place_forget()
    checklada.place_forget()
    checkmerica.place_forget()
    checksantan.place_forget()
    checkbbombay.place_forget()
    checkcabe.place_forget()
    cheackketumbar.place_forget()
    checkjahe.place_forget()
    checkwortel.place_forget()
    checklengkuas.place_forget()
    checkgaram.place_forget()
    checkgula.place_forget()
    checkkemiri.place_forget()
    checktomat.place_forget()
    checkkacang.place_forget()
    checkjamur.place_forget()
    checkpenyedap.place_forget()
    checktempe.place_forget()
    checktelur.place_forget()
    checkbuncis.place_forget()
    checkjeruknipis.place_forget()
    checktahu.place_forget()
    checkkunyit.place_forget()

def show_button_pokok():
    button_ayam.place(
    x=196.0,
    y=444.0,
    width=300.0,
    height=82.0
    )
    button_kambing.place(
    x=536.0,
    y=444.0,
    width=300.0,
    height=82.0
    )
    button_sapi.place(
    x=876.0,
    y=444.0,
    width=300.0,
    height=82.0
    )
    button_ikan.place(
    x=1216.0,
    y=444.0,
    width=300.0,
    height=82.0
    )
    button_udang.place(
    x=1556.0,
    y=444.0,
    width=300.0,
    height=82.0
    )
    button_filter.place(
    x=66.0,
    y=444.0,
    width=90.0,
    height=82.0
    )
    textresult.place(
    x=66,
    y=574,
    anchor=NW
    )

# when the checkbox clicked, filter the Ingredients column in all dataframes
def cb_ingredient(var, word:str):
    if var.get() == 1:
        filter_ayamdata(word)
        filter_kambingdata(word)
        filter_sapidata(word)
        filter_ikandata(word)
        filter_udangdata(word)
        
    elif var.get() == 0:
        filter_ayamdatabackup(word)
        filter_kambingdatabackup(word)
        filter_sapidatabackup(word)
        filter_ikandatabackup(word)
        filter_udangdatabackup(word)

def filter_ayamdata(word:str):
    global ayamdata
    global ayamdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = ayamdata['Ingredients'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = ayamdata['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    ayamdata_backup = pd.concat([ayamdata_backup, ayamdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    ayamdata = ayamdata[contains_word]

    # Reset the index of both DataFrames
    ayamdata = ayamdata.reset_index(drop=True)
    ayamdata_backup = ayamdata_backup.reset_index(drop=True)

def filter_kambingdata(word:str):
    global kambingdata
    global kambingdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = kambingdata['Ingredients'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = kambingdata['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    kambingdata_backup = pd.concat([kambingdata_backup, kambingdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    kambingdata = kambingdata[contains_word]

    # Reset the index of both DataFrames
    kambingdata = kambingdata.reset_index(drop=True)
    kambingdata_backup = kambingdata_backup.reset_index(drop=True)

def filter_sapidata(word:str):
    global sapidata
    global sapidata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = sapidata['Ingredients'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = sapidata['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    sapidata_backup = pd.concat([sapidata_backup, sapidata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    sapidata = sapidata[contains_word]

    # Reset the index of both DataFrames
    sapidata = sapidata.reset_index(drop=True)
    sapidata_backup = sapidata_backup.reset_index(drop=True)

def filter_ikandata(word:str):
    global ikandata
    global ikandata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = ikandata['Ingredients'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = ikandata['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    ikandata_backup = pd.concat([ikandata_backup, ikandata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    ikandata = ikandata[contains_word]

    # Reset the index of both DataFrames
    ikandata = ikandata.reset_index(drop=True)
    ikandata_backup = ikandata_backup.reset_index(drop=True)

def filter_udangdata(word:str):
    global udangdata
    global udangdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = udangdata['Ingredients'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = udangdata['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    udangdata_backup = pd.concat([udangdata_backup, udangdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    udangdata = udangdata[contains_word]

    # Reset the index of both DataFrames
    udangdata = udangdata.reset_index(drop=True)
    udangdata_backup = udangdata_backup.reset_index(drop=True)

def filter_ayamdatabackup(word: str):
    global ayamdata
    global ayamdata_backup

    # Create a boolean Series
    contains_word = ayamdata_backup['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata_backup and transfer these rows to ayamdata
    ayamdata = pd.concat([ayamdata, ayamdata_backup[contains_word]], ignore_index=True)

    # Drop these rows from ayamdata_backup
    ayamdata_backup = ayamdata_backup[~contains_word]

    # Reset the index of both DataFrames
    ayamdata = ayamdata.reset_index(drop=True)
    ayamdata_backup = ayamdata_backup.reset_index(drop=True)

def filter_kambingdatabackup(word: str):
    global kambingdata
    global kambingdata_backup
    # Create a boolean Series
    contains_word = kambingdata_backup['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata_backup and transfer these rows to ayamdata
    kambingdata = pd.concat([kambingdata, kambingdata_backup[contains_word]], ignore_index=True)

    # Drop these rows from ayamdata_backup
    kambingdata_backup = kambingdata_backup[~contains_word]

    # Reset the index of both DataFrames
    kambingdata = kambingdata.reset_index(drop=True)
    kambingdata_backup = kambingdata_backup.reset_index(drop=True)

def filter_sapidatabackup(word: str):
    global sapidata
    global sapidata_backup
    # Create a boolean Series
    contains_word = sapidata_backup['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata_backup and transfer these rows to ayamdata
    sapidata = pd.concat([sapidata, sapidata_backup[contains_word]], ignore_index=True)

    # Drop these rows from ayamdata_backup
    sapidata_backup = sapidata_backup[~contains_word]

    # Reset the index of both DataFrames
    sapidata = sapidata.reset_index(drop=True)
    sapidata_backup = sapidata_backup.reset_index(drop=True)

def filter_ikandatabackup(word: str):
    global ikandata
    global ikandata_backup
    # Create a boolean Series
    contains_word = ikandata_backup['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata_backup and transfer these rows to ayamdata
    ikandata = pd.concat([ikandata, ikandata_backup[contains_word]], ignore_index=True)

    # Drop these rows from ayamdata_backup
    ikandata_backup = ikandata_backup[~contains_word]

    # Reset the index of both DataFrames
    ikandata = ikandata.reset_index(drop=True)
    ikandata_backup = ikandata_backup.reset_index(drop=True)

def filter_udangdatabackup(word: str):
    global udangdata
    global udangdata_backup
    # Create a boolean Series
    contains_word = udangdata_backup['Ingredients'].str.contains(word, na=False)

    # Use the Series to index ayamdata_backup and transfer these rows to ayamdata
    udangdata = pd.concat([udangdata, udangdata_backup[contains_word]], ignore_index=True)

    # Drop these rows from ayamdata_backup
    udangdata_backup = udangdata_backup[~contains_word]

    # Reset the index of both DataFrames
    udangdata = udangdata.reset_index(drop=True)
    udangdata_backup = udangdata_backup.reset_index(drop=True)

# when the user "Enter the entry", filter the Title column in all dataframes
def on_enter_entry(event):
    # Get the string from the entry widget
    word = entry_1.get().lower()

    if word != "":
        # Filter the data
        filter_ayamdata_title(word)
        filter_kambingdata_title(word)
        filter_sapidata_title(word)
        filter_ikandata_title(word)
        filter_udangdata_title(word)
    else:
        reset_data()
    
def filter_ayamdata_title(word:str):
    global ayamdata
    global ayamdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = ayamdata['Title'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = ayamdata['Title'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    ayamdata_backup = pd.concat([ayamdata_backup, ayamdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    ayamdata = ayamdata[contains_word]

    # Reset the index of both DataFrames
    ayamdata = ayamdata.reset_index(drop=True)
    ayamdata_backup = ayamdata_backup.reset_index(drop=True)

def filter_kambingdata_title(word:str):
    global kambingdata
    global kambingdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = kambingdata['Title'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = kambingdata['Title'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    kambingdata_backup = pd.concat([kambingdata_backup, kambingdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    kambingdata = kambingdata[contains_word]

    # Reset the index of both DataFrames
    kambingdata = kambingdata.reset_index(drop=True)
    kambingdata_backup = kambingdata_backup.reset_index(drop=True)

def filter_sapidata_title(word:str):
    global sapidata
    global sapidata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = sapidata['Title'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = sapidata['Title'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    sapidata_backup = pd.concat([sapidata_backup, sapidata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    sapidata = sapidata[contains_word]

    # Reset the index of both DataFrames
    sapidata = sapidata.reset_index(drop=True)
    sapidata_backup = sapidata_backup.reset_index(drop=True)

def filter_ikandata_title(word:str):
    global ikandata
    global ikandata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = ikandata['Title'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = ikandata['Title'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    ikandata_backup = pd.concat([ikandata_backup, ikandata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    ikandata = ikandata[contains_word]

    # Reset the index of both DataFrames
    ikandata = ikandata.reset_index(drop=True)
    ikandata_backup = ikandata_backup.reset_index(drop=True)

def filter_udangdata_title(word:str):
    global udangdata
    global udangdata_backup
    # Create a boolean Series
    if word == "cabe" or word == "cabai":
        contains_word = udangdata['Title'].str.contains('cabe|cabai', na=False)
    else:
        contains_word = udangdata['Title'].str.contains(word, na=False)

    # Use the Series to index ayamdata and transfer these rows to ayamdata_backup
    udangdata_backup = pd.concat([udangdata_backup, udangdata[~contains_word]], ignore_index=True)

    # Keep only the rows in ayamdata that contain the word
    udangdata = udangdata[contains_word]

    # Reset the index of both DataFrames
    udangdata = udangdata.reset_index(drop=True)
    udangdata_backup = udangdata_backup.reset_index(drop=True)

def reset_data():
    global ayamdata
    global ayamdata_backup
    global kambingdata
    global kambingdata_backup
    global sapidata
    global sapidata_backup
    global ikandata
    global ikandata_backup
    global udangdata
    global udangdata_backup

    ayamdata = data.ayam()
    ayamdata_backup = data.ayam_backup()
    kambingdata = data.kambing()
    kambingdata_backup = data.kambing_backup()
    sapidata = data.sapi()
    sapidata_backup = data.sapi_backup()
    ikandata = data.ikan()
    ikandata_backup = data.ikan_backup()
    udangdata = data.udang()
    udangdata_backup = data.udang_backup()

    checkbputih.deselect()
    checkbmerah.deselect()
    checklada.deselect()
    checkmerica.deselect()
    checksantan.deselect()
    checkbbombay.deselect()
    checkcabe.deselect()
    cheackketumbar.deselect()
    checkjahe.deselect()
    checkwortel.deselect()
    checklengkuas.deselect()
    checkgaram.deselect()
    checkgula.deselect()
    checkkemiri.deselect()
    checktomat.deselect()
    checkkacang.deselect()
    checkjamur.deselect()
    checkpenyedap.deselect()
    checktempe.deselect()
    checktelur.deselect()
    checkbuncis.deselect()
    checkjeruknipis.deselect()
    checktahu.deselect()
    checkkunyit.deselect()

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFC25F")


canvas = Canvas(
    window,
    bg = "#FFC25F",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_bg_sayur = PhotoImage(
    file=relative_to_assets("bg_sayur.png"))
bg_sayur = canvas.create_image(
    959.0,
    253.0,
    image=image_bg_sayur
)

title = canvas.create_text(
    531.0,
    53.0,
    anchor="nw",
    text="LET US COOK!",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 128 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    960.0,
    281.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("OpenSansRoman", 35 * -1)
)
entry_1.place(
    x=489.0,
    y=235.0,
    width=942.0,
    height=80.0
)
entry_1.bind("<Return>", on_enter_entry)

image_bg_putih = PhotoImage(
    file=relative_to_assets("bg_putih.png"))
bg_putih = canvas.create_image(
    960.0,
    734.0,
    image=image_bg_putih
)

button_kambing_image = PhotoImage(
    file=relative_to_assets("button_kambing.png"))
button_kambing = Button(
    image=button_kambing_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_kambing_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_kambing.place(
    x=536.0,
    y=444.0,
    width=300.0,
    height=82.0
)

button_ayam_image = PhotoImage(
    file=relative_to_assets("button_ayam.png"))
button_ayam = Button(
    image=button_ayam_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_ayam_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_ayam.place(
    x=196.0,
    y=444.0,
    width=300.0,
    height=82.0
)

button_sapi_image = PhotoImage(
    file=relative_to_assets("button_sapi.png"))
button_sapi = Button(
    image=button_sapi_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_sapi_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_sapi.place(
    x=876.0,
    y=444.0,
    width=300.0,
    height=82.0
)

button_ikan_image = PhotoImage(
    file=relative_to_assets("button_ikan.png"))
button_ikan = Button(
    image=button_ikan_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_ikan_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_ikan.place(
    x=1216.0,
    y=444.0,
    width=300.0,
    height=82.0
)

button_udang_image = PhotoImage(
    file=relative_to_assets("button_udang.png"))
button_udang = Button(
    image=button_udang_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_udang_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_udang.place(
    x=1556.0,
    y=444.0,
    width=300.0,
    height=82.0
)

button_filter_image = PhotoImage(
    file=relative_to_assets("button_filter.png"))
button_filter = Button(
    image=button_filter_image,
    borderwidth=0,
    highlightthickness=0,
    command=button_filter1_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)
button_filter.place(
    x=66.0,
    y=444.0,
    width=90.0,
    height=82.0
)

font = Font(
    family="OpenSansRoman Bold", size=40 * -1)
textresult = Label(
    window, text="Result", fg="#9E9E9E", font=font, bg="#FFFFFF")
textresult.place(
    x=66, y=574, anchor=NW)

button_result_image = PhotoImage(
    file=relative_to_assets("button_result.png"))
button_result1 = Button(
    image=button_result_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    bg="white",
    activebackground="white"
)

button_result2 = Button(
    image=button_result_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    bg="white",
    activebackground="white"
)

button_result3 = Button(
    image=button_result_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    bg="white",
    activebackground="white"
)

button_result4 = Button(
    image=button_result_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
    bg="white",
    activebackground="white"
)


button_back_image = PhotoImage(
    file=relative_to_assets("button_back.png"))
button_back = Button(
    image=button_back_image,
    borderwidth=0,
    highlightthickness=0,
    command=botton_back_clicked,
    relief="flat",
    bg="white",
    activebackground="white"
)

checkbputih_value = IntVar()
checkbputih = Checkbutton(window, variable=checkbputih_value)
checkbputih.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Bawang Putih',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkbputih_value, "bawang putih")
)

checkbmerah_value = IntVar()
checkbmerah = Checkbutton(window, variable=checkbmerah_value)
checkbmerah.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    state="normal",
    text='Bawang Merah',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkbmerah_value, "bawang merah")
)

checklada_value = IntVar()
checklada = Checkbutton(window, variable=checklada_value)
checklada.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Lada',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checklada_value, "lada")
)

checkmerica_value = IntVar()
checkmerica = Checkbutton(window, variable=checkmerica_value)
checkmerica.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Merica',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkmerica_value, "merica")
)

checksantan_value = IntVar()
checksantan = Checkbutton(window, variable=checksantan_value)
checksantan.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Santan',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checksantan_value, "santan")
)

checkbbombay_value = IntVar()
checkbbombay = Checkbutton(window, variable=checkbbombay_value)
checkbbombay.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Bawang Bombay',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkbbombay_value, "bombay")
)

checkcabe_value = IntVar()
checkcabe = Checkbutton(window, variable=checkcabe_value)
checkcabe.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Cabe',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkcabe_value, "cabe")
)

cheackketumbar_value = IntVar()
cheackketumbar = Checkbutton(window, variable=cheackketumbar_value)
cheackketumbar.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Ketumbar',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(cheackketumbar_value, "ketumbar")
)

checkjahe_value = IntVar()
checkjahe = Checkbutton(window, variable=checkjahe_value)
checkjahe.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Jahe',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkjahe_value, "jahe")
)

checkwortel_value = IntVar()
checkwortel = Checkbutton(window, variable=checkwortel_value)
checkwortel.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Wortel',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkwortel_value, "wortel")
)

checklengkuas_value = IntVar()
checklengkuas = Checkbutton(window, variable=checklengkuas_value)
checklengkuas.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Lengkuas',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checklengkuas_value, "lengkuas")
)

checkkunyit_value = IntVar()
checkkunyit = Checkbutton(window, variable=checkkunyit_value)
checkkunyit.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Kunyit',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkkunyit_value, "kunyit")
)

checkgaram_value = IntVar()
checkgaram = Checkbutton(window, variable=checkgaram_value)
checkgaram.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Garam',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkgaram_value, "garam")
)

checkgula_value = IntVar()
checkgula = Checkbutton(window, variable=checkgula_value)
checkgula.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Gula',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkgula_value, "gula")
)

checkkemiri_value = IntVar()
checkkemiri = Checkbutton(window, variable=checkkemiri_value)
checkkemiri.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Kemiri',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkkemiri_value, "kemiri")
)

checktomat_value = IntVar()
checktomat = Checkbutton(window, variable=checktomat_value)
checktomat.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Tomat',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checktomat_value, "tomat")
)

checkkacang_value = IntVar()
checkkacang = Checkbutton(window, variable=checkkacang_value)
checkkacang.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Kacang',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkkacang_value, "kacang")
)

checkjamur_value = IntVar()
checkjamur = Checkbutton(window, variable=checkjamur_value)
checkjamur.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Jamur',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkjamur_value, "jamur")
)

checkpenyedap_value = IntVar()
checkpenyedap = Checkbutton(window, variable=checkpenyedap_value)
checkpenyedap.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Penyedap Rasa',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkpenyedap_value, "penyedap")
)

checktempe_value = IntVar()
checktempe = Checkbutton(window, variable=checktempe_value)
checktempe.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Tempe',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checktempe_value, "tempe")
)

checktelur_value = IntVar()
checktelur = Checkbutton(window, variable=checktelur_value)
checktelur.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Telur',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checktelur_value, "telur")
)

checkbuncis_value = IntVar()
checkbuncis = Checkbutton(window, variable=checkbuncis_value)
checkbuncis.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Buncis',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkbuncis_value, "buncis")
)

checkjeruknipis_value = IntVar()
checkjeruknipis = Checkbutton(window, variable=checkjeruknipis_value)
checkjeruknipis.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Jeruk Nipis',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checkjeruknipis_value, "jeruk nipis")
)

checktahu_value = IntVar()
checktahu = Checkbutton(window, variable=checktahu_value)
checktahu.configure(
    anchor="w",
    bg="white",
    font="{OpenSansRoman} 16 {}",
    text='Tahu',
    width=15,
    activebackground="#FFFFFF",
    onvalue=1,
    offvalue=0, 
    command=lambda: cb_ingredient(checktahu_value, "tahu")
)

window.resizable(False, False)
window.mainloop()