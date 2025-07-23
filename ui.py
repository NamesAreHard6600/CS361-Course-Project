# UI Class for CS361 Project
# By: Joshua Knowles


from tkinter import *
from alarm import Alarm
import time

class UI:
    def __init__(self, DEBUG):
        self.DEBUG = DEBUG
        self.home = Tk()
        self.home.geometry("312x624")
        self.home.title("Wake.exe")
        self.home.grid_columnconfigure(0, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)

        self.title = Label(self.home, text="Wake.exe", font=("MS Sans Serif",36))

        self.main_frame = Frame(self.home, bg="darkgrey", bd=3)

        self.alarms = []

        # self.alarm_going_off = Tk()
        # self.alarm_going_off.geometry("312x624")
        # self.alarm_going_off.title("Wake.exe: Alarm is going off!")

        if self.DEBUG:
            test_button = Button(self.home, text="Debug Testing", command=self.debug_test)
            test_button.grid(row=6, column=0)

        self.add_alarm()
        self.add_alarm()
        self.show_home()

    def add_alarm(self):
        alarm = Alarm(self, "Test", 7, 30, False)
        self.alarms.append(alarm)

    def get_num_alarms(self):
        return len(self.alarms)

    def show_home(self):
        self.title.grid(row=0, column=0, sticky="new")
        self.main_frame.grid(row=1, column=0, sticky="new")
        for i, alarm in enumerate(self.alarms):
            alarm.show_frame(i+1)

    def hide_home(self):
        self.title.grid_forget()
        for alarm in self.alarms:
            alarm.hide_frame()

    def debug_test(self):
        print("Button Pressed")
        if self.title.grid_info():
            self.hide_home()
        else:
            self.show_home()

    def display(self):
        self.home.mainloop()
