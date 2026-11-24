import csv
import os 

class Student:
    def __init__(self, fullname, section, spanish_grade, english_grade, history_grade, sciences_grade ):
        self.fullname = fullname
        self.section = section
        self.spanish_grade = float(spanish_grade)
        self.english_grade = float(english_grade)
        self.history_grade = float(history_grade)
        self.sciences_grade = float(sciences_grade)
        self.average = self.calculate_average()
        
    
    def calculate_average(self):

        grades = [ self.spanish_grade, self.english_grade, self.history_grade, self.sciences_grade]
        return sum(grades) / len(grades) if grades else 0 

    def __str__(self):
        return f'fullname: {self.fullname}, section: {self.section}, average: {self.average:.2f}'


    def __repr__(self):
        return f"Student(fullname ='{self.fullname}', section ='{self.section}', spanish_grade = {self.spanish_grade}, english_grade = {self.english_grade}, history_grade = {self.history_grade}, sciences_grade = {self.sciences_grade})"
    


def add_student ():
    
    students = []
        
    while True:
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

        student = Student(fullname, section, spanish_grade, english_grade, history_grade, sciences_grade)
        students.append(student)

        while True:
            add_another = input('Would you like to add another student?(yes/no): ')
            if add_another.lower() in ['yes', 'no']:
                break
            else: 
                print('Invalid input. Please answer "yes" or "no".')

        if add_another.lower()=='no':
            break

    return students



def save_csv(students_list, file_name, export_option ='overwrite'):
    try:  
        file_exists = os.path.isfile(file_name)
        write_mode = 'w' if export_option == 'overwrite' else 'a'
        write_header = not file_exists or export_option == 'overwrite'


        with open (file_name, write_mode, newline='', encoding='utf-8') as file_csv:
            fieldnames = ['fullname', 'section', 'spanish_grade', 'english_grade', 'history_grade', 'sciences_grade']
            write_csv = csv.DictWriter(file_csv, fieldnames=fieldnames)
            if write_header:
                write_csv.writeheader()
            for student in  students_list:
                write_csv.writerow({
                    'fullname': student.fullname,
                    'section': student.section,
                    'spanish_grade': student.spanish_grade,
                    'english_grade': student.english_grade,
                    'history_grade': student.history_grade, 
                    'sciences_grade' : student.sciences_grade
                })

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
        if isinstance(row, Student):    
            student_data = {
                'fullname': row.fullname, 
                'section' : row.section,
                'spanish_grace' : row.spanish_grade,
                'english_grade': row.english_grade,
                'history_grade': row.history_grade,
                'sciences_grade' : row.sciences_grade,
                'average' : row.average
            }

            for i, header in enumerate(headers):
                column_widths[i] = max(column_widths[i], len(str(student_data.get(header,'')) ))
        else:
            print(f' Invalid row{row}')
            return
        
    separator='-' * (sum(column_widths) + len(headers)* 3-1)
    print(separator)
    formatted_header_row = '|' + '|'.join(f'{header:<{column_widths[i]}}' for i, header in enumerate(headers)) + '|'
    print(formatted_header_row)
    print(separator)

    for row in data : 
        if isinstance (row, Student):
            student_data ={
                'fullname': row.fullname, 
                'section' : row.section, 
                'spanish_grade' : row.spanish_grade,
                'english_grade' : row.english_grade,
                'history_grade' : row.history_grade,
                'sciences_grade' : row.sciences_grade,
                'average': f'{row.average:.2f}'
            }

            formatted_row = '|' + '|'.join(f'{str(student_data.get(header,'')): <{column_widths[i]}}' for i, header in enumerate(headers)) +'|'
            print(formatted_row)
        else:
            print(f' Invalid row{row}')
    print(separator)


def display_top_average_from_list(students):
    if students:
        students_sorted= sorted(students, key= lambda student: student.average, reverse = True)
        top_3_students = students_sorted[:3]
        display_as_table(top_3_students,['fullname', 'average'])

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
                total_average = sum(student.average for student in students)
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
                    student = Student (
                        row.get('fullname',''),
                        row.get('section', ''),
                        float(row.get('spanish_grade', '0')),
                        float(row.get('english_grade', '0')),
                        float(row.get('history_grade', '0')),
                        float(row.get('sciences_grade', '0'))
                        )   
                    imported_students.append(student)                
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
    