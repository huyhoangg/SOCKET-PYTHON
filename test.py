
from tkinter import *
def register():
    global screenRegis
    screenRegis = Toplevel(screen)
    screenRegis.title("Register")
    screenRegis.geometry("400x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screenRegis, text="Register Form", bg="grey", font=("Calibri", 13), width="25").pack()
    Label(screenRegis, text="").pack()
    Label(screenRegis, text="").pack()

    username_lable = Label(screenRegis, text="Username  ")
    username_lable.pack()

    username_entry = Entry(screenRegis, textvariable=username, width="25")
    username_entry.pack()
    Label(screenRegis, text="").pack()

    password_lable = Label(screenRegis, text="Password  ")

    password_lable.pack()
    password_entry = Entry(screenRegis, textvariable=password, width="25")
    password_entry.pack()
    password_lable.pack()
    Label(screenRegis, text="").pack()
    Button(screenRegis, text="Register", width=10, height=1, bg="#0d8bf0", fg="black").pack()

def cmd():
    if oldPass.get()== "1":
        return True
    else:
        return False


def showNoteGUI():
    global show_note_Scr
    show_note_Scr = Toplevel(Hscreen)
    show_note_Scr.title("See your friend status ")
    show_note_Scr.geometry("400x300")
    global who
    who = StringVar()

    global who_entry

    Label(show_note_Scr, text="See your friend status ", bg="cyan2", font=("Calibri", 13), width="25").pack()
    Label(show_note_Scr, text="").pack()
    Label(show_note_Scr, text="who are you looking for ").pack()
    who_entry = Entry(show_note_Scr, textvariable=who, width="35")
    who_entry.pack()

    Button(show_note_Scr, text = "Check").place(x= 330, y=64)

    Button(show_note_Scr, text="Watch",state="disable", width=20, height=1, bg="maroon1", fg="white").pack(pady= 10)


def homepage(user):
    global Hscreen
    Hscreen = Tk()
    Hscreen.geometry("800x600")
    Hscreen.title("Homepage")

    Label(text="Welcome to game, "+user, bg= "MediumOrchid1",fg="turquoise1",font=("Calibri", 19),height=3 ,width=600).pack()
    Label(bg= "purple1",fg="black",height=10 ,width=600).pack()
    Label(bg= "mediumOrchid4",fg="black",height=12 ,width=600).pack()
    Label(bg= "dark slate blue",fg="black",height=10 ,width=600).pack()


    Label(text="Check out your information",bg="PaleVioletRed1",font=("Calibri", 15)).place(x=10,y=110)
    Label(text="Looking for someone ?",bg="tomato2",font=("Calibri", 15)).place(x=10,y=270)

    Button(text="Change Password", bg="darkorchid1", fg="gold", height="2", width="20", command = showNoteGUI).place(x=20, y= 170)
    Button(text="Fullname",bg="darkorchid2",fg="gold", height="2", width="20").place(x=220, y= 170)
    Button(text="Birthday",bg="darkorchid3",fg="gold", height="2", width="20").place(x=420, y= 170)
    Button(text="Note",bg="darkorchid4",fg="gold", height="2", width="20").place(x=620, y= 170)

    Button(text="Show fullname", bg="maroon1",fg="cyan", height="2", width="20").place(x=20, y=370)
    Button(text="Show birthday", bg="maroon2",fg="cyan", height="2", width="20").place(x=220, y=370)
    Button(text="Show point", bg="maroon3",fg="cyan", height="2", width="20").place(x=420, y=370)
    Button(text="Show note", bg="violetred3",fg="cyan", height="2", width="20").place(x=620, y=370)

    Button(text="Find your friend", bg="maroon2", fg="cyan", height="2", width="20").place(x=130, y=310)
    Button(text="Find online user", bg="maroon3", fg="cyan", height="2", width="20").place(x=330, y=310)
    Button(text="Show everything", bg="violetred3", fg="cyan", height="2", width="20").place(x=530, y=310)

    Hscreen.mainloop()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x300")
    screen.title("Account Login")
    Label(text="Select Your Choice", bg="#f96854", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="35").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="35", command=register).pack()
    Label(text="").pack()

    screen.mainloop()

user = "hoang"
homepage(user)
