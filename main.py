import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen

from io import BytesIO

root = tk.Tk()

URL = "https://e-note.s3.amazonaws.com/img.png?AWSAccessKeyId=AKIA5P4ROYQSWV2BUFMD&Signature=%2BT1Vfdia%2B1jPWucAguxRX1EQhZs%3D&Expires=1656486019"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()
