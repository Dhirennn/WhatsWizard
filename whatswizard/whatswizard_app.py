import tkinter as tk
from whatsapp_parser import *

"""
This file header will provide a short description of whatswizard_app.py

This simple app is made using tkinter, and is just to provide the user with a GUI to parse the WhatsApp chatlog file

Documentation by : Mandhiren Singh
"""
__author__ = "Mandhiren Singh"


# Auxiliary function to call my WhatsApp chatlog parser
def run_parser_aux(string):
    return run_parser(string)


def go_to_new_window(window):
    # root.destroy()
    root.withdraw()
    window.withdraw()
    window.deiconify()


def centre_window(window, width, height):
    # Aligning the window better...

    # Get the width and height of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Playing around with good width and height (in pixels)
    window_width = width
    window_height = height

    # Calculate the position of the window
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2) - 200

    # Set the dimensions of the window and position it properly using .geometry()
    window.geometry(f'{window_width}x{window_height}+{int(x_coord)}+{int(y_coord)}')


# =====================================================================================================================

root = tk.Tk()

centre_window(root, 600, 220)


# Create a label to prompt the user to enter the name of their chatlog file
chatlog_prompt_label = tk.Label(root, text="Enter the name of your whatsapp chatlog (.txt) file:",
                                font=("Helvetica", 16), fg="blue")

# create an input field for the user to enter a string
string_input = tk.Entry(root, font=("Helvetica", 16), fg="blue")

# create a button that uses the string entered by the user when clicked
button = tk.Button(root, text="Parse chatlog file", command=lambda: run_parser_aux(string_input.get()),
                   font=("Helvetica", 16), fg="blue")

# instructions
instructions_label = tk.Label(root,
                              text="1. Place your WhatsApp chatlog file into this directory\n2. Type out the name of your "
                                   "chatlog.txt file (e.g: 'my_groupchat.txt')\n3. Click on the blue \"Parse chatlog file "
                                   "button\"\n4. The button will turn black after the parsing has been completed."
                                   "\n5. Click on the 'Go to next step button'.\n6. The CSV file will be in your directory.",
                              font=("Helvetica", 8), fg="maroon")

# Create new window to display stats
stats_window = tk.Toplevel()

done_label = tk.Label(stats_window, text="The parsing has been completed!\nYou can find the {chatlog_name}_extracted.csv in your directory!",
                                font=("Helvetica", 20), fg="black")
stats_window.withdraw()
done_label.pack()
centre_window(stats_window, 900, 150)

# next step label
next_step_button = tk.Button(root, text="Go to next step", command=lambda: go_to_new_window(stats_window))

# create a label to prompt the user to close the app
# close_label = tk.Label(root, text="Close this app once the 'Parse chatlog file' button turns blue", font=("Helvetica", 8), fg="maroon")

# pack the widgets into the window
chatlog_prompt_label.pack()
string_input.pack()
button.pack()
instructions_label.pack()
next_step_button.pack()
# close_label.pack()


# start the main event loop
root.mainloop()


