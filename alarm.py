# Alarm Class for CS361 Project
# By: Joshua Knowles
from tkinter import *
from customtkinter import *

class Alarm:
    def __init__(self, ui, title="Alarm", hour=12, minutes=0, pm=False, one_time=True):
        self.ui = ui
        self.title = title
        self.hour = hour
        self.minutes = minutes
        self.pm = pm
        self.one_time = one_time
        self.enabled = BooleanVar(value=True)
        self.days = ["S", "M", "T", "W", "Th", "F", "Sa"]
        self.day_vars = [True for _ in range(7)]

        self.total_columns = 3

        self.form_frame()

    # Runs Once
    def form_frame(self):
        # Main Frame
        self.frame = Frame(self.ui.main_frame, bg="darkgrey", bd=3)

        # Configure columns
        for i in range(self.total_columns):
            # Give more weight to the last two columns
            weight = 1 if i >= self.total_columns - 2 else 0
            self.frame.columnconfigure(i, weight=weight)

        # Label
        self.alarm_label = Label(self.frame, text="T Pose", bg="darkgrey", font=("MS Reference Sans Serif",20))
        self.alarm_label.grid(row=0, column=0, sticky="nw")

        # Time
        self.time_label = Label(self.frame,
            text="T Pose",
            bg="darkgrey",
            font=("MS Reference Sans Serif", 20))
        self.time_label.grid(row=1, column=0, sticky="nw")

        self.one_time_label = Label(self.frame, text="One Time", bg="darkgrey",
                                    font=("MS Reference Sans Serif", 16))
        self.daily_label = Text(self.frame,
                                bg="darkgrey",
                                font=("MS Reference Sans Serif", 16),
                                state="disabled",
                                borderwidth=0,
                                highlightthickness=0,
                                takefocus=0,
                                height=1,
                                width=15,
                                wrap="none",
                                selectbackground = "darkgrey",
                                selectforeground = "darkgrey",
                                inactiveselectbackground = "darkgrey",
                                cursor="arrow"
        )

        if self.one_time:
            self.one_time_label.grid(row=2, column=0, sticky="nw")
        else:
            self.daily_label.grid(row=2, column=0, sticky="nw")
            self.fill_daily_text()

        self.enable_switch = CTkSwitch(self.frame, text="", fg_color="red", progress_color="green", variable=self.enabled, command=self.switch_toggled, width=45)
        self.enable_switch.grid(row=1, column=self.total_columns-1, sticky="e")

        self.edit_button = Button(self.frame, text="Edit", bg="blue", command=self.edit_alarm)
        self.edit_button.grid(row=0, column=self.total_columns-1, sticky="e")

        self.delete_button = Button(self.frame, text="Delete", bg="red", command=self.delete_alarm)
        self.delete_button.grid(row=2, column=self.total_columns-1, sticky="e")

        self.update_frame()

    # Runs Multiple Times
    def update_frame(self):
        self.alarm_label.configure(text=self.title)
        self.time_label.configure(text=f"{self.hour}:{self.minutes:02d} {'pm' if self.pm else 'am'}")
        if self.enabled.get():
            self.frame.configure(bg="darkgrey")
            self.alarm_label.configure(bg="darkgrey")
            self.time_label.configure(bg="darkgrey")
            self.one_time_label.configure(bg="darkgrey")
            self.daily_label.configure(bg="darkgrey",
                                       selectbackground = "darkgrey",
                                       selectforeground = "darkgrey",
                                       inactiveselectbackground = "darkgrey")
        else:
            self.frame.configure(bg="grey26")
            self.alarm_label.configure(bg="grey26")
            self.time_label.configure(bg="grey26")
            self.one_time_label.configure(bg="grey26")
            self.daily_label.configure(bg="grey26",
                                       selectbackground="grey26",
                                       selectforeground="grey26",
                                       inactiveselectbackground="grey26")
        self.one_time_label.grid_forget()
        self.daily_label.grid_forget()
        if self.one_time:
            self.one_time_label.grid(row=2, column=0, sticky="nw")
        else:
            self.daily_label.grid(row=2, column=0, sticky="nw")
            self.fill_daily_text()

    def fill_daily_text(self):
        self.daily_label.config(state="normal")
        self.daily_label.delete("1.0", END)
        for day, enabled in zip(self.days, self.day_vars):
            self.daily_label.insert(END, day + " ", "enabled" if enabled else "disabled")
        self.daily_label.tag_configure("enabled", foreground="black")
        self.daily_label.tag_configure("disabled", foreground="grey")
        self.daily_label.config(state="disabled")

    def switch_toggled(self):
        self.update_frame()

    def get_alarm_num(self):
        return self.ui.get_alarm_num(self)

    def edit_alarm(self):
        self.ui.edit_alarm(self.get_alarm_num())

    def delete_alarm(self):
        self.ui.delete_alarm(self)

    def show_frame(self, row):
        self.frame.grid(row=row, column=0, sticky="nsew",
                        padx=10, pady=5)

    def hide_frame(self):
        self.frame.grid_forget()