from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import datetime 

root = Tk()
root.title("Weather App")
root.geometry("600x600")
root.iconbitmap("images/iconfinder_Weather_Weather_Forecast_Lightning_Storm_Energy_3859139.ico")
#root.resizable(False, False)
root.configure(background="lightgrey")


def search():

    if(city_entry.get() == ""):
        messagebox.showinfo("Info","Please enter a city!")
        return

    try:
        #Results Frame
        frame = LabelFrame(root, text=city_entry.get())
        frame.place(x=25, y=70)

        #Results Label
        date = datetime.now()
        l = Label(frame, text=date)
        l.grid(row=0, column=2)
    except:
        messagebox.showerror("Invalid input", "Please give a city name only!")    


#Input Field
city_entry = Entry(root, width=40)
city_entry.place(x=180, y=20)

#Search button
search_btn = Button(root, text="Search", command=search)
img = Image.open("images/search.png")
img2 = img.resize((25, 25), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(img2)
search_btn.config(image=tk_image)
search_btn.place(x=400,y=15)

#City Label
city_label = Label(root, text="Enter City: " , background="lightgrey")
city_label.place(x=118, y=20)

root.mainloop()