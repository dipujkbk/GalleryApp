from tkinter import *
from PIL import ImageTk,Image
import os

root = Tk()
root.title("Gallery")

my_image_names = os.listdir("photos") # it will return a list of file names(here images) present in the folder "photos"
image_list=[]

for i in range(len(my_image_names)):
    obj = ImageTk.PhotoImage(Image.open(".\\photos\\"+ my_image_names[i]))
    image_list.append(obj)

mylabel = Label(image=image_list[0]) # for very first time it will work
status = Label(root,text=f'Image 1 of {len(image_list)}',bd=1,relief=SUNKEN, anchor=E)

mylabel.grid(row=0,column=0,columnspan=3) # columnspan =3 becz ther are three buttons
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def  forward(image_num):
    global mylabel
    global button_forward
    global button_back
    global status

    mylabel.grid_forget() # to hide the previous image label
    mylabel= Label(image=image_list[image_num]) # it will show the current picture
    status = Label(text=f'Image {image_num + 1} of {len(image_list)}', relief=SUNKEN, anchor=E)

    button_forward = Button(root,text=">>",command=lambda: forward(image_num + 1))
    button_back = Button(root,text="<<",command=lambda: back(image_num-1))
    if image_num == (len(image_list)-1):
        button_forward = Button(root,text=">>",state=DISABLED)


    mylabel.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2,pady=10)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(image_num):
    global mylabel
    global button_forward
    global button_back
    global status

    mylabel.grid_forget()
    mylabel=Label(image=image_list[image_num])
    status = Label(text=f'Image {image_num + 1} of {len(image_list)}', relief=SUNKEN, anchor=E)

    button_forward = Button(root,text=">>",command=lambda: forward(image_num+1))
    button_back = Button(root,text="<<",command = lambda: back(image_num-1))
    if image_num == 0:
        button_back = Button(root,text="<<",state=DISABLED)
    
    mylabel.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2,pady=10)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    




# buttons for back ,forward and exit
button_back = Button(root,text="<<",state=DISABLED) # for the very first time it will be disbaled
button_exit = Button(root,text="EXIT PROGRAM",command = root.quit)
button_forward = Button(root,text=">>",command=lambda: forward(1))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)


root.mainloop()
