from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer Program")

showingNow = 0

# Functions

def ForwardButton():
    global showingNow
    global my_imageshower
    my_imageshower.grid_forget()
    showingNow = showingNow + 1
    my_imageshower = Label(image=image_list[showingNow])
    my_imageshower.grid(row=0, column=0, columnspan=3)
    CheckWhere()


def BackButton():
    global showingNow
    global my_imageshower
    my_imageshower.grid_forget()
    showingNow = showingNow - 1
    my_imageshower = Label(image=image_list[showingNow])
    my_imageshower.grid(row=0, column=0, columnspan=3)
    CheckWhere()


def CheckWhere():
    global showingNow
    global backButton
    if showingNow < 1 :
        backButton.config(state=DISABLED)
    else:
        backButton.config(state=NORMAL)
    if (showingNow + 2) > (len(image_list)):
        forwardButton.config(state=DISABLED)
    else:
        forwardButton.config(state=NORMAL)



my_image1 = ImageTk.PhotoImage(Image.open("GUI/Image1.png"))
my_image2 = ImageTk.PhotoImage(Image.open("GUI/Image2.png"))
my_image3 = ImageTk.PhotoImage(Image.open("GUI/Image3.png"))
my_image4 = ImageTk.PhotoImage(Image.open("GUI/Image4.png"))
my_image5 = ImageTk.PhotoImage(Image.open("GUI/Image5.png"))




#Buttons
backButton = Button(root, text="<-", padx = 91, pady= 20 ,command=BackButton)
forwardButton = Button(root, text="->", padx = 91, pady= 20 ,command=ForwardButton)
quitButton = Button(root, text="EXIT PROGRAM", padx = 91, pady= 20 ,command=root.quit)
#Disable backButton on run
backButton.config(state=DISABLED)

#Buttons Placement
backButton.grid(row=2, column=0)
quitButton.grid(row=2, column=1)
forwardButton.grid(row=2, column=2)


# Image List
image_list = [my_image1,my_image2,my_image3,my_image4,my_image5]



my_imageshower = Label(image=image_list[showingNow])
my_imageshower.grid(row=0, column=0, columnspan=3)














root.mainloop()