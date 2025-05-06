import actions
import data



def menu():
    students =[]
    while True: 
        print('\n--- Student Management System ---')
        print('1. Add a new student')
        print('2. Display top 3 averages ' )
        print('3. Display all students list')
        print('4. Display class average')
        print('5. Import student from CVS')
        print('6. Export student from CVS')
        print('7. Clear student list')
        print('8. Exit')

        while True:
            choice = input('Enter your choice(1-8):')
            if choice in ('1','2','3','4','5','6','7','8'):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
            
        if choice == '1':
            new_students = data.add_student()
            if new_students:
                students.extend(new_students)
        elif choice == '2':
            actions.display_top_averages(students)
        elif choice == '3':
            actions.display_all_students(students)
        elif choice == '4':
            actions.display_class_average(students)
        elif choice == '5':
            file_name = input('Enter the name of the CSV file to import: ')
            students, message = actions.import_students_from_csv(file_name, students)
            print(message)
        elif choice == '6':
            file_name = input('Enter the name for the CSV file to export to: ')
            message = actions.export_students_from_csv(students, file_name)
            print(message)
        elif choice == '7':
            students = actions.clear_student_list(students)
        elif choice == '8':
            print('Exiting...')
            break