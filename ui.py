# UI Class for CS361 Project
# By: Joshua Knowles
from logging import disable
from tkinter import *
from customtkinter import *
from tkinter import messagebox
from alarm import Alarm
import random
import time

class UI:
    def __init__(self, DEBUG):
        # Root Vars
        self.DEBUG = DEBUG
        self.home = Tk()
        self.home.geometry("356x624")
        self.home.title("Wake.exe")
        self.home.config(bg="grey17")
        self.home.resizable(width=False, height=True)
        # self.root.grid_rowconfigure(0, weight=1)

        # Home Vars
        self.title = Label(self.home, text="Wake.exe", font=("MS Sans Serif",36), bg="grey17", fg="white")
        self.main_frame = CTkScrollableFrame(self.home)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.alarms = []

        self.add_alarm_button = Button(self.home, text="Add Alarm", command=self.add_alarm, bg="red")

        if self.DEBUG:
            test_button = Button(self.home, text="Debug Testing", command=self.debug_test)
            test_button.grid(row=30, column=0)

        # Edit Page Vars
        self.edit_columns = 7
        self.edit_rows = 5
        self.edit_exit_button = CTkButton(self.home, text="X", text_color="black", border_color="white", hover_color="darkred", border_width=2, fg_color="red", font=("MS Reference Sans Serif", 24), corner_radius=5, command=self.cancel_edit, height=38, width=38)
        self.title_edit = Entry(self.home, font=("MS Reference Sans Serif", 16))
        vcmdh = (self.home.register(self.is_hour), '%P')
        vcmdm = (self.home.register(self.is_minute), '%P')
        self.hour_entry = Entry(self.home, validate='key', validatecommand=vcmdh, justify="right", font=("MS Reference Sans Serif", 16))
        self.semicolon = Label(self.home, text=":", fg="white", bg="grey17", justify="center", font=("MS Reference Sans Serif", 16))
        self.minute_entry = Entry(self.home, validate='key', validatecommand=vcmdm, font=("MS Reference Sans Serif", 16))
        self.one_time_text = Label(self.home, text="One-Time", bg="grey17", fg="white")
        self.type_switch = CTkSwitch(self.home, text="", width=0, fg_color="grey", progress_color="grey", command=self.update_edit)
        self.daily_text = Label(self.home, text="Daily", bg="grey17", fg="white")

        self.days = ["S", "M", "T", "W", "Th", "F", "Sa"]
        self.day_buttons = []
        self.day_vars = []
        for i in range(7):
            self.day_vars.append(BooleanVar(value=True))
            self.day_buttons.append(Checkbutton(self.home, text=self.days[i], variable=self.day_vars[i], bg="grey17", fg="white", activebackground="grey17", activeforeground="white", selectcolor="darkgrey"))

        self.save_button = CTkButton(self.home, text="Save", text_color="black", border_color="white", hover_color="darkgreen", border_width=2, fg_color="green", font=("MS Reference Sans Serif", 24), corner_radius=5, command=self.apply_edit, height=40)

        self.editing = -1

        self.show_home()

    def add_alarm(self):
        alarm = Alarm(self, "Alarm", 12, 0, False)
        self.alarms.append(alarm)
        self.edit_alarm(self.get_num_alarms() - 1)

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
        self.home.grid_rowconfigure(1, weight=1)
        self.home.grid_columnconfigure(0, weight=1)
        self.title.grid(row=0, column=0, sticky="new")
        self.main_frame.grid(row=1, column=0, sticky="news")
        for i, alarm in enumerate(self.alarms):
            alarm.show_frame(i+1)
        self.add_alarm_button.grid(row=2, column=0, sticky="se", padx=5, pady=5)

    def hide_home(self):
        self.home.grid_rowconfigure(1, weight=0)
        self.home.grid_columnconfigure(0, weight=0)
        self.title.grid_forget()
        for alarm in self.alarms:
            alarm.hide_frame()
        self.add_alarm_button.grid_forget()
        self.main_frame.grid_forget()

    # self.editing must be set
    def show_edit(self):
        if self.editing == -1 or self.editing >= self.get_num_alarms():
            self.show_home()
            raise "EDITING ALARM OUT OF BOUNDS"

        alarm = self.alarms[self.editing]

        for i in range(self.edit_columns):
            self.home.grid_columnconfigure(i, weight=1, uniform="equal_columns")

        self.edit_exit_button.grid(row=0, column=0, sticky = "nwe", padx=5, pady=5)

        self.title_edit.delete(0, END)
        self.title_edit.insert(0, alarm.title)
        self.title_edit.grid(row=1, column=0, columnspan=self.edit_columns, sticky="nwe", padx=5, pady=5)

        self.hour_entry.delete(0, END)
        self.hour_entry.insert(0, alarm.hour)
        self.hour_entry.grid(row=2, column=2, columnspan=1, sticky="ne", padx=5, pady=5)

        self.semicolon.grid(row=2, column=3, sticky="wens")

        self.minute_entry.delete(0, END)
        self.minute_entry.insert(0, alarm.minutes)
        self.minute_entry.grid(row=2, column=4, columnspan=1, sticky="nw", padx=5, pady=5)

        self.one_time_text.grid(row=3, column=0, columnspan=3, sticky="ne", padx=5, pady=5)
        if alarm.one_time:
            self.type_switch.deselect()
        else:
            self.type_switch.select()

        self.type_switch.grid(row=3, column=3, sticky="nwe", padx=5, pady=5)
        self.daily_text.grid(row=3, column=4, columnspan=3, sticky="nw", padx=5, pady=5)

        for i, button in enumerate(self.day_buttons):
            if alarm.day_vars[i]:
                button.select()
            else:
                button.deselect()
            button.grid(row=4, column=i, sticky="nsew", padx=5)

        self.save_button.grid(row=5, column=0, columnspan=self.edit_columns, sticky="new", padx=5, pady=5)

        self.update_edit()

    def hide_edit(self):
        for i in range(self.edit_columns):
            self.home.grid_columnconfigure(i, weight=0, uniform="")
        for i in range(self.edit_rows):
            self.home.grid_rowconfigure(i, weight=0)
        self.editing = -1
        self.edit_exit_button.grid_forget()
        self.title_edit.grid_forget()
        self.hour_entry.grid_forget()
        self.semicolon.grid_forget()
        self.minute_entry.grid_forget()
        self.one_time_text.grid_forget()
        self.type_switch.grid_forget()
        self.daily_text.grid_forget()
        for button in self.day_buttons:
            button.grid_forget()
        self.save_button.grid_forget()

    def update_edit(self):
        if self.type_switch.get():
            self.daily_text.configure(fg="white")
            self.one_time_text.configure(fg="grey52")
            for button in self.day_buttons:
                button.config(state=NORMAL)
        else:
            self.daily_text.configure(fg="grey52")
            self.one_time_text.configure(fg="white")
            for button in self.day_buttons:
                button.config(state=DISABLED)

    def apply_edit(self):
        alarm = self.alarms[self.editing]
        alarm.title = self.title_edit.get()
        alarm.one_time = not self.type_switch.get()
        alarm.hour = int(self.hour_entry.get())
        alarm.minutes = int(self.minute_entry.get())
        for i, var in enumerate(self.day_vars):
            if var.get():
                alarm.day_vars[i] = True
            else:
                alarm.day_vars[i] = False

        alarm.update_frame()

        self.hide_all()
        self.show_home()

    def cancel_edit(self):
        response = messagebox.askyesno(f"Cancel Edits",f"Are you sure you want to cancel your edits? You will have to edit the alarm again.")
        if not response:
            return
        self.hide_all()
        self.show_home()

    def is_hour(self, new_value):
        if new_value == "":
            return True

        if not new_value.isdigit():
            return False

        return 1 <= int(new_value) <= 12

    def is_minute(self, new_value):
        if new_value == "":
            return True

        if not new_value.isdigit():
            return False

        return 0 <= int(new_value) <= 59

    def hide_all(self):
        self.hide_home()
        self.hide_edit()

    def check_alarms(self):
        # print("Checking alarms")
        self.home.after(100, self.check_alarms)

    def display(self):
        self.home.after(100, self.check_alarms)
        self.home.mainloop()

    def debug_test(self):
        if not self.title_edit.grid_info():
            self.add_alarm()
        else:
            self.apply_edit()
            self.hide_all()
            self.show_home()
