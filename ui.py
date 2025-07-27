# UI Class for CS361 Project
# By: Joshua Knowles


from tkinter import *
from customtkinter import *
from tkinter import messagebox
from alarm import Alarm
import random
import time

class UI:
    def __init__(self, DEBUG):
        self.DEBUG = DEBUG
        self.home = Tk()
        self.home.geometry("312x624")
        self.home.title("Wake.exe")
        self.home.grid_rowconfigure(1, weight=1)
        self.home.grid_columnconfigure(0, weight=1)
        # self.root.grid_rowconfigure(0, weight=1)

        # Home
        self.title = Label(self.home, text="Wake.exe", font=("MS Sans Serif",36))
        self.main_frame = CTkScrollableFrame(self.home)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # self.scrollbar = Scrollbar(self.home)

        self.alarms = []

        # self.alarm_going_off = Tk()
        # self.alarm_going_off.geometry("312x624")
        # self.alarm_going_off.title("Wake.exe: Alarm is going off!")

        self.title_edit = Entry(self.home)

        self.editing = -1

        if self.DEBUG:
            test_button = Button(self.home, text="Debug Testing", command=self.debug_test)
            test_button.grid(row=6, column=0)

        self.show_home()

    def add_alarm(self):
        alarm = Alarm(self, "Alarm", 12, 0, False)
        self.alarms.append(alarm)
        self.show_home()

    def edit_alarm(self, num):
        self.hide_all()
        self.editing = num
        self.show_edit()

    def delete_alarm(self, alarm):
        for i, a in enumerate(self.alarms):
            if alarm == a:
                response = messagebox.askyesno(f"Delete {alarm.title}", f"Are you sure you want to delete {alarm.title}?\n The alarm will have to be remade.")
                if response:
                    alarm.hide_frame()
                    self.alarms.remove(alarm)
                return

        # Prompt permission
        self.show_home()

    def get_num_alarms(self):
        return len(self.alarms)

    def get_alarm_num(self, alarm):
        for i, a in enumerate(self.alarms):
            if alarm == a:
                return i

    def show_home(self):
        # Remove all previous, add everything again
        # self.hide_home()
        self.title.grid(row=0, column=0, sticky="new")
        # self.scrollbar.grid(row=0, column=1, rowspan=20, sticky="nse")
        self.main_frame.grid(row=1, column=0, sticky="news")
        for i, alarm in enumerate(self.alarms):
            alarm.show_frame(i+1)

    def hide_home(self):
        self.title.grid_forget()
        for alarm in self.alarms:
            alarm.hide_frame()
        self.main_frame.grid_forget()

    # self.editing must be set
    def show_edit(self):
        if self.editing == -1 or self.editing >= self.get_num_alarms():
            raise "EDITING ALARM OUT OF BOUNDS"
        self.title_edit.delete(0, END)
        self.title_edit.insert(0, self.alarms[self.editing].title)
        self.title_edit.grid(row=1, column=0, sticky="nwe")

    def hide_edit(self):
        self.editing = -1
        self.title_edit.grid_forget()

    def apply_edit(self):
        alarm = self.alarms[self.editing]
        alarm.title = self.title_edit.get()
        alarm.update_frame()

    def debug_test(self):
        if not self.title_edit.grid_info():
            self.add_alarm()
            self.edit_alarm(self.get_num_alarms()-1)
        else:
            self.apply_edit()
            self.hide_all()
            self.show_home()

    def hide_all(self):
        self.hide_home()
        self.hide_edit()

    def display(self):
        self.home.mainloop()

    def test(self, event):
        print(event)
