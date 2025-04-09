import actions
import data
import os 


def menu():
    while True: 
        print('\n--- Student Management System ---')
        print('1. Add a new student')
        print('2. Display top 3 averages ' )
        print('3. Display all students list')
        print('4. Display class average')
        print('5. Import student from CVS')
        print('6. Exit')

        while True:
            choice = input('Enter your choice(1-6):')
            if choice in ('1','2','3','4','5','6'):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
            
        if choice == '1':
            actions.add_new_student('students.csv')
        elif choice == '2':
            actions.display_top_averages()
        elif choice == '3':
            actions.display_all_students()
        elif choice == '4':
            actions.display_class_average()
        elif choice == '5':
            actions.import_students_from_csv('students.csv')
        elif choice == '6':
            print('Exiting...')
            break
