import tkinter as tk
import pyshorteners as ps
import pyperclip
window= tk.Tk()
window.geometry("500x250")
window.config(bg="skyblue")
def Shorturl():
    u1=url.get()
    s= ps.Shortener()
    a =s.tinyurl.short(u1)
    
    l1= tk.Label(f1,text="Shortened URL",font="bold")
    l1.place(relx=0.35,rely=0.1)
    
    u1_w= tk.StringVar()
    u1_w.set(a)
    u1= tk.Entry(f1,width=50,textvariable= u1_w)
    u1.place(relx=0.1,rely=0.3)
    
    b2= tk.Button(f1,text="Copy URL",command= pyperclip.copy(a))
    b2.place(relx=0.4,rely=0.55)

l1= tk.Label(window,text="URL: ",bg="skyblue")
l1.place(relx=0.1,rely=0.2)

url= tk.StringVar()
u= tk.Entry(window,width=50,textvariable= url )
u.place(relx=0.2,rely=0.2)

gb= tk.Button(window,text="Go",command= Shorturl)
gb.place(relx=0.85,rely=0.2)

f1= tk.Frame(window,width=400, height=130,bd=3, relief="ridge")
f1.place(relx=0.1,rely=0.4)

window.mainloop()