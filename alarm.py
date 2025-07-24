# Alarm Class for CS361 Project
# By: Joshua Knowles
from tkinter import *

class Alarm:
    def __init__(self, ui, title="Alarm", hour=12, minutes=0, pm=False, one_time=True):
        self.ui = ui
        self.title = title
        self.hour = hour
        self.minutes = minutes
        self.pm = pm
        self.one_time = one_time
        self.days = [("S", True), ("M", True), ("T", True), ("W", True), ("Th", True), ("F", True), ("Sa", True)]

        self.total_columns = 15

        self.form_frame()

    def form_frame(self):
        # Main Frame
        self.frame = Frame(self.ui.home, bg="darkgrey", bd=3)

        # Configure columns
        for i in range(self.total_columns):
            self.frame.columnconfigure(i, weight=1 if i >= 0 else 0)

        # Label
        self.alarm_label = Label(self.frame, text=self.title, bg="darkgrey", font=("MS Reference Sans Serif",20))
        self.alarm_label.grid(row=0, column=0, columnspan=self.total_columns, sticky="nw")

        # Time
        self.time_label = Label(self.frame,
            text=f"{self.hour}:{self.minutes:02d} {'pm' if self.pm else 'am'}",
            bg="darkgrey",
            font=("MS Reference Sans Serif", 20))

        self.time_label.grid(row=1, column=0, columnspan=self.total_columns-1, sticky="nw")

        if self.one_time:
            self.one_time_label = Label(self.frame, text="One Time", bg="darkgrey", font=("MS Reference Sans Serif",16))
            self.one_time_label.grid(row=2, column=0, columnspan=self.total_columns-2, sticky="nw")

        self.edit_button = Button(self.frame, text="Edit", bg="blue", command=self.edit_alarm)
        self.edit_button.grid(row=2, column=self.total_columns-2, sticky="se")

        self.delete_button = Button(self.frame, text="Delete", bg="red", command=self.delete_alarm)
        self.delete_button.grid(row=2, column=self.total_columns-1, sticky="se")

    def get_alarm_num(self):
        return self.ui.get_alarm_num(self)

    def edit_alarm(self):
        self.ui.edit_alarm(self.get_alarm_num())

    def delete_alarm(self):
        self.ui.delete_alarm(self)

    def show_frame(self, row):
        self.frame.grid(row=row, column=0, sticky="ew",
                        padx=10, pady=5)

    def hide_frame(self):
        self.frame.grid_forget()