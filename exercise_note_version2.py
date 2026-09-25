import tkinter as tk
import csv

exercise_type_list = ["Aerobic","Cycling","Weight Training"]

exercise_list = list()
date_exercise_data = list()

main_window = tk.Tk()
main_window.geometry("405x290")
main_window.title("Exercise Note")
main_window.resizable(False,False)

def start_program():
    month_input_box.config(state="normal")
    day_input_box.config(state="normal")
    year_input_box.config(state="normal")
    minute_input_box.config(state="normal")
    exercise_record_button.config(state="normal")
    reset_exercise_program_button.config(state="normal")

def exercise_recording_script():

    exercise_today_month = month_input_box.get()
    exercise_today_day = day_input_box.get()
    exercise_today_year = year_input_box.get()
    exercise_totay_type = exercise_type_var.get()
    exercise_today_minute = minute_input_box.get()

    exercise_time_format(exercise_today_month,exercise_today_day,exercise_today_year,exercise_totay_type,exercise_today_minute)

def exercise_time_format(exercise_today_month,exercise_today_day,exercise_today_year,exercise_totay_type,exercise_today_minute):
    
    date_exercise_period = f"{exercise_today_day}/{exercise_today_month}/{exercise_today_year}"
    type_exercise_data = exercise_totay_type
    time_exercise_data = f"{exercise_today_minute} minutes"
    
    exercise_list_record(date_exercise_period,type_exercise_data,time_exercise_data)

def exercise_list_record(date_exercise_period,type_exercise_data,time_exercise_data):
    
    date_exercise_data.append(date_exercise_period)
    date_exercise_data.append(type_exercise_data)
    date_exercise_data.append(time_exercise_data)
    exercise_list.append(date_exercise_data)

    with open('exercise_note.csv', 'a', newline='') as file:
        csv_exercise_file = csv.writer(file)
        csv_exercise_file.writerow(date_exercise_data)

def reset_the_program():
    global exercise_today_month,exercise_today_day,exercise_today_year,exercise_totay_type,exercise_today_minute,exercise_list,date_exercise_data,month_input_box
    
    month_input_box.delete(0,tk.END)
    month_input_box.config(state="disabled")

    day_input_box.delete(0,tk.END)
    day_input_box.config(state="disabled")

    year_input_box.delete(0,tk.END)
    year_input_box.config(state="disabled")

    minute_input_box.delete(0,tk.END)
    minute_input_box.config(state="disabled")

    exercise_record_button.config(state="disabled")

    reset_exercise_program_button.config(state="disabled")

    exercise_type_var.set("-")

    exercise_today_month = None
    exercise_today_day = None
    exercise_today_year = None
    exercise_totay_type = None
    exercise_today_minute = None

    exercise_list = list()
    date_exercise_data = list()

#ROW 0 

exercise_note_label = tk.Label(main_window,text="Exercise Note")
exercise_note_label.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

#ROW 1 

start_exercise_program_button = tk.Button(main_window,text="Start",command=start_program)
start_exercise_program_button.grid(row=1, column=1,padx=5,pady=5)

#ROW 2 

month_input_label = tk.Label(main_window,text="Month")
month_input_label.grid(row=2,column=0,padx=10,pady=10)

day_input_label = tk.Label(main_window,text="Day")
day_input_label.grid(row=2,column=1,padx=10,pady=10)

year_input_label = tk.Label(main_window,text="Year")
year_input_label.grid(row=2,column=2,padx=10,pady=10)

#ROW 3

month_input_box = (tk.Entry(main_window))
month_input_box.config(state="disabled")
month_input_box.grid(row=3,column=0,padx=5,pady=5)

day_input_box = (tk.Entry(main_window))
day_input_box.config(state="disabled")
day_input_box.grid(row=3,column=1,padx=5,pady=5)

year_input_box = (tk.Entry(main_window))
year_input_box.config(state="disabled")
year_input_box.grid(row=3,column=2,padx=5,pady=5)

#ROW 4

exercise_type_label = tk.Label(main_window,text="Exercise Type")
exercise_type_label.grid(row=4,column=0,padx=10,pady=10)

minute_input_label = tk.Label(main_window,text="Minute")
minute_input_label.grid(row=4,column=1,padx=5,pady=5)

#ROW 5 

exercise_type_var = tk.StringVar()
exercise_type_var.set("-")
input_exercise_type_selection = tk.OptionMenu(main_window,exercise_type_var,*exercise_type_list)
input_exercise_type_selection.grid(row = 5, column = 0,padx=10,pady=10)

minute_input_box = (tk.Entry(main_window))
minute_input_box.config(state="disabled")
minute_input_box.grid(row=5,column=1,padx=5,pady=5)

exercise_record_button = tk.Button(main_window,text="Save",command=exercise_recording_script)
exercise_record_button.config(state="disabled")
exercise_record_button.grid(row=5, column=2,padx=5,pady=5)

#ROW 6

reset_exercise_program_button = tk.Button(main_window,text="Reset",command=reset_the_program)
reset_exercise_program_button.config(state="disabled")
reset_exercise_program_button.grid(row=6, column=1,padx=5,pady=5)

main_window.mainloop()