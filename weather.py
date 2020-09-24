from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import time

root = Tk()
root.title("Weather App")
root.geometry("600x600")
root.iconbitmap("images/iconfinder_Weather_Weather_Forecast_Lightning_Storm_Energy_3859139.ico")
root.resizable(False, False)
root.configure(background="lightgrey")

def clock():
    day = time.strftime("%A")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_clock.config(text=day + " " + hour + ":" + minute + ":" + second)
    my_clock.after(1000,clock)

  

def search():

    if(city_entry.get() == ""):
        messagebox.showinfo("Info","Please enter a city!")
        return

    try:
        #Results Frame
        result_frame = Frame(root, background="orange")
        l = Label(result_frame, text="Results")
        l.pack(fill="x", pady=5)
        result_frame.place(x=100, y=100)


    except:
        messagebox.showerror("Invalid input", "Please give a city name only!")    


#Frame Header
frame_header = Frame(master=root, padx=3, pady=3, height=50)
frame_header.place(x=300, y=20, anchor=N)

#Frame Bottom
frame_bottom = Frame(root, background="orange")
frame_bottom.place(x=300, y=540, anchor=CENTER)

#Frame Main
frame_main = Frame(root)


#Clock
my_clock = Label(frame_bottom, text="Clock", width=30, font=("Arial" , 10), height=3)
my_clock.pack(padx=3, pady=3)


#Title
titleLabel = Label(frame_header, text="My Weather App", font=("Arial", 18))
titleLabel.grid(row=0, column=0, columnspan=4)


#City Label
city_label = Label(frame_header, text="Enter City:")
city_label.grid(row=1, column=0)

#Input Field
city_entry = Entry(frame_header, width=40)
city_entry.grid(row=1, column=1)

#Search button
search_btn = Button(frame_header, text="Search", command=search)
img = Image.open("images/search.png")
img2 = img.resize((25, 25), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(img2)
search_btn.config(image=tk_image)
search_btn.grid(row=1, column=3)

#Call clock method
clock()  


root.mainloop()