from tkinter import *
from random import choice


win = Tk()
win.geometry('650x300+400+220')
win.title('First project')
win_bg  = '#ffffff'
win.configure(bg= win_bg)

Default_Color = '#ffffff'
rgb_color = ''

def change_color():
    rgb_color = ""
    for i in range (6):
        rgb_color += choice('0123456789ABCDEF')
    rgb_color = '#' + rgb_color
    print(rgb_color)
    win.configure(bg=rgb_color)
    lbl_1.configure(bg=rgb_color)
    lbl_2.configure(bg=rgb_color)
    lbl_3.configure(text= rgb_color,bg=rgb_color)
    



def Reset_Color():
    win.configure(bg=Default_Color)
    lbl_1.configure(bg=Default_Color)
    lbl_2.configure(bg=Default_Color)
    lbl_3.configure(text=Default_Color ,bg=Default_Color)

# print(rgb_color)
lbl_1 = Label(win,text= 'Welcome', font= ('arial', 34 ),bg= win_bg,padx=20, pady= 15)

# lbl_1.place(x= 100, y= 40)

lbl_1.grid(row=0, column=0)

lbl_2 = Label(win,text= 'Pouria .Habibi',font= 'arial 24' , bg=win_bg)

# lbl_2.place(x = 250,y = 40)

lbl_2.grid(row= 0 , column= 1)

lbl_3= Label(win,text = Default_Color,font='arial 24',)

lbl_3.place(x=200,y=200)

btn_1 = Button(win, text='Start', command= change_color,width=50)
btn_1.grid(row=1,column=0)
pic = PhotoImage(file='C:/Users/Sali/Pictures/tree_25px.png')
btn_1.config(image= pic, compound= TOP )
# btn_1.config(compound= TOP )



btn_2 = Button(win,text ='reset color', command=Reset_Color)

btn_2.grid(row=1,column=1)




win.mainloop()



