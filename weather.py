from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import time
import requests

root = Tk()
root.title("Weather App")
root.geometry("600x500")
root.iconbitmap("images/iconfinder_Weather_Weather_Forecast_Lightning_Storm_Energy_3859139.ico")
root.resizable(False, False)
root.configure(background="lightgrey")

def clock():
    global hour
    day = time.strftime("%A")
    date = time.strftime("%d") + "/" + time.strftime("%m") + "/" + time.strftime("%Y")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_clock.config(text=day + "  " + date + " \n" + hour + ":" + minute + ":" + second)
    my_clock.after(1000,clock)


def createWelcomeFrame():
    global frame_w
    global welcome
    #Frame Welcome
    frame_w = Frame(root)
    frame_w.place(x=160, y=180)

    #Welcome Label
    welcome = Label(frame_w, text="Discover the weather\n in any city" , font=("Arial" , 22), bg="lightgrey")
    welcome.pack(anchor=CENTER)


def conditions(con):
    global imgLabel
    con = con.lower()
    #Clouds
    if(con == "few clouds"):
        global tk_cloudImg
        if(hour >= "06" and hour <= "18"):
            Img = Image.open("images/sunCloud.png")
            tk_cloudImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
            imgLabel.config(image=tk_cloudImg)
        else:
            Img = Image.open("images/nightCloud.png")    
            tk_cloudImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
            imgLabel.config(image=tk_cloudImg)
    elif(con == "scattered clouds" or con == "broken clouds" or con == "overcast clouds"):
        global tk_cImg
        Img = Image.open("images/cloud.png")
        tk_cImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_cImg)    
    #Rain    
    elif(con == "light rain" or con == "rain" or con == "moderate rain" or con == "light intensity shower rain" or con == "shower rain" or con == "ragged shower rain"):
        global tk_rainImg
        Img = Image.open("images/cloudRain.png")
        tk_rainImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_rainImg)
    elif(con == "heavy intensity rain" or con == "very heavy rain" or con == "extreme rain" or con == "freezing rain" or con == "heavy intensity shower rain"):
        global tk_hrainImg
        Img = Image.open("images/heavyRain.png")
        tk_hrainImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_hrainImg)    
    #Clear    
    elif(con == "clear sky"):
        global tk_clearImg
        if(hour >= "06" and hour <= "18"):
            Img = Image.open("images/sun.png")
            tk_clearImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
            imgLabel.config(image=tk_clearImg) 
        else:
            Img = Image.open("images/clearNight.png")
            tk_clearImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
            imgLabel.config(image=tk_clearImg)     
    #Atmosphere    
    elif(con == "mist" or con == "smoke" or con == "fog" or con == "haze"):
        global tk_mistImg
        Img = Image.open("images/smokeFoggy.png")
        tk_mistImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_mistImg)
    elif(con == "sand" or con == "sand/ dust whirls" or con == "dust" or con == "volcanic ash"):
        global tk_sandImg
        Img = Image.open("images/sand.png")
        tk_sandImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_sandImg) 
    elif(con == "tornado"):
        global tk_tornadoImg
        Img = Image.open("images/tornado.png")
        tk_tornadoImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_tornadoImg)              
    #Snow           
    elif(con == "light snow" or con == "snow" or con == "heavy snow" or con == "rain and snow" or con == "heavy shower snow"):
        global tk_snowImg
        Img = Image.open("images/snow.png")
        tk_snowImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_snowImg)
    elif(con == "sleet" or con == "light shower sleet" or con == "shower sleet" or con == "light rain and snow" or con == "light shower snow" or con == "shower snow"):
        global tk_snowflakeImg
        Img = Image.open("images/snowflake.png")
        tk_snowflakeImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_snowflakeImg)  
    #Thunderstorm
    elif(con == "thunderstorm" or con == "thunderstorm with light rain" or con == "thunderstorm with rain" or con == "thunderstorm with heavy rain"):
        global tk_thunderImg
        Img = Image.open("images/cloudStorm.png")
        tk_thunderImg = ImageTk.PhotoImage(Img.resize((125, 125), Image.ANTIALIAS))
        imgLabel.config(image=tk_thunderImg)       


def weatherCall():
    try:            
        city = city_entry.get()
        
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&appid=606fbbff84c0cd0b13c4a6677cb33928".format(city)
        
        res = requests.get(url)

        data = res.json()

        temperature = data["main"]["temp"]
        TempCelcius = round(temperature - 273.15)

        welcome.destroy()
        frame_w.destroy()

        #CityName
        cityLabel = Label(frame_main, text=city_entry.get().upper() , font=("Arial" , 18), bg="lightgrey")
        cityLabel.grid(row=0,columnspan=2, sticky="NSWE")

        #TempLabel
        tempLabel = Label(frame_main, text="Temperature: ", font=("Arial" , 16), bg="lightgrey")
        tempLabel.grid(row=1,column=0, sticky="NSE")

        #TempResult
        tempResult = Label(frame_main, text=(str(TempCelcius) + " ℃"), font=("Arial" , 16), bg="lightgrey")
        tempResult.grid(row=1,column=1, sticky="NSWE")

        wind_speed = round(data["wind"]["speed"] * 3.6)

        #WindLabel
        windLabel = Label(frame_main, text="Wind Speed: ", font=("Arial" , 16), bg="lightgrey")
        windLabel.grid(row=2,column=0, sticky="NSE")
        
        #WindResult
        windResult = Label(frame_main, text=(str(wind_speed) + " km/h"), font=("Arial" , 16), bg="lightgrey")
        windResult.grid(row=2,column=1, sticky="NSWE")

        main_weather = data["weather"][0]["main"]

        #MainLabel
        mainLabel = Label(frame_main, text="Main Weather: ", font=("Arial" , 16), bg="lightgrey")
        mainLabel.grid(row=3,column=0, sticky="NSWE")
        
        #MainResult
        mainResult = Label(frame_main, text=main_weather, font=("Arial" , 16), bg="lightgrey")
        mainResult.grid(row=3,column=1, sticky="NSWE")

        description = data["weather"][0]["description"]

        #DescLabel
        descLabel = Label(frame_main, text="Description: ", font=("Arial" , 16), bg="lightgrey")
        descLabel.grid(row=4,column=0, sticky="NSE")
        
        #DescResult
        descResult = Label(frame_main, text=description, font=("Arial" , 16), bg="lightgrey")
        descResult.grid(row=4,column=1, sticky="NSWE")

        city_entry.delete(0, END)

        conditions(description)

    except:
        messagebox.showerror("Invalid input", "Please give a city name only!") 
        city_entry.delete(0, END)
        if(not Frame.winfo_ismapped(frame_main)):
            createWelcomeFrame()
            return   



def search(self):

    if(city_entry.get() == ""):
        messagebox.showinfo("Info","Please enter a city!")
        return
    
    weatherCall()
           


#Frame Header
frame_header = Frame(master=root, padx=3, pady=3, height=50)
frame_header.place(x=300, y=20, anchor=N)

#Frame Bottom
frame_bottom = Frame(root, background="orange")
frame_bottom.place(x=300, y=440, anchor=CENTER)

#Frame Main
global frame_main
frame_main = Frame(root, padx=40 , pady= 10, bg="lightgrey")
frame_main.place(x=220, y=240, anchor=CENTER)

#Frame Img
frame_img = Frame(root)
frame_img.place(x=410, y=175)

createWelcomeFrame()

#Initialize imgLabel
imgLabel = Label(frame_img, padx=3,pady=3, bg="lightgrey")
imgLabel.pack()

#Clock
my_clock = Label(frame_bottom, text="Clock", width=30, font=("Arial" , 14), height=3)
my_clock.pack(padx=3, pady=3)

#Title
titleLabel = Label(frame_header, text="My Weather App", font=("Arial", 20))
titleLabel.grid(row=0, column=0, columnspan=4)

#City Label
city_label = Label(frame_header, text="Enter City:", font=("Arial", 10))
city_label.grid(row=1, column=0)

#Input Field
city_entry = Entry(frame_header, width=40)
city_entry.grid(row=1, column=1)
city_entry.bind('<Return>',search)

#Search button
search_btn = Button(frame_header, text="Search", command=search)
img = Image.open("images/search.png")
img2 = img.resize((30, 30), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(img2)
search_btn.config(image=tk_image)
search_btn.grid(row=1, column=3)

#Call clock method
clock()  


root.mainloop()