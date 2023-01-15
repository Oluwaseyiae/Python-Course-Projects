import tkinter as tk
from PIL import Image, ImageTk

# Window setup
root = tk.Tk()
root.title('Simple Email Slicer')

canvas = tk.Canvas(root, height=300, width=500)
canvas.grid(columnspan= 3, rowspan=5)

# Logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# ----------------------Main_Body---------
instruction = tk.Label(root, text="Input your e-mail ID in the text box and click the slice button", font="Raleway 13")
instruction.grid(columnspan=3, column=0, row=2)

# Placeholder
email = tk.StringVar()
entry = tk.Entry(textvariable= email,font=("Raleway 11"),width=40, justify="left", bg="White", border=1, borderwidth= 2)
entry.grid(column=1, row=3)

# Button
slice_text = tk.StringVar()
slice_btn = tk.Button(root, textvariable=slice_text, command=lambda: slice(), font=("Raleway"), bg="Magenta", fg="white", height=1, width=7)
slice_text.set("Slice")
slice_btn.grid(column=1, row=4)

# Text box
text_box = tk.Text(root, height=10, width=50, font=("Raleway 11") ,padx=10, pady=10 )
text_box.grid(column=1, row=5)

# Functionality
def slice():
    try:
        email=entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index("@")]
        domain = inp_email[inp_email.index('@') + 1:]

        text_box.delete("1.0", tk.END)
        msg = "Email entered was: {}\nYour email username is {}\nAnd your email domain server is {}"
        msg_formatted = msg.format(email,username,domain)

        text_box.insert(tk.END,msg_formatted)
        entry.delete(0, "end")
    except:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END,"Invalid Email!")

# --------------------------Main_Body ends----------

canvas = tk.Canvas(root, height=60, width=500)
canvas.grid(columnspan=3)

root.mainloop()