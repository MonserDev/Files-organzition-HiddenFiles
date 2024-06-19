import fileorz as fz
import clipboard
import customtkinter as ctk
import os
from customtkinter import  CTkImage
from PIL import Image




def send():
    path = b1.get()
    try:
        match combo.get():
            case "PACKFILE":
                fz.packfile(path)
            case 'ONETIMES':
                fz.onetimes_pack(path)
            case 'UNPACK':
                fz.unpack_dir(path)
            case 'HIDDEN':
                fz.hidden(path)
            case 'SHOW':
                fz.show(path)
            case 'HIDDEN_ALL':
                fz.hidden_all(path)


        text("Susseses !")
    except IOError as e:
        text(e)

def text(massage):
    l2.pack(pady=4)
    text = ctk.CTkLabel(l2, text=massage)
    text.pack()

def get_clipborad():
    b1.delete(0, ctk.END)
    copy = clipboard.paste()
    b1.insert(0,copy)
def browsing():
    b1.delete(0, ctk.END)
    from tkinter.filedialog import askdirectory
    file = askdirectory()
    b1.insert(0,file)

def openfolder():
    os.startfile(b1.get())
def check_clipboard():
    if "\\" in clipboard.paste():
        b1.insert(0,clipboard.paste())

forcombo = ['PACKFILE','ONETIMES','UNPACK','HIDDEN','SHOW','HIDDEN_ALL']

root = ctk.CTk()
root.title("File organzisor")
root.geometry("600x500")
ctk.set_default_color_theme("green")

frame = ctk.CTkFrame(master=root)
frame.pack(padx=20,pady = 60 ,fill="both" ,expand=True)
l1 = ctk.CTkLabel(master=frame,text= 'Enter path',font=('Roboto',40))
l1.pack(pady = 20)



b1 = ctk.CTkEntry(frame,width=400)
b1.pack()

combo = ctk.CTkComboBox(master= frame,values = forcombo,font=('Roboto',16))
combo.pack(pady = 10)

openfile = ctk.CTkButton(master=frame,text = "Open folder" , command=lambda : openfolder() , font=('Roboto',16) )
openfile.pack(pady = 4)

browsing_b = ctk.CTkButton(master= frame,text = "Brows" , command= lambda : browsing(),font=('Roboto',16))
browsing_b.pack(pady = 4) ,check_clipboard()

copy_b = ctk.CTkButton(master=frame,text = '' , command= lambda:get_clipborad(),image=CTkImage(Image.open(r"photo/clipboard.png")),width=30,height=30)
copy_b.place(relx=0.87, rely=0.23)

l2 = ctk.CTkScrollableFrame(frame,width=500)


bu1  =ctk.CTkButton(master=frame,text = "Organized !",command= lambda:send(),font=('Roboto',16))
bu1.pack(pady = 4)

root.mainloop()