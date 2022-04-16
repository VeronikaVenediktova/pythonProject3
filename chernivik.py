import tkinter as tk
import random
import time
false_click_count = 0
def send_message():
    if value == "red":
        t2 = time.time()
        var = t2-t1
        result_1.config(text="Speed reaction is ")
        result_2.config(text=var)

    else:
        result_1.config(text="False click")
        result_2.config(text="")
        false_click_count += 1
def timer_update():
    global value,  t1
    t1 = time.time()
    value = random.choice(colors)
    label.config(bg=value)
    window.after(2000, timer_update)

window = tk.Tk()
# Tentry = tk.Entry()
colors = ["black", 'white', 'yellow', 'red', 'blue', 'green']
window.geometry("300x300")
label = tk.Label(
    text="Check your reaction",
    foreground="white",  # Set the text color to white
    bg=random.choice(colors),  # Set the background color to black
    width=100,
    height=3
)
# entry = tk.Entry()

frame = tk.Frame(
    height=10
)

button = tk.Button(
    text="Click me!",
    bg="blue",
    fg="yellow",
    width=10,
    height=1,
    command=send_message
)

frame_2 = tk.Frame(
    height=10
)

result_1 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 14))

result_2 = tk.Label(
    foreground="green",  # Set the text color to white
    font=("Arial", 14)
)

for c in window.children:
    print(c)
    window.children[c].pack()



window.after(2000, timer_update)

window.mainloop()