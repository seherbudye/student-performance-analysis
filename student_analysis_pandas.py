# ----------------------------------------
# Project: Student Performance Analysis (Pandas Version)
# Author: Seher
# Level: First Year Mini Project
# Description:
# This program uses pandas to analyze student performance
# from a CSV file.
# ----------------------------------------

import pandas as pd

# Load data from CSV
data = pd.read_csv("student_data.csv")
data.columns=data.columns=data.columns.str.strip()   #Clean column names (remove spaces)
print("Student Data:\n")
print(data)

# Calculate Total and Average
data["Total"] = data["Maths"] + data["Science"]
data["Average"] = data["Total"] / 2

print("\nData with Total and Average:\n")
print(data)

# Function to assign grade based on average
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

# Apply grade function
data["Grade"] = data["Average"].apply(assign_grade)

print("\nData with Grades:\n")
print(data)

# Function to assign attendance status
def assign_attendance(att):
    if att >= 90:
        return "Good"
    else:
        return "Needs Improvement"

# Apply attendance status
data["Attendance_Status"] = data["Attendance"].apply(assign_attendance)

print("\nData with Attendance Status:\n")
print(data)

# Calculate class average
class_average = data["Average"].mean()

print("\nClass Average:", class_average)

# Find topper
topper_row = data.loc[data["Average"].idxmax()]

print("\nTopper Details:")
print(topper_row)

