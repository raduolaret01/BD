from tkinter import *
from tkinter import ttk

import logic_layer


class LoginWindow:

    def __init__(self, master):
        self.root = master
        self.mainPanel = ttk.Frame(self.root, padding=(5, 5, 12, 0))
        self.mainPanel.grid(column=0, row=0, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.usernameEntry = ttk.Entry(self.mainPanel, )
