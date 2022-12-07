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

# =====================================================================================================================

# Create the root window and title
root = tk.Tk()
root.bg = "light blue"
root.title("WhatsApp Chatlog Parser")

# Create a label to prompt the user to enter the name of their chatlog file
chatlog_prompt_label = tk.Label(root, text="Enter the name of your whatsapp chatlog (.txt) file:", font=("Helvetica", 16), fg="blue")

# create an input field for the user to enter a string
string_input = tk.Entry(root, font=("Helvetica", 16), fg="blue")

# create a button that uses the string entered by the user when clicked
button = tk.Button(root, text="Parse chatlog file", command=lambda: run_parser_aux(string_input.get()), font=("Helvetica", 16), fg="blue")

# instructions
instructions_label = tk.Label(root, text="1. Place your WhatsApp chatlog file into this directory\n2. Type out the name of your "
                             "chatlog.txt file (e.g: 'my_groupchat.txt')\n3. Click on the blue \"Parse chatlog file "
                             "button\"\n4. The button will turn black. Close the app once the button turns blue "
                             "again.\n5. The CSV file will be in your directory.",font=("Helvetica", 8), fg="maroon")


# create a label to prompt the user to close the app
# close_label = tk.Label(root, text="Close this app once the 'Parse chatlog file' button turns blue", font=("Helvetica", 8), fg="maroon")

# pack the widgets into the window
chatlog_prompt_label.pack()
string_input.pack()
button.pack()
instructions_label.pack()
# close_label.pack()

# start the main event loop
root.mainloop()