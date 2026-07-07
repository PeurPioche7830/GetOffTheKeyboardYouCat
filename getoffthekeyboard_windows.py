import tkinter as tk
from tkinter import ttk


def open_secondary_window():
    # Create cat protect window.
    secondary_window = tk.Toplevel()
    secondary_window.iconbitmap("cat.ico")
    secondary_window.title("Secondary Window")
    secondary_window.geometry('1920x1080')
    secondary_window.resizable(False,False)
    secondary_window.attributes('-topmost', 1, '-alpha',0.9)
    
    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        secondary_window,
        text="Unlock this computer from feline activity",
        command=secondary_window.destroy
    )
    button_close.place(relx=0.5, rely=0.5, anchor='center')


# Create the main window.
main_window = tk.Tk()
main_window.iconbitmap("cat.ico")
main_window.geometry('400x200')
main_window.title("Get off the Keyboard, you cat!")
main_window.resizable(False,False)
label1 = tk.Label(main_window, text='Get off the keyboard, you cat!',bg='orange',fg='white')
label1.pack()
# Create the button to open the cat-proofing
button_open = ttk.Button(
    main_window,
    text="Lock this computer from feline activity",
    command=open_secondary_window
)
button_open.place(relx=0.5, rely=0.5, anchor='center')

# keep window open
main_window.mainloop()
