import csv
import os 

def add_student ():
    
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

    return student


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


def save_csv(students_list, file_name):
    try:  
        file_exists = os.path.isfile(file_name)

        with open (file_name,'a', newline='', encoding='utf-8') as file_csv:
            fields = students_list[0].keys()
            write_csv= csv.DictWriter(file_csv, fieldnames=fields)


            if not file_exists or os.stat(file_name). st_size == 0:
                write_csv.writeheader()
                write_csv.writerows(students_list)

            print(f'Data saved correctly in {file_name}')
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
        for i, header in enumerate(headers):
            column_widths[i] = max(column_widths[i], len(str(row.get(header,'')) ))
    separator='-' * (sum(column_widths) + len(headers)* 3-1)
    print(separator)
    formatted_header_row = '|'.join(f'{header:<{column_widths[i]}}' for i, header in enumerate(headers))
    print(formatted_header_row)
    print(separator)

    for row in data : 
        formatted_row = '|'.join(f'{str(row.get(header,'')): <{column_widths[i]}}' for i, header in enumerate(headers))
        print(formatted_row)
    print(separator)


def display_csv_with_average(file_name ):
    try: 
        with open (file_name, 'r', newline='', encoding='utf-8' ) as file_csv:
            reader_csv = csv.DictReader(file_csv)
            students = list(reader_csv)
            if students:
                students_sorted= sorted(students, key= lambda x:float(x['average']), reverse = True)

                top_3_students = students_sorted[:3]

                headers = ['fullname', 'average']
                data_table = [{'fullname': student['fullname'],'average':student['average']} for student in top_3_students]
                display_as_table(data_table,headers)
            
            else:
                print(f'No data found in {file_name}.')
    except FileNotFoundError:
        print(f'Error: The file {file_name} was not found. ')
    except Exception as e:
            print(f'An error occurred while processing the CSV file {e}')


def all_list( file_name):

    try:
        with open (file_name, 'r', newline='', encoding= 'utf-8' ) as file_csv:
            reader_csv = csv.DictReader(file_csv)
            students = list(reader_csv)
            if students:
                headers = ['fullname', 'section', 'spanish_grade', 'english_grade', 'history_grade','sciences_grade']
                display_as_table(students, headers)
            else:
                print(f'No data found in {file_name}.')
    except FileNotFoundError:
        print(f'Error: The file {file_name} was not found.')
    except Exception as e:
        print(f'An error occurred while opening the CSV file: {e}')


def display_class_average(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file_csv:
            reader_csv=csv.DictReader(file_csv)
            students= list(reader_csv)

            if not students:
                print(f'Error: No data found in {file_name}')
                return
            
            total_average = 0
            for student in students:
                total_average += float(student.get('average',0))

            class_average= total_average / len(students) if students else 0

            print(f'Average of the class: {class_average:.2f}')

    except FileNotFoundError:
        print(f'Error: The file{file_name} was not found.')
    except Exception as e:
        print(f'An error occurred while processing the CSV file{e}')


def import_csv(file_name):
    try: 
        with open (file_name, 'r', newline ='', encoding='utf-8') as file_csv:
            reader_csv= csv.DictReader(file_csv)
            students = list(reader_csv)
            if students:
                print('Students imported successfully: ')
                headers = students[0].keys()
                display_as_table(students, headers)
            else: 
                print(' The CSV file is empty.')
    except FileNotFoundError:
        print(f'Error: File{file_name} not found.')
    except Exception as e :
        print(f'An error occurred:{e}')