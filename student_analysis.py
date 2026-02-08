#Project:Student Performance Analysis
#Author : Seher Anjum Budye
#Level: First Year Mini Project
#Description:
#1)This program analyzes student marks and attendance.
#2)It calculates total,average,grade and attendance status for each student
#3)It also finds class average,topper and counts students with good attendance
#-----------------------------------------------------------------------
#Storing student data in lists
names=["Aisha","Anya","Raj","Tara","Aman","Neha","Rohan","Pooja"]
maths=[85,70,60,95,78,88,72,90]
science=[90,80,75,85,82,91,68,94]
attendance=[95,88,90,92,87,96,85,98]
def assign_grade(avg):  #Function to assign grade based on average marks
    if avg>=85:
        return "A"
    elif avg>=70:
        return "B"
    else:
        return "C"
def attendance_status(att): #Function to assign attendance status
    if att >= 90:
        return "Good"
    else:
        return "Needs Improvement"
grades=[]
#Main loop to calculate total,average,grade and status for each student
for i in range(len(names)):
    total = maths[i]+science[i]
    average=total/2
    grade=assign_grade(average)
    status=attendance_status(attendance[i])
    print("Name:",names[i],"| Total:",total,"| Average:",average,"| Grade:",grade,"| Status:",status)
    grades.append(grade)
print("\nGrades List:",grades)  #Display list of all grades
total_class_avg=0   #Calculate and display class average
for i in range(len(names)):
    avg=(maths[i]+science[i])/2
    total_class_avg+=avg
class_average=total_class_avg/len(names)
print("\nClass Average:",class_average)
highest_avg=0
topper=""
for i in range(len(names)):   #Find and display topper of the class 
    avg=(maths[i]+science[i])/2
    if avg>highest_avg:
        highest_avg=avg
        topper=names[i]
print("\nTopper:",topper,"with average:",highest_avg)
good_attendance_count=0
for att in attendance:  #Count number of students with good attendance
    if att>=90:
        good_attendance_count+=1
print("Students with Good Attendance:",good_attendance_count)

#End of Student Performance Analysis Program    
                                                

