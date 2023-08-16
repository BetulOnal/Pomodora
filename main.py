from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_count = 0
close= None
click =True

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(close)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        timer(long_break)
        label.config(text="Long Break", fg= RED)
    elif reps % 2 == 0:
        global check_count
        check_count += 1
        timer(short_break)
        label.config(text="Short Break", fg=PINK)
    else:
        timer(work_sec)
        label.config(text="Study Time", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    #burda önce canvas a dokundum. sonra canvas'ın hangi ögesinde değişiklik yapacaksam onu belirttim.
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global close
        close=window.after(1000, timer, count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark +="✅"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)


#resmi görüntüledik(tomatesi)
canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)

#resmin içine metin yazdık. canvas ın içine
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=1, column=1)


label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,40), bg=YELLOW)
label.grid(row=0, column=1)

button_s = Button(text="Start", bg=YELLOW, command=start_timer)
button_s.grid(row=2, column=0)
button_r= Button(text="Reset", command=reset)
button_r.grid(row=2,column=2)



check_mark = Label(text="")
check_mark.grid(row=3,column=1)

window.mainloop()