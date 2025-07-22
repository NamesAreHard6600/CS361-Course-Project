# UI Class for CS361 Project
# By: Joshua Knowles


from tkinter import *
from alarm import Alarm

class UI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("312x624")
        self.root.title("Alarm.exe")

        self.title = Label(self.root, text="Alarm.exe")
        self.title.grid(row=0, column=0)

        self.main_frame = Frame(self.root, bg="darkgrey", bd=3)
        self.main_frame.grid(row=1, column=0)

        self.test = Label(self.main_frame, text="Test")
        self.test.grid(row=0, column=0)

        self.alarms = []
        self.alarm_frames = []

    def add_alarm(self):
        self.alarms.append(Alarm("Test"))
        self.alarm_frames.append(Frame(self.root, ))

    def display(self):
        self.root.mainloop()
