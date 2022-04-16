import tkinter as tk
import random
import time
false_click_count = 0
button_color = "red"
label_color = "red"
time_start = time.time()


def send_message():
    global false_click_count
    if label_color == button_color:
        time_click = time.time()
        var = time_click - time_start
        result_1.config(text="Speed reaction is ")
        result_2.config(text=var)

    else:
        result_1.config(text="False click")
        false_click_count += 1
        result_2.config(text=false_click_count)


def timer_update():
    global time_start, label_color, button_color
    time_start = time.time()
    label_color = random.choice(colors)
    button_color = random.choice(colors)
    label.config(bg=label_color)
    button.config(bg=button_color)
    window.after(random.randint(500, 2500), timer_update)


window = tk.Tk()
colors = ["black", 'white', 'yellow', 'red', 'blue', 'green']
window.geometry("300x300")
label = tk.Label(
    text="Check your reaction",
    foreground="white",
    bg=random.choice(colors),
    width=100,
    height=3
)

frame = tk.Frame(
    height=10
)

button = tk.Button(
    text="Click me!",
    bg=button_color,
    fg="yellow",
    width=10,
    height=1,
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

