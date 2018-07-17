from tkinter import *


def show():
    print("hello user")



window = tk()

window .  _title("book directory")


labell = label(window,text="title")
labell.grid(row= 0, column= 0)

label2 =label(window,text="author")
label2.grid(row = 0,column = 2)

label3 = label(window, text = "year")
label3.grid(row = 1, column = 0)

label4 = label(window, text ="isbn")
label4.grid(row =1,column =2)

title_text = StringVar()
entry1 = Entry(window , textvariale = title_text)
entry1.grid( row = 0,column = 1)

author_text = StringVar()
entry2 = Entry(window . textvariable = author_text)
entry2.grid(row =0,column=3)

year_text=StringVar()
entry3 = Entry(window,textvariable = year_text)
entry3.grid(row =1 ,column =1)

isbn_text=StringVar()
entry4 =Entery(window, textvariable =isbn_text)
entry4.grid(row =1, column =3)



listing =listbox(window ,height =6 ,width =25)
listing.grid(row =2, column =0,rowspan =6 ,columnspan =2)

scrollbar = scrollbar(window)
scroller.grid(row = 2, column = 2,rowspan =6)


button1 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button1.grid(row =2,column =3)

button2 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button2.grid(row =3,column =3)

button3 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button3.grid(row =4,column =3)

button4 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button4.grid(row =5,column =3)

button5 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button5.grid(row =6,column =3)

button6 = Button(window,
                 text ="view ALL",
                 width =12,
                 command = show)
button6.grid(row =7,column =3)

window.mainloop()