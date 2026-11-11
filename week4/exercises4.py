#Clasificacion de notas


Counter_note = 1
number_of_approved_grades = 0
number_of_failed_grades = 0
average_of_passed_grades = 0
average_of_failed_grades = 0 
total_grade_average = 0
total_grades = 0
current_note=0

total_grades = int(input("Input the total grades: "))

while Counter_note<=total_grades:
    current_note=int(input(f"Input the note {Counter_note}: "))
    Counter_note+=1
    total_grade_average+=current_note
    if current_note < 70 :
        number_of_failed_grades+=1
        average_of_failed_grades+=current_note
    else:
        number_of_approved_grades+=1
        average_of_passed_grades+=current_note
if number_of_approved_grades>0:
    average_of_failed_grades/=number_of_failed_grades
else:
    average_of_failed_grades=0

if number_of_approved_grades>0:
    average_of_passed_grades/=number_of_approved_grades
else:
    average_of_passed_grades=0


total_grade_average= total_grade_average/total_grades

print (f"The student has this number of approved grades: {number_of_approved_grades} ")
print (f"This is the passing grade average: {average_of_passed_grades} ")
print (f"The student has this number of failed grades: {number_of_failed_grades} ")
print (f"This is the average of failed grades {average_of_failed_grades} ")
print (f"This is the total grade average: {total_grade_average} ")
