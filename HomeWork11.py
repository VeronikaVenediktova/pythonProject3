import tkinter as tk
import random
import time
from datetime import date
import datetime
import json

font_size = ("Arial", 12)
click_count = 0
false_click_count = 0
button_color = "red"
list_average = []
time_start = time.time()
var_average = 0
var_minimum = 0.0
click_ratio = 0
file_name = "user_scores.json"

try:
    with open(file_name, "r") as file:
        file_dict = json.load(file)
        # print(file_dict)
        print("File allready exist and has correct json  format")
except:
    with open(file_name, "w") as file:
        print("File not found or has incorect format, creating new file")
        file_title = {
            "File version": str(datetime.datetime.today())
        }
        # print(file_title)
        json.dump(file_title, file)


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

    # result_3.config(text="MIN:" + str(var_minimum) + ", AVG:" + str(var_average) + ", LEN:" + str(len(list_average)) + ", CLK_RAT:" + str(click_ratio))

    return


def timer_update():
    global time_start, button_color
    time_start = time.time()
    button_color = random.choice(colors)
    button_click.config(bg=button_color)
    window.after(random.randint(500, 2500), timer_update)


def enter_name():
    global name
    name = entry.get()
    if len(name) >= 2 and name.isalpha():
        entry.config(state="disabled")
        button_start.config(state="disabled")
        button_click.config(state="normal")
        button_save.config(state="normal")

    return


def save():  # функция сохранения в файл
    button_save.config(state="disabled")
    button_start.config(state="normal")
    button_click.config(state="disabled")
    entry.config(state="normal")
    user_data = {}
    current_user_from_file = []
    file_dict = {}
    if click_ratio >= 0.5:
        with open(file_name, "r") as file:
            file_dict = json.load(file)
            # print(file_dict)
            # print(type(file_dict))
            current_user_from_file = file_dict.get(name)
            # print(current_user_from_file)

        rec_time = datetime.datetime.today()
        user_data = {
            'Date': str(rec_time),
            'MIN': var_minimum,
            'AVG': var_average}
        try:
            current_user_from_file = file_dict.get(name)
            current_user_from_file.append(user_data)
        except:
            current_user_from_file = []
            current_user_from_file.append(user_data)

        file_dict.update({name: current_user_from_file})

        # print(file_dict)

        with open(file_name, "w") as file:
            json.dump(file_dict, file)


window = tk.Tk(screenName="Check you Reaction")
colors = ['white', 'yellow', 'red', 'blue', 'green', 'red', 'cyan', 'magenta', 'red']
# colors = ["red"]
window.geometry("800x480")
label = tk.Label(
    text="Check your reaction",
    font=font_size,
    foreground="Black",
    bg="white",
    width=100,
    height=3
)

label_name = tk.Label(
    text="Enter your name",
    font=("Arial", 12),
    foreground="black",
    background="white",
    border=5,
    borderwidth=3,
    width=200,
    height=2
)
entry = tk.Entry()
frame = tk.Frame(
    height=10
)

button_start = tk.Button(
    text="START",
    bg="Gray",
    fg="Cyan",
    width=40,
    height=1,
    command=enter_name,
    border=10,
    font=font_size,
    borderwidth=2
)

frame_2 = tk.Frame(
    height=10
)
button_save = tk.Button(
    state="disabled",
    text="STOP and SAVE",
    font=font_size,
    bg="Gray",
    fg="black",
    width=40,
    height=1,
    command=save
)

frame_1 = tk.Frame(
    height=10
)
button_click = tk.Button(
    text="Click me!",
    bg=button_color,
    fg="Black",
    width=40,
    height=3,
    font=font_size,
    command=send_message
)

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="Black",
    font=font_size
)
result_2 = tk.Label(
    foreground="Black",
    font=font_size
)

for c in window.children:
    window.children[c].pack()

button_save.config(state="disabled")
button_start.config(state="normal")
button_click.config(state="disabled")

window.after(random.randint(500, 2500), timer_update)

window.mainloop()