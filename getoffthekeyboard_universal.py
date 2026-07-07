import tkinter as tk
from tkinter import ttk


def open_secondary_window():
    # Create cat protect window.
    secondary_window = tk.Toplevel()
    secondary_window.title("Secondary Window")
    secondary_window.config(width=1920, height=1080)
    secondary_window.resizable(False,False)
    secondary_window.attributes('-topmost', 1)
    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        secondary_window,
        text="Unlock this computer from feline activity",
        command=secondary_window.destroy
    )
    button_close.place(x=960, y=540)


# Create the main window.
main_window = tk.Tk()
main_window.config(width=400, height=200)
main_window.resizable(False,False)
main_window.title("Get off the Keyboard, you cat!")
# Create the button to open the cat-proofing
button_open = ttk.Button(
    main_window,
    text="Lock this computer from feline activity",
    command=open_secondary_window
)
button_open.place(x=70, y=90)
main_window.mainloop()
