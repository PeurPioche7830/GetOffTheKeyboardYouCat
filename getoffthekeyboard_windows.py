import tkinter as tk
from tkinter import ttk


def open_secondary_window():
    # Create cat protect window.
    secondary_window = tk.Toplevel()
    secondary_window.iconbitmap("cat.ico")
    secondary_window.title("Secondary Window")
    # Window size (i'll find a way to make this work on all monitor sizes later)
    window_width = 1920
    window_height = 1080
    # get the screen dimension
    screen_width = secondary_window.winfo_screenwidth()
    screen_height = secondary_window.winfo_screenheight()
    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    secondary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # options to make it all cleaner
    secondary_window.resizable(False,False)
    secondary_window.attributes('-topmost', 1, '-alpha',0.9)
    secondary_window.overrideredirect(1)

    
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



