from tkinter import *
n = 0
points = int(n)
y = int(1)

def clickbtn_1():
    global y
    global points
    points += y
    print(points)

def clickupg_1():
    global y
    global points
    if points < 50:
        print("Sorry you don't have enough points -", points)
    else:
        points -= 50
        print("Thank you for your purchase, your points are now -", points)
        y += 1
        

def clickupg_2():
     global y
     global points
if points < 100:
        print("Sorry you don't have enough points -", points)
else:
        points -= 100
        print("Thank you for your purchase, your points are now -", points)
        y += 2



window = Tk()

btn_1 = Button(window,
                text="Click Me!",
                command=clickbtn_1,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black")

btn_1.pack()

upg_1 = Button(window,
                text="Bigger Clicks I - 50 Points",
                command=clickupg_1,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black")

upg_1.pack()

upg_2 = Button(window,
                text="Bigger Clicks II - 100 Points",
                command=clickupg_1,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black")

upg_2.pack()


window.mainloop()
