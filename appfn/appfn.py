import requests
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import urllib.request as urllib2
import time
import tkinter.messagebox
from tkinter.simpledialog import askstring
window = tk.Tk()

def styleinput(styleinfo):
    try:
        res = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={styleinfo}&language=it&searchLanguage=en&matchMethod=full')
        jsonres = res.json()
        tittleitem = tk.Label(text=jsonres['data'][0]['name'], width=10, height=10)
        tittleitemstyle = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        tittleitem.configure(font=tittleitemstyle)

        #image

        imageopen = Image.open(urllib2.urlopen(jsonres['data'][0]['images']['smallIcon']))
        imageset = ImageTk.PhotoImage(imageopen)

        labelimage = tk.Label(image=imageset)
        labelimage.image = imageset
        labelimage.place(x=450, y=150)

        #description
        description = tk.Label(text="descrizione:" +jsonres['data'][0]['description'])
        descriptionstyle = tkFont.Font(family="Raleway", size=12, weight="normal")
        description.configure(font=descriptionstyle)
        #other
        timeinsert = tk.Label( text="▶data inserimento:" + jsonres['data'][0]['introduction']['text'], height=5)
        timeinsertstyle = tkFont.Font(family="Raleway", size=12, weight="normal")
        timeinsert.configure(font=timeinsertstyle)
        
        type = tk.Label(text="▶tipo:"+jsonres['data'][0]['type']['value'])
        typestyle=tkFont.Font(family="Raleway", size=12, weight="normal")
        type.configure(font=typestyle)


        rarity = tk.Label(text="▶rarita:" +jsonres['data'][0]['rarity']['value'])
        raritystyle=tkFont.Font(family="Raleway", size=12, weight="normal")
        rarity.configure(font=raritystyle)

        set = tk.Label(text="▶set:"+jsonres['data'][0]['set']['value'])
        setstyle=tkFont.Font(family="Raleway", size=12, weight="normal")
        set.configure(font=setstyle)

        pathfn = tk.Label(text="▶path:"+jsonres['data'][0]['path'])
        pathfnstyle=tkFont.Font(family="Raleway", size=12, weight="normal")
        pathfn.configure(font=pathfnstyle)

        id = tk.Label(text="▶id oggetto:"+jsonres['data'][0]['id'])
        idstyle=tkFont.Font(family="Raleway", size=12, weight="normal")
        id.configure(font=idstyle)
        tittleitem.pack()
        description.pack()
        timeinsert.pack()
        type.pack()
        rarity.pack()
        set.pack()
        pathfn.pack()
        id.pack()
    except:
        tkinter.messagebox.showerror("errore ","chiusura programma")
        time.sleep(5)
        window.destroy()
       
       

window.title("fortnite app")
style=styleinput(askstring('hello', 'insert items  name?'))
if style=="Cancel":
    window.destroy()
  
else:
   
window.mainloop()
