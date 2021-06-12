import tkinter as tk
import requests as req
import Constants as cs
def OnClick():
    response= req.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.get()}&appid={cs.Constants.API_KEY}")
    reout=response.json()
    print(response.content)
    print(type(reout))
    print(list(reout.keys()))
    cityname=reout['name']
    country=reout["sys"]['country']
    temp_kel=reout['main']['temp']
    vis=reout["visibility"]
    wea=reout["weather"][0]["main"]
    tup=(cityname, country, vis, wea, temp_kel)
    loc=tk.Label(window, text='{}, {}'.format(cityname, country), font="Arial")
    loc.pack()
    temp_c=tk.Label(window, text='{}'.format(temp_kel-273.15))
    temp_c.pack()
    weat=tk.Label(window, text='{}'.format(wea))
    weat.pack()
    visi=tk.Label(window, text='{}'.format(vis))
    visi.pack()
    print(tup)

window= tk.Tk()
window.title("Weather")
city= tk.Entry(window, font='Arial')
city.pack()
but= tk.Button(window, text='Enter', fg='blue', command=OnClick)
but.pack()

window.mainloop()
