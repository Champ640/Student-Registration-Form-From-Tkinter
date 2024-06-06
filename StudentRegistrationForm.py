from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x650")
root.maxsize(500, 650)
root.minsize(500, 650)

def action():
    name = e1.get()
    age = e2.get()
    gen = gender.get()
    room = listroom.get()
    course1 = ""
    course2 = ""
    
    if var1.get() == "1":
        course1 = "Java"
    if var2.get() == "2":
        course2 = "Python"
    course3 = course1 + " " + course2
    
    # Check if all fields are filled
    if not name or not age or room == "Select your Room Type":
        messagebox.showerror("Input Error", "Please fill in all the fields.")
        return
    
    # Check if age is a valid number
    if not age.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid age.")
        return

    # If everything is fine, print the details
    print(name)
    print(age)
    print(gen)
    print(room)
    print(course3)

# Load and display the image
img = Image.open("stdreg.png")
img = img.resize((100, 100))
my = ImageTk.PhotoImage(img)
label = Label(image=my)
label.pack()

# Create and place labels and entry widgets
l1 = Label(root, text="Student Registration Panel", font="time 20 bold")
l1.place(x=75, y=120)
l2 = Label(root, text="Enter Name", font="time 15 bold")
l2.place(x=30, y=220)
e1 = Entry(root, width=30, bd=3)
e1.place(x=260, y=220)
l3 = Label(root, text="Age", font="time 15 bold")
l3.place(x=30, y=260)
e2 = Entry(root, width=30, bd=3)
e2.place(x=260, y=260)

# Gender selection
l4 = Label(root, text="Select Your Gender", font="time 15 bold")
l4.place(x=30, y=340)
gender = StringVar()
g1 = Radiobutton(root, text="Male", variable=gender, value="Male", font="time 15")
g1.select()
g1.place(x=260, y=340)
g2 = Radiobutton(root, text="Female", variable=gender, value="Female", font="time 15")
g2.place(x=360, y=340)

# Room selection
l5 = Label(root, text="Select Room", font="time 15 bold")
l5.place(x=30, y=390)
lists = ["Ac Room", "Non-Ac Room"]
listroom = StringVar(root)
listroom.set("Select your Room Type")
menu = OptionMenu(root, listroom, *lists)
menu.place(x=260, y=390, width=190)

# Course selection
l6 = Label(root, text="Select Course", font="time 15 bold")
l6.place(x=30, y=445)
var1 = StringVar()
var2 = StringVar()
l7 = Checkbutton(root, text="Java", variable=var1, onvalue="1", offvalue="0", font="time 15")
l7.place(x=260, y=445)
l8 = Checkbutton(root, text="Python", variable=var2, onvalue="2", offvalue="0", font="time 15")
l8.place(x=330, y=445)

# Buttons
button = Button(root, text="Submit", fg="white", bg="blue", font="time 15 bold", width=34, command=action)
button.place(x=32, y=500)
button2 = Button(root, text="Exit", fg="white", bg="red", font="time 15 bold", width=34, command=root.quit)
button2.place(x=32, y=570)

root.mainloop()
