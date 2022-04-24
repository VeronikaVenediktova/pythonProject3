import tkinter as tk
import random
import time
from datetime import date

button_state = "normal"
click_count = 0
false_click_count = 0
button_color = "red"
list_average = []
time_start = time.time()
var_average = 0
var_minimum = 0.0
click_ratio = 0


def send_message():
    global false_click_count, click_count, click_ratio, var_average, list_average, var_minimum
    if button_color == "red":
        time_click = time.time()
        var = time_click - time_start
        result_1.config(text="Speed reaction is ")
        result_2.config(text=var)
        click_count += 1
        list_average.append(var)

        var_average = sum(list_average) / len(list_average)  # считаем среднее время
        var_minimum = min(list_average)  # считаем минимальное время ложных и правильных нажатий

    else:
        result_1.config(text="False click")
        false_click_count += 1
        result_2.config(text=false_click_count)
    click_ratio = click_count / (click_count + false_click_count)  # считаем процентное соотношение
    return

def timer_update():
    global time_start, button_color
    time_start = time.time()
    button_color = random.choice(colors)
    button_click.config(bg=button_color)
    window.after(random.randint(500, 2500), timer_update)


window = tk.Tk()
colors = ["black", 'white', 'yellow', 'red', 'blue', 'green']
window.geometry("480x480")
label = tk.Label(
    text="Check your reaction",
    font=("Arial", 12),
    foreground="white",
    bg="black",
    width=100,
    height=3
)

label_name = tk.Label(
    state=button_state,
    text="Enter your name",
    font=("Arial", 12),
    foreground="black",
    background="white",
    width=200,
    height=2
)
entry = tk.Entry()
frame = tk.Frame(
    height=10
)


def enter_name():
    global name
    name = entry.get()
    if len(name) >= 2 and name.isalpha():
        button_start.config(state="disabled")
        button_click.config(state="normal")
        button_save.config(state="normal")

    return


def save():  # функция сохранения в файл
    global button_state
    if click_ratio >= 0.5:
        text = f"{name} {var_minimum} {var_average} {date.today()}\n"
        with open("text.txt", "a") as f:
            f.write(text)
        button_state = "normal"


button_start = tk.Button(
    text="START",
    bg="blue",
    fg="yellow",
    width=40,
    height=1,
    command=enter_name
)

frame_2 = tk.Frame(
    height=10
)
button_save = tk.Button(
    state="disabled",
    text="SAVE",
    bg="Green",
    fg="black",
    width=40,
    height=1,
    command=save
)

frame_1 = tk.Frame(
    height=10
)
button_click = tk.Button(
    state="disabled",
    text="Click me!",
    bg=button_color,
    fg="yellow",
    width=40,
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

result_3 = tk.Label(
    foreground="green",
    font=("Arial", 14)
)

for c in window.children:
    print(c)
    window.children[c].pack()

window.after(random.randint(500, 2500), timer_update)

window.mainloop()