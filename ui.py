# UI Class for CS361 Project
# By: Joshua Knowles


from tkinter import *
from alarm import Alarm

class UI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("312x624")
        self.root.title("Wake.exe")
        self.root.grid_columnconfigure(0, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)

        self.title = Label(self.root, text="Wake.exe", font=("MS Sans Serif",36))
        self.title.grid(row=0, column=0, sticky="new")

        self.main_frame = Frame(self.root, bg="darkgrey", bd=3)
        self.main_frame.grid(row=1, column=0, sticky="new")

        self.alarms = []

        self.add_alarm()
        self.add_alarm()

    def add_alarm(self):
        alarm = Alarm(self, "Test", 7, 30, False)
        self.alarms.append(alarm)

    def get_num_alarms(self):
        return len(self.alarms)

    def display(self):
        self.root.mainloop()
