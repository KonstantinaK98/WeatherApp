from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Weather App")
root.geometry("600x600")
root.iconbitmap("images/iconfinder_Weather_Weather_Forecast_Lightning_Storm_Energy_3859139.ico")
root.resizable(False, False)
root.configure(background="lightgrey")


def search():

    frame = LabelFrame(root, text=city_entry.get(), padx=250, pady=200)
    frame.place(x=25, y=50)

    l = Label(frame, text="Results")
    l.pack()

city_entry = Entry(root, width=40)
city_entry.place(x=180, y=10)

search_btn = Button(root, text="Search", command=search)
img = Image.open("images/search.png")
img2 = img.resize((25, 25), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(img2)
search_btn.config(image=tk_image)
search_btn.place(x=400,y=5)

city_label = Label(root, text="Enter City: " , background="lightgrey")
city_label.place(x=118, y=10)

root.mainloop()