import data 

def display_top_averages(students):
    data.display_top_average_from_list(students)


def display_all_students(students):
    data.all_list_from_list(students)


def display_class_average(students):
    data.display_class_average_from_list(students)


def import_students_from_csv(file_name, current_students):
    updated_students, message = data.import_csv(file_name, current_students)
    return updated_students, message


def export_students_from_csv(students, file_name):
    while True: 
        export_option = input(f' Do you want to overwrite existing data in {file_name}(overwrite) or add to it (add)? (overwrite/add): ')
        if export_option.lower() in ['overwrite', 'add']:
            break
        else:
            print('Invalid choice. Please answer  "overwrite" or "add".')

    data.save_csv(students, file_name, export_option.lower())
    return f'Data exported correctly to {file_name} ({export_option} mode)'



def clear_student_list(students_list):

    if students_list:
        confirm = input('Are you sure  you want to clear the entire student list?(yes/no): ')
        if confirm.lower() == 'yes':
            students_list.clear()
            print('Student list cleared.')
        else:
            print('Clear operation cancelled.')
    else:
        print('The student list is already empty.')
    return students_list