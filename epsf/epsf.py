import tkinter as  tk
from PIL import Image as img
from PIL import ImageTk as imgtk
import pymysql as mysql
import easygui as gui
from tkinter import ttk
#design
##func
main=tk.Tk()
def insert():
    if name.get()=="" or id.get()=="" or email.get()=="" or phone.get()=="" or address.get()=="" or facebook.get()=="" or points.get()=="":
        gui.msgbox(title="Alert",msg="information missing")
        return 0
    con=mysql.Connect(host="localhost",user="root", password="",db="epsf")
    exe=con.cursor()
    exe.execute("""INSERT INTO epsf(name,id,email,phone,address,facebook,points,rank) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s") """%(name.get(),id.get(),email.get(),phone.get(),address.get(),facebook.get(),points.get(),"new"))
    gui.msgbox("insert done")
def findthis():
    if f_d.get()=="" :
        gui.msgbox(title="Alert",msg="the find text is empty")
        return 0
    con = mysql.Connect(host="localhost", user="root", password="", db="epsf")
    exe = con.cursor()
    exe.execute(""" SELECT * FROM epsf WHERE name="%s" OR id="%s" """%(f_d.get(),f_d.get()))
    result=exe.fetchall()
    tree = ttk.Treeview(columns=("id", "email", "phone", "address", "facebook", "points", "rank"))
    tree.column('rank',width=100)
    tree.column('points', width=90)
    def dys():
        tree.destroy()


    btm=tk.Button(text="delete this result", command=dys).place(x=0,y=450)
    for row in result:
        tree.heading("#0",text="name")
        tree.heading("id", text="id")
        tree.heading("email",text="email")
        tree.heading("phone", text="phone")
        tree.heading("address", text="address")
        tree.heading("facebook", text="facebook")
        tree.heading("points", text="points")
        tree.heading("rank", text="rank")
        tree.insert(parent="",index=0,text=row[0],value=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        tree.place(x=0,y=500)

        con.close()
def remove():
    if f_d.get()=="":
        gui.msgbox(title="Alert",msg="missing information")
        return 0
    con = mysql.Connect(host="localhost", user="root", password="", db="epsf")
    exe = con.cursor()
    exe.execute("""DELETE FROM `epsf` WHERE `name` ="%s" OR `id`="%s" """ % (f_d.get(), f_d.get()))
    gui.msgbox(title="Alert",msg="delete done")
    con.close()
def modify():
    if change.get()=="" or value.get()=="" or id_mod.get()=="":
        gui.msgbox(title="Alert",msg="information missing")
        return 0

    con = mysql.Connect(host="localhost", user="root", password="", db="epsf")
    exe = con.cursor()
    exe.execute(""" UPDATE epsf SET `%s`="%s"  WHERE name="%s" OR id="%s"  """ % (change.get(),value.get(),id_mod.get(),id_mod.get()))
    gui.msgbox("modify done")
    con.close()


main.title("epsf main table")
bg_img=img.open("bg.png")
bg=imgtk.PhotoImage(bg_img)
tk.Label(image=bg).pack(expand=True)

##new commer
tk.Label(text="add new member",font=20,border=0).place(x=790,y=0)
#email
tk.Label(text="email",font=30,border=0).place(x=690,y=50)
email=tk.Entry(width=20,font=33)
email.bind("<Return>",insert)
email.place(x=800,y=50)
#id
tk.Label(text="id",font=30,border=0).place(x=690,y=100)
id = tk.Entry(width=20,font=33)
id.bind("<Return>",insert)
id.place(x=800,y=100)
##phone
tk.Label(text="phone",font=30,border=0).place(x=690,y=150)
phone=tk.Entry(width=20,font=33)
phone.bind("<Return>",insert)
phone.place(x=800,y=150)
#name
tk.Label(text="name",font=30,border=0).place(x=690,y=200)
name=tk.Entry(width=20,font=33)
name.bind("<Return>",insert)
name.place(x=800,y=200)
# address
tk.Label(text="address",font=30,border=0).place(x=690,y=250)
address=tk.Entry(width=20,font=33)
address.bind("<Return>",insert)
address.place(x=800,y=250)
#facebook
tk.Label(text="facebook",font=30,border=0).place(x=690,y=300)
facebook=tk.Entry(width=20,font=33)
facebook.bind("<Return>",insert)
facebook.place(x=800,y=300)
#points
tk.Label(text="points",font=30,border=0).place(x=690,y=350)
points=tk.Entry(width=20,font=33)
points.bind("<Return>",insert)
points.place(x=800,y=350)
#btm
btm_img=img.open("add.png")
show1=imgtk.PhotoImage(btm_img)
tk.Button(image=show1,border=0,command=insert).place(x=800,y=400)

###############
#find\delete
tk.Label(text="[ find / delete ]",font=30,bg="white").place(x=140,y=0)
tk.Label(text="id or name",font=30).place(x=140,y=50)
f_d = tk.Entry(width=20,font=33)
f_d.bind("<Return>",findthis)
f_d.bind("<Return>",remove)
f_d.place(x=100,y=100)
#find
find_img = img.open("btm_find.png")
find = imgtk.PhotoImage(find_img)
tk.Button(image=find,border=0,command=findthis).place(x=100,y=150)
#delete
delete_img = img.open("delete.png")
delete = imgtk.PhotoImage(delete_img)
tk.Button(image=delete,border=0,command=remove).place(x=200,y=150)
##########
##### modify
tk.Label(text="options",font=30,border=0).place(x=1250,y=0)
# id_mod
tk.Label(text="id / name",font=30,border=0).place(x=1250,y=30)
id_mod=tk.Entry(width=20,font=33)
id_mod.bind("<Return>",modify)
id_mod.place(x=1200,y=60)
#what to change
tk.Label(text="what do u want to change",font=30,border=0).place(x=1200,y=90)
change=tk.Entry(width=20,font=33)
change.bind("<Return>",modify)
change.place(x=1200,y=120)
#value
tk.Label(text="to value",font=30,border=0).place(x=1250,y=150)
value=tk.Entry(width=20,font=33)
value.bind("<Return>",modify)
value.place(x=1200,y=180)
mod_img=img.open("reload.png")
mod=imgtk.PhotoImage(mod_img)
tk.Button(image=mod,border=0,command=modify).place(x=1230,y=210)


main.mainloop()