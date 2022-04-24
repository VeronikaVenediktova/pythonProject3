import tkinter as tk
import random
import time
from datetime import date

click_count = 0
false_click_count = 0
button_color = "red"
list_average = []
time_start = time.time()
var_average = 0
var_minimum = 0.0
click_ratio = 0
button_state = "active"


def send_message():
    global false_click_count, click_count, click_ratio, var_average, list_average, var_minimum
    if button_color == "red":
        time_click = time.time()
        var = time_click - time_start
        result_1.config(text="Speed reaction is ")
        result_2.config(text=var)
        click_count += 1
        list_average.append(var)

        var_average = sum(list_average)/len(list_average)         # считаем среднее время
        var_minimum = min(list_average)                           # считаем минимальное время
        # return var_average

    else:
        result_1.config(text="False click")
        false_click_count += 1
        result_2.config(text=false_click_count)
    click_ratio = click_count/(click_count+false_click_count)      # считаем процентное соотношение ложных и правильных нажатий
    return


def timer_update():
    global time_start,  button_color
    time_start = time.time()
    button_color = random.choice(colors)
    button.config(bg=button_color)
    window.after(random.randint(500, 2500), timer_update)


window = tk.Tk()
colors = ["black", 'white', 'yellow', 'red', 'blue', 'green']
window.geometry("300x300")
label = tk.Label(
    text="Check your reaction",
    font=("Arial", 12),
    foreground="white",
    bg="black",
    width=100,
    height=3
)

label_name = tk.Label(
    text="Enter your name",
    font=("Arial", 12),
    foreground="black",
    background="white",
    width=100,
    height=2
)
entry = tk.Entry()
frame = tk.Frame(
    height=10
)


def enter_name():
    global name, button_state
    name = entry.get()
    if len(name) >= 2 and name.isalpha():
        button_state = "disabled"
        return name


def save():
    global button_state # функция сохранения в файл
    if click_ratio >= 0.5:
        text = f"{name} {var_minimum} {var_average} {date.today()}\n"
        with open("text.txt", "a") as f:
            f.write(text)
    # button_state = "active"


botton_start = tk.Button(
    state=button_state,
    text="START",
    bg="blue",
    fg="yellow",
    width=10,
    height=1,
    command=enter_name
)

frame_2 = tk.Frame(
    height=10
)
botton_save = tk.Button(
    text="SAVE",
    bg="Green",
    fg="black",
    width=10,
    height=1,
    command=save
)

frame_1 = tk.Frame(
    height=10
)
button = tk.Button(
    text="Click me!",
    bg=button_color,
    fg="yellow",
    width=10,
    height=3,
    command=send_message
)

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="green",
    font=("Arial", 14))

result_2 = tk.Label(
    foreground="green",
    font=("Arial", 14)
)

for c in window.children:
    print(c)
    window.children[c].pack()

window.after(random.randint(500, 2500), timer_update)

window.mainloop()

