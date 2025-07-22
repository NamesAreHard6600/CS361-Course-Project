# Alarm Class for CS361 Project
# By: Joshua Knowles
from tkinter import *

class Alarm:
    def __init__(self, ui, title, hour, minutes, pm):
        self.ui = ui
        self.title = title
        self.hour = hour
        self.minutes = minutes
        self.pm = pm

        self.form_frame()

    def form_frame(self):
        self.frame = Frame(self.ui.root, bg="darkgrey", bd=3)
        self.alarm_label = Label(self.frame, text=self.title, bg="darkgrey", font=("MS Reference Sans Serif",20))
        self.alarm_label.grid(row=0, column=0, sticky="nw")

        self.time_label = Label(self.frame,
            text=f"{self.hour}:{self.minutes:02d} {'pm' if self.pm else 'am'}",
            bg="darkgrey",
            font=("MS Reference Sans Serif",20))

        self.time_label.grid(row=1, column=0, sticky = "nw")

        self.frame.grid(row=self.ui.get_num_alarms()+1, column=0, sticky="ew", padx=10, pady=5)