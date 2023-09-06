

from tkinter import*
import webbrowser
from tkinter import ttk



windows = Tk()
windows.title('myapplication')
windows.geometry('720x720')
windows.config(background='#41B77f')


#fram
frame = Frame(windows, bg='#353535', bd=1)

#text
user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = Label(user_info_frame, text="Age")
age_spinbox = Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)
               





windows.mainloop()