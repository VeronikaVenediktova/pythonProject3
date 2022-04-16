import tkinter as tk
import random
import time

window = tk.Tk()
# Tentry = tk.Entry()
colors = ["black", 'white', 'yellow', 'red', 'blue', 'green']
window.geometry("300x300")
label = tk.Label(
    text="Check your reaction",
    foreground="white",  # Set the text color to white
    bg=random.choice(colors),  # Set the background color to black
    width=100,
    height=2
)
# entry = tk.Entry()

frame = tk.Frame(
    height=10
)


def send_message():
    t2 = time.time()
    var = t2-t1
    result_1.config(text="Speed reaction is ")
    result_2.config(text=var)

# def start():
#
#
# def stop():
#     window.after_cancel(time.time())

button = tk.Button(
    text="Click me!",
    bg="blue",
    fg="yellow",
    width=10,
    height=1,
    command=send_message
)

# result = tk.Label(
#     text="0.0",
#     foreground="red",  # Set the text color to white
#     font=("Arial", 25)
# )

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

# for value in colors:
#     if value == colors[3]:
#         t1 = time.time()

def timer_update():
    global value,  t1
    # for value in colors:
    #     if value == "red":
    #         t1 = time.time()
    #     else:
    #         False
    value = random.choice(colors)
    label.config(bg=value)
        if value == "red":
            t1 = time.time()
        else:
            False
    window.after(2000, timer_update)
    # return t1



window.after(2000, timer_update)

window.mainloop()


