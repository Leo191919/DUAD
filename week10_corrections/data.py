import csv
import os 

def add_student ():
    
    students = []
        
    while True:
        student = {}

        while True:
            fullname = input('Please, input the fullname: ')
            if fullname.strip():
                break
            else:
                print('Invalid input for fullname. Please enter a valid name.')


        while True:

            section = input('Please, input the section: ')
            if section.strip():
                break
            else:
                print('Invalid input for section. Please enter a valid section.')



        while True:
            try:
                spanish_grade = float(input("Please, input the spanish grade: "))
                if 0 <= spanish_grade <= 100:
                    break
                else:
                    print('Invalid input for spanish grade. Please enter a number between 0 and 100')
            except ValueError:
                print("Invalid input for spanish grade. Please enter a number" )

        while True:
            try:
                english_grade =float(input("Please, input the english grade: "))
                if 0 <= english_grade <= 100:
                    break
                else: 
                    print('Invalid input for english grade. Please enter the number between 0 and 100')
            except ValueError:
                print("Invalid input for english grade. Please enter a number" )
                
        while True:
            try:
                history_grade = float(input("Please, input the history grade: "))
                if 0 <= history_grade <= 100:
                    break
                else: 
                    print('Invalid input for history grade. Please enter a number between 0 and20 100.')
            except ValueError:
                print("Invalid input for history grade. Please enter a number" )

        while True:
            try:
                sciences_grade =float( input("Please, input the sciences grade: "))
                if 0 <= sciences_grade <= 100:
                    break
                else:
                    print('Invalid input for sciences grade. Please enter the number between 0 and 100.')
            except ValueError:
                print("Invalid input for sciences grade. Please enter a number." )

        student['fullname'] = fullname
        student['section'] = section
        student['spanish_grade'] = spanish_grade
        student['english_grade'] = english_grade
        student['history_grade'] = history_grade
        student['sciences_grade'] = sciences_grade
        students.append(student)
        calculate_average(students)

        while True:
            add_another = input('Would you like to add another student?(yes/no): ')
            if add_another.lower() in ['yes', 'no']:
                break
            else: 
                print('Invalid input. Please answer "yes" or "no".')

        if add_another.lower()=='no':
            break

    return students


def calculate_average(student_list):

    for student in student_list:
        grade = [
            student.get('spanish_grade',0),
            student.get('english_grade',0), 
            student.get('history_grade',0),
            student.get('sciences_grade',0),
        ]
        average = sum(grade) / len(grade) if grade else 0 
        student['average'] = average


def save_csv(students_list, file_name, export_option ='overwrite'):
    try:  
        file_exists = os.path.isfile(file_name)
        write_mode = 'w' if export_option == 'overwrite' else 'a'
        write_header = not file_exists or export_option == 'overwrite'


        with open (file_name, write_mode, newline='', encoding='utf-8') as file_csv:
            fields = students_list[0].keys()
            write_csv= csv.DictWriter(file_csv, fieldnames=fields)
            if write_header:
                write_csv.writeheader()
            write_csv.writerows(students_list)

            print(f'Data saved correctly in {file_name} ({export_option} mode)')
    except FileNotFoundError:
        print(f'Error: File {file_name} could not be found.')
    except Exception as e :
        print(f'Error saving CSV file{e}')


def display_as_table(data, headers):
    if not data:
        print('No data to display.')
        return
    column_widths = [len(header) for header in headers]
    for row in data:
        if isinstance(row, dict):    
            for i, header in enumerate(headers):
                column_widths[i] = max(column_widths[i], len(str(row.get(header,'')) ))
        else:
            print(f' Invalid row{row}')
    separator='-' * (sum(column_widths) + len(headers)* 3-1)
    print(separator)
    formatted_header_row = '|'.join(f'{header:<{column_widths[i]}}' for i, header in enumerate(headers))
    print(formatted_header_row)
    print(separator)

    for row in data : 
        if isinstance (row, dict):
            formatted_row = '|'.join(f'{str(row.get(header,'')): <{column_widths[i]}}' for i, header in enumerate(headers))
            print(formatted_row)
        else:
            print(f' Invalid row{row}')
    print(separator)


def display_top_average_from_list(students):
    if students:
        students_sorted= sorted(students, key= lambda x:float(x['average']), reverse = True)
        top_3_students = students_sorted[:3]
        headers = ['fullname', 'average']
        data_table = [{'fullname': student['fullname'],'average':student['average']} for student in top_3_students]
        display_as_table(data_table,headers)

    else:
        print(f'No data found.')


def all_list_from_list( students):

    if students:
        headers = ['fullname', 'section', 'spanish_grade', 'english_grade', 'history_grade','sciences_grade','average']
        display_as_table(students, headers)
    else:
        print(f'No data found.')


def display_class_average_from_list(students):

            if students:
                total_average = sum(student['average'] for student in students)
                class_average = total_average / len(students)
                print(f'Average of the class:{class_average:.2f}')
            else:
                print('No data found.')

def import_csv(file_name, current_students):

    imported_students = []
    try: 
        with open (file_name, 'r', newline ='', encoding='utf-8') as file_csv:
            reader_csv = csv.DictReader(file_csv)
            for row in reader_csv:
                try:
                    row['fullname'] = row.get('fullname','')
                    row['section'] = row.get('section','')
                    row['spanish_grade'] = float(row.get('spanish_grade','0'))
                    row['english_grade'] = float(row.get('english_grade','0'))
                    row['history_grade'] = float(row.get('history_grade','0'))
                    row['sciences_grade'] = float(row.get('sciences_grade','0'))
                    imported_students.append(row)                
                except ValueError as e:
                    print(f'Error processing row {row}. Error: {e}')
                    return current_students, 'Error: Invalid grade format in CSV. Importation failed.'
                except KeyError as e :
                    print(f'Error: Missing column in csv: {e}' )
                    return current_students, 'Error: Missing required column in CSV. Importation failed.'

            current_students.extend(imported_students)
            return current_students, f'{len(imported_students)} students added successfully. '

    except FileNotFoundError:
        return current_students, f'Error: File {file_name} not found. '
    except Exception as e: 
        return current_students, f'An error occurred: {e}'
    