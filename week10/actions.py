import data 

def add_new_student (file_name):
    students = []
    while True:
        new_student = data.add_student()
        students.append(new_student)
        data.calculate_average(students)

        add_another = input('Would you like to add another student?(yes/no)')
        if add_another.lower()!= 'yes':
            break
    data.save_csv(students, file_name)

def display_top_averages():
    data.display_csv_with_average('students.csv')


def display_all_students():
    data.all_list('students.csv')


def display_class_average():
    data.display_class_average('students.csv')

def import_students_from_csv(file_name):
    data.import_csv(file_name)