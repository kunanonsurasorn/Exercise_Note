import csv

exercise_list = list()
date_exercise_data = list()

date_exercise_period = input("Enter the exercise date (Day/Month/Year Example: 20/12/2020): ")
type_exercise_data = input("Enthe the exercise type (Example: Aerobic, Cycling etc): ")
time_exercise_data = input("Enter the exercise time (Example: 30 minutes): ")

date_exercise_data.append(date_exercise_period)
date_exercise_data.append(type_exercise_data)
date_exercise_data.append(time_exercise_data)
exercise_list.append(date_exercise_data)

with open('exercise_note.csv', 'a', newline='') as file:
    csv_exercise_file = csv.writer(file)
    csv_exercise_file.writerow(date_exercise_data)

