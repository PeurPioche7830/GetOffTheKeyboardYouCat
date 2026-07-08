import tkinter as tk
from tkinter import ttk

# Default settings
DarkBrown = "#17120c"
Beige   = "#fef8ef"
KindaBrown   = "#655552"

def open_secondary_window():
    # Create cat protect window.
    secondary_window = tk.Toplevel()
    secondary_window.title("Secondary Window")
    # get the screen dimension
    screen_width = secondary_window.winfo_screenwidth()
    screen_height = secondary_window.winfo_screenheight()
    # Window size (works on all screen sizes! at least in theory.)
    window_width = screen_width
    window_height = screen_height
    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    secondary_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # options to make it all cleaner
    secondary_window.resizable(False,False)
    secondary_window.attributes('-topmost', 1, '-alpha',0.9)
    secondary_window.overrideredirect(1)
    secondary_window.configure(bg=KindaBrown)
    # text
    label2 = tk.Label(secondary_window, text='Computer is currently locked',bg='#655552',fg='white', font=('Rubik', 40))
    label2.pack()
    label2.place(relx=0.5, rely=0.4, anchor='center')

    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        secondary_window,
        text="Unlock this computer from feline activity",
        command=secondary_window.destroy
    )
    button_close.place(relx=0.5, rely=0.5, anchor='center')


# Create the main window.
main_window = tk.Tk()
main_window.geometry('400x200')
# main window stuff
main_window.title("Get off the Keyboard, you cat!")
main_window.iconphoto(False, tk.PhotoImage(file='canvas.png'))
main_window.configure(bg=Beige)
main_window.resizable(False,False)
# text
label1 = tk.Label(main_window, text='Get off the keyboard, you cat!',bg='#fef8ef',fg='#17120c', font=('Rubik', 19))
label1.pack()
label1.place(relx=0.5, rely=0.1, anchor='center')
# cat-proofing button
button_open = ttk.Button(
    main_window,
    text="Lock this computer from feline activity",
    command=open_secondary_window
)
button_open.place(relx=0.5, rely=0.5, anchor='center')

# keep window open
main_window.mainloop()
