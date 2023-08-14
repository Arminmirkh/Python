import tkinter as tk
import json
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import requests as rq


def getw(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=512ed63321972affad607c8ef9d6d5bc"
    r = 0
    try:
        r = rq.get(url.format(city))
    except:
        mb.showerror("Connection Erorr", "Try Again")
        return
    if r.status_code == 200:
        y = json.loads(r.text)
        status = y["weather"][0]["main"]
        status2 = y["weather"][0]["description"]
        lblt.configure(
            text=city + " Temprature : " + str(round(y["main"]["temp"] - 273.15, 2))
        )
        lblw.configure(text=f"Status : {status} {status2} ")
        if status == "Rain":
            icon("r.png")
        elif status == "Sun":
            icon("s.png")
        elif status == "Clouds":
            icon("c.png")
    else:
        mb.showerror("Erorr", "Something Went Wrong")


def icon(address):
    img = Image.open(address)
    photo = ImageTk.PhotoImage(img)
    lbls.configure(image=photo)
    lbls.image = photo


root = tk.Tk(className="Weather App")
root.geometry("300x300")
btnclk = tk.Button(root, text="Get Weather", command=lambda: getw(txt.get(1.0, tk.END)))
txt = tk.Text(root, height=1, width=25, font=("aerial", 20))
lblt = tk.Label(root)
lblw = tk.Label(root)
lbls = tk.Label(root)
txt.pack(pady=5)
btnclk.pack(pady=10)
lblt.pack()
lblw.pack()
lbls.pack()
root.mainloop()
