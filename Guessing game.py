from tkinter import *
import random
import threading
from pygame import mixer
import tkinter.messagebox as tkmsg

screen = Tk()
screen.geometry("500x500")
screen.title("Guessing Game")
screen.maxsize(500,500)
screen.minsize(500,500)
mixer.init()

def music_play():
    mixer.music.load('bgm.mp3')
    mixer.music.play(100)


t1 = threading.Thread(target=music_play)
t1.start()



def retry():
    global totl_chnc_var
    global result_status
    global screen1
    global total_chance
    global number
    global entr_num
    screen1.destroy()
    total_chance = 10

    number = random.randint(1, 100)

    main_lbl = Label(screen, text="Welcome to Number Guessing Game", font="calibri 20 bold", pady=30, bg = 'cyan', fg = 'red').update()

    Label(screen, text='Total Chances Left', font="calibri 15 bold", pady=20, bg = 'cyan').update()
    totl_chnc_var.set("10")

    chance_lbl = Label(screen, textvariable=totl_chnc_var, fg="red", font='calibri 20 bold', pady=20, bg = 'cyan').update()

    Label(screen, text='Guess a number between 1 to 100', font="calibri 15 bold", pady=20, bg = 'cyan').update()
    result_status.set("lets go")
    result = Label(screen, textvariable=result_status, fg="green", font="calibri 15 bold", pady=20, bg = 'cyan').update()
    entr_num.delete(0, END)

def restart():
    global totl_chnc_var
    global result_status
    global total_chance
    global number
    global entr_num

    total_chance = 10

    number = random.randint(1, 100)

    main_lbl = Label(screen, text="Welcome to Number Guessing Game", font="calibri 20 bold", pady=30, bg='cyan',
                     fg='red').update()

    Label(screen, text='Total Chances Left', font="calibri 15 bold", pady=20, bg='cyan').update()
    totl_chnc_var.set("10")

    chance_lbl = Label(screen, textvariable=totl_chnc_var, fg="red", font='calibri 20 bold', pady=20,
                       bg='cyan').update()

    Label(screen, text='Guess a number between 1 to 100', font="calibri 15 bold", pady=20, bg='cyan').update()
    result_status.set("lets go")
    result = Label(screen, textvariable=result_status, fg="green", font="calibri 15 bold", pady=20, bg='cyan').update()
    entr_num.delete(0, END)



def won():
    global total_chance
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("500x500")
    screen1.maxsize(500, 500)
    screen1.minsize(500, 500)
    screen1.title("You Won")
    screen1.config(bg ='green')


    used_chance = StringVar()
    used_chance.set(f"You used {10 - total_chance} chances")
    Label(screen1, text = "Congratulations You have guessed correctly", font = "calibri 15 bold", fg = 'white', bg = 'green', pady = 40).pack()
    Label(screen1,textvariable = used_chance , font = "calibri 15 bold", bg = 'green', fg = 'white', pady = 40).pack()

    used_chance = 10 - total_chance

    if used_chance <= 4:
        status = Label(screen1, text = "Sir.. You are a Pro :)", font = "calibri 15 bold", pady = 30, fg = 'cyan', bg = "green").pack()

    elif used_chance <= 7:
        status = Label(screen1, text="Average Player :)", font="calibri 15 bold", pady=30, fg = 'orange', bg = "green").pack()

    else:
        status = Label(screen1, text="Sorry you are Noob :(", font="calibri 15 bold", pady=30, fg='red', bg="green").pack()

    screen1.wm_iconbitmap('logo.ico')
    Button(screen1, text = "Retry", command = retry, pady = 10, padx = 15, fg = 'white', bg = 'red').pack(pady = 40)
    Button(screen1, text="Exit", command=quitf, pady=10, padx=20, bg='red', fg='white').pack(pady=0)


def compare(event):
    global number
    global entered_num
    global result_status
    global total_chance
    total_chance -=1
    global totl_chnc_var
    global entr_num
    if total_chance >= 1:


        totl_chnc_var.set(total_chance)
        chance_lbl = Label(screen, textvariable=totl_chnc_var, fg="red", font='calibri 20 bold', pady = 20).update()


        entrered_val = int(entered_num.get())

        if number == entrered_val:
            result_status.set("Great you got it..")
            result = Label(screen, textvariable = result_status, fg = "green", font = "calibri 15 bold", pady = 20).update()
            won()

        elif number < entrered_val:
            result_status.set("You entered larger number.. try again")
            result = Label(screen, textvariable = result_status, fg = "green", font = "calibri 15 bold", pady = 20).update()

        elif number > entrered_val:
            result_status.set("You entered lesser number.. try again")
            result = Label(screen, textvariable=result_status, fg="green", font="calibri 15 bold", pady = 20).update()

    else:
        game_over()
    entr_num.delete(0, END)
    

def game_over():
    global total_chance
    global screen1
    global number
    screen1 = Toplevel(screen)
    screen1.geometry("500x500")
    screen1.maxsize(500, 500)
    screen1.minsize(500, 500)
    screen1.title("You Lost")
    screen1.config(bg='red')

    used_chance = StringVar()
    used_chance.set(f"You used all {10 - total_chance} chances :(")
    Label(screen1, text="Better luck next time", font="calibri 15 bold", fg = 'white', bg = 'red', pady = 40).pack()
    Label(screen1, textvariable=used_chance, font="calibri 15 bold", fg = 'white', bg = 'red', pady = 30).pack()
    Label(screen1, text = f"Answer was {number}", font="calibri 15 bold", fg = 'white', bg = 'red', pady = 30).pack()
    Button(screen1, text="Retry", command=retry, pady = 10, padx = 15, bg = 'green', fg = 'white').pack( pady = 40)
    Button(screen1, text="Exit", command=quitf, pady = 10, padx = 20, bg = 'cyan', fg = 'red').pack( pady = 0)
    screen1.wm_iconbitmap('logo.ico')


def help1():
    tkmsg.showinfo("Help Center", "This is a number guessing game in which you have to guess a number between 1 to 100... You have only 10 chances\n ThankYou")

def quitf():
    global screen
    screen.destroy()

def about():
    tkmsg.showinfo("About Us", "This game is developed by student of MCAET\n\nAditya Yadav\n\nE-11077/19 \nThankYou...")


def music_off():
    mixer.music.pause()

menubar = Menu(screen)
mainmenu = Menu(menubar)

mainmenu.add_command(label = "Help", command = help1)
mainmenu.add_command(label = "About Us", command =about)

menubar.add_cascade(label = "Help", menu = mainmenu)

exit_menu = Menu(menubar)
exit_menu.add_command(label = "Exit", command = quitf)
menubar.add_cascade(label = 'Quit', menu = exit_menu)

setting_menu = Menu(menubar)
setting_menu.add_command(label = "Music off", command = music_off)
setting_menu.add_command(label = "Music on", command= music_play)

menubar.add_cascade(label = "Settings", menu = setting_menu)

screen.config(menu=menubar)


main_lbl = Label(screen, text = "Welcome to Number Guessing Game", font = "calibri 20 bold", pady = 30, bg = 'cyan', fg = "red").pack()
entered_num = StringVar()

total_chance = 10
Label(screen, text = 'Total Chances Left', font = "calibri 15 bold", pady = 20, bg = 'cyan').pack()


totl_chnc_var = StringVar()
totl_chnc_var.set("10")

chance_lbl = Label(screen, textvariable = totl_chnc_var, fg = "red", font = 'calibri 20 bold', pady = 20, bg = 'cyan').pack()

Label(screen, text='Guess a number between 1 to 100', font="calibri 15 bold", pady=20, bg = 'cyan').pack()

number = random.randint(1, 100)

entered_num = StringVar()

entr_num = Entry(screen, textvariable = entered_num, font = "calibri 25 bold", fg = 'brown', borderwidth = 5, relief = GROOVE, justify = CENTER)
entr_num.pack( pady = 20)
entr_num.focus_set()

entr_num.bind("<Return>", compare)

result_status = StringVar()
result_status.set("Lets go")
result = Label(screen, textvariable = result_status, fg = "green", font = "calibri 15 bold", pady = 5, bg = 'cyan').pack()
Button(screen, text = "Restart", command = restart, pady = 5, padx = 15, fg = 'white', bg = 'red').pack(pady = 0)

screen.config(bg = 'cyan', borderwidth = 7, relief = GROOVE)
screen.wm_iconbitmap('logo.ico')
screen.mainloop()


