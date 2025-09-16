import PySimpleGUI as sg
import datetime
from logic import Finance_manager



my_manager = Finance_manager()

def calendar_window():
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day

    layout = [
        [sg.calendar(
            pad=None, 
            close_when_date_chosen=True,
            target = (None, '-CALENDAR-'),
            default_date_m_d_y=(month, day, year), 
            locale = 'en_US',
            format = '%Y-%m-%d',
            key= '-CALENDAR-'
            ) ],
        [sg.Button('OK', key= '-CALENDAR_OK-'),sg.Button('Cancel', key= '-CALENDAR_CANCEL-')]
    ]

    calendar_win = sg.Window('Calendar', layout, modal = True)
    date_chosen = None
    while True:
        event, values = calendar_win.read()
        if event in (sg.WIN_CLOSED, '-CALENDAR_CANCEL-'):
            break
        elif event == '-CALENDAR_OK-':
            date_chosen = values['-CALENDAR-']
            break

    calendar_win.close()
    return date_chosen

def manage_categories_window(manager):
    layout_manage_categories = [
        [sg.Text("Add New Category:")],
        [sg.Input(key = "-NEW_CATEGORY_INPUT-")],
        [sg.Button("Add", key = "-ADD_CATEGORY_BTN-"), sg.Button("Close", key = "-CLOSE_CATEGORIES_BTN-")],
        [sg.Listbox(values=manager.category_manager.get_categories(), size=(30, 6), key="-CATEGORY_LIST-")]
    ]

    categories_window = sg.Window("Manage Categories", layout_manage_categories)
    while True: 
        event, values = categories_window.read()
        if event ==sg.WIN_CLOSED or event == "-CLOSE_CATEGORIES_BTN-":
            break
        elif event == "-ADD_CATEGORY_BTN-":
            new_category = values["-NEW_CATEGORY_INPUT-"].strip()
            if new_category and new_category not in manager.category_manager.get_categories():
                manager.category_manager.add_category(new_category)
                categories_window["-CATEGORY_LIST-"].update(values=manager.category_manager.get_categories())
                categories_window["-NEW_CATEGORY_INPUT-"].update("")
            else:
                sg.popup_error("Category cannot be empty or already exists.")
    categories_window.close()

def add_movement_window(manager, kind = "income"):
    is_income = kind == "income"
    is_expense = kind == "expense"


    layout_add_movement = [  
        [sg.Text(f"Add new {kind.capitalize()}:")],
        [sg.Radio("Income", "RADI01", default = is_income, key = '-KIND_INCOME-')],
        [sg.Radio("Expense", "RADI01", default = is_expense, key = '-KIND_EXPENSE-')],
        [sg.Text("Amount:")],
        [sg.Input(key ='-AMOUNT_INPUT-')],
        
        [sg.Text("Description:")],
        [sg.Input(key='-DESCRIPTION_INPUT-')],

        [sg.Text("Date (YYYY-MM-DD):")],
        [sg.Input(key = "-DATE_INPUT-", size= (12, 1 ), disabled = True),
        sg.Button("Choose Date", key = "-CALENDAR_BTN-")],

        [sg.Text("Category")],
        [sg.Combo(manager.category_manager.get_categories(), key = "-CATEGORY_INPUT-", readonly = True)],
        [sg.Button("Manage Categories", key = "-MANAGE_CATEGORIES_BTN-")],
        [sg.Button("Add", key = "-ADD_MOVEMENT_BTN-"), sg.Button("Cancel", key ="-CANCEL_BTN-")]
        ]

    emergent_window = sg.Window("Add New Movement", layout_add_movement)

    while True:
        event_emergent, values_emergent = emergent_window.read()

        if event_emergent == sg.WIN_CLOSED or event_emergent == "-CANCEL_BTN-":
            break
        elif event_emergent == "-CALENDAR_BTN-":
            date_chosen = calendar_window()
            if date_chosen:
                emergent_window['-DATE_INPUT-'].update(date_chosen[0])
        elif event_emergent == "-MANAGE_CATEGORIES_BTN-":
            manage_categories_window(manager)
            emergent_window['-CATEGORY_INPUT-'].update(values=manager.category_manager.get_categories()) 

        elif event_emergent == "-ADD_MOVEMENT_BTN-":
            description = values_emergent['-DESCRIPTION_INPUT-'].strip()
            category = values_emergent['-CATEGORY_INPUT-']
            amount = values_emergent['-AMOUNT_INPUT-'].strip()
            date = values_emergent['-DATE_INPUT-'].strip()

            if not description or not category or not date or not amount:
                sg.popup_error("All the fields must be filled.")
                continue
    
            try: 
                amount_movement = float(values_emergent['-AMOUNT_INPUT-'])
            except ValueError:
                sg.popup_error("Please enter a valid amount.")
                continue

            kind_movement = "income" if values_emergent['-KIND_INCOME-'] else "expense"            

            data_movement =  { 
                "kind": kind_movement,
                "amount": amount_movement,
                "description": description,
                "date": date,
                "category": category
            }
            emergent_window.close()
            return data_movement
    
    emergent_window.close()
    return None
        


def edit_movement_window(manager,movement_data):
    is_income = movement_data['kind'].lower() == 'income'
    is_expense = movement_data['kind'].lower() == 'expense'

    layout_edit_movement= [
        [sg.Text("Kind movement(Income/Expense):")],
        [sg.Radio("Income", "RADIO1", default = is_income, key = '-KIND_INCOME-' )],
        [sg.Radio("Expense", "RADIO1", default= is_expense, key = '-KIND_EXPENSE-' )],

        [sg.Text("Amount:")],
        [sg.Input(default_text= f"{movement_data['amount']}", key= '-AMOUNT_INPUT-')],

        [sg.Text("Description:")],
        [sg.Input(default_text=movement_data['description'], key= '-DESCRIPTION_INPUT-' )],

        [sg.Text("Date ( YYYY-MM-DD ):")],
        [sg.Input(default_text=movement_data['date'], key = '-DATE_INPUT-', size=(12,1), disabled = True),
        sg.Button("Choose Date", key = '-CALENDAR_BTN-')],
        [sg.Text("Category")],
        [sg.Combo(manager.category_manager.get_categories(), key = "-CATEGORY_INPUT-", readonly =  True,
                default_value= movement_data['category'] )],

        [sg.Button("Manage Categories", key = 'MANAGE_CATEGORIES_BTN-')],
        [sg.Button("Save Changes", key = '-SAVE_CHANGES_BTN-'), sg.Button( "Cancel", key = '-CANCEL_BTN-' )]

    ]

    emergent_window = sg.Window("Edit Movement", layout_edit_movement)

    while True:
        event_emergent, values_emergent = emergent_window.read()


        if event_emergent == sg.WIN_CLOSED or event_emergent == '-CANCEL_BTN-':
            break
        elif event_emergent == '-CALENDAR_BTN-':
            date_chosen = calendar_window()
            if date_chosen:
                emergent_window['-DATE_INPUT-'].update(date_chosen[0])  

        elif event_emergent == '-MANAGE_CATEGORIES_BTN-':
            manage_categories_window(manager)
            emergent_window['-CATEGORY_INPUT-'].update(values=manager.category_manager.get_categories())
        elif event_emergent == '-SAVE_CHANGES_BTN-':
            kind_movement = "income" if values_emergent ['-KIND_INCOME-'] else "expense"

            try: 
                amount_movement = float(values_emergent['-AMOUNT_INPUT-'])
            except ValueError:
                sg.popup_error( "Please enter a valid amount." )
                continue

            edited_data = {
                "kind": kind_movement,
                "amount": amount_movement, 
                "description": values_emergent['-DESCRIPTION_INPUT-'],
                "date" : values_emergent['-DATE_INPUT-'],
                "category" : values_emergent['-CATEGORY_INPUT-']
            }
            emergent_window.close()
            return edited_data


def get_movements_for_table(manager):
    table_data = [] 
    for mov in manager.movements: 
        table_data.append([
            mov.type.capitalize(),
            f"{mov.amount:.2f}",
            mov.description, 
            mov.date, 
            mov.category
            ])
    return table_data


def update_main_display(window, manager):
    current_movements_data= get_movements_for_table(manager)
    window['-MOVEMENTS_TABLE-'].update(values=current_movements_data)

    current_balance = manager.calculate_total_balance()
    window['-BALANCE_TEXT-'].update(value=f'Current Balance: {current_balance:.2f}')

layout = [
    [sg.Button("Add Income", key = '-ADD_INCOME_BTN-'),
    sg.Button("Add Expense", key = '-ADD_EXPENSE_BTN-' ), 
    sg.Button("Remove Movement", key = '-REMOVE_MOVEMENT_BTN-'),
    sg.Button("Edit Movement", key =  '-EDIT_MOVEMENT_BTN-')],

    [sg.Table(values= [],
            headings =['Type', 'Amount', 'Description', 'Date', 'Category'],
            display_row_numbers = False, 
            auto_size_columns = True, 
            num_rows =  10,
            justification = 'left', 
            key = '-MOVEMENTS_TABLE-',
            enable_events = True,
            select_mode = 'browse')],

    [sg.Text('Current Balance: $0.00', key = '-BALANCE_TEXT-', font = ('Helvetica', 12, 'bold'))],
    [sg.Button("Exit", key = '-EXIT_BTN-')]
]

window = sg.Window("Manager finances", layout, finalize = True)

update_main_display(window, my_manager)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-EXIT_BTN-":
        my_manager.save_data()
        break
    
    elif event == '-ADD_INCOME_BTN-':
        data_movement = add_movement_window(my_manager, kind="income")

        if data_movement:
            if my_manager.add_movement(
                data_movement['kind'],
                data_movement['amount'],
                data_movement['description'],
                data_movement['date'],
                data_movement['category']
            ):
                sg.popup_ok("Income added successfully!")
                update_main_display(window, my_manager)
            else: 
                sg.popup_error("Could not add movement. Please check data (positive amount, valid date/type).")

    elif event == '-ADD_EXPENSE_BTN-':
        data_movement = add_movement_window(my_manager, kind="expense")
        if data_movement:
            if my_manager.add_movement(
                data_movement['kind'],
                data_movement['amount'],
                data_movement['description'],
                data_movement['date'],
                data_movement['category']
            ):
                sg.popup_ok("Expense added successfully!")
                update_main_display(window, my_manager)
            else:
                sg.popup_error("Could not add expense. Please check data(positive amount, valid date/type).")

    elif event == "-REMOVE_MOVEMENT_BTN-":
        select_rows_indices = values['-MOVEMENTS_TABLE-']

        if not select_rows_indices:
            sg.popup_error ("Please select a movement from the table to remove.")
        else:
            index_to_delete = select_rows_indices[0]

            confirm = sg.popup_yes_no(f"Are you sure you want to delete the selected movement (row{index_to_delete + 1 })?")
            
            if confirm == 'Yes':
                if my_manager.remove_movement (index_to_delete):
                    sg.popup_ok("Movement deleted successfully!")
                    update_main_display(window, my_manager)

                else :
                    sg.popup_error("could  not delete movement. Invalid index or internal error. ")
            else: 
                sg.popup_ok ("Deletion canceled. ")

    elif event == "-EDIT_MOVEMENT_BTN-":
        select_rows_indices = values['-MOVEMENTS_TABLE-']
        if not select_rows_indices:
            sg.popup_error("Please select a movement from the table to edit. ")
        elif len(select_rows_indices) > 1:
            sg.popup_error("Please select only one movement to edit.")
        else:
            index_to_edit = select_rows_indices[0]
            if 0 <= index_to_edit < len(my_manager.movements ):
                movement_to_edit = my_manager.movements[index_to_edit ]

                data_for_edit_window = {
                    "kind" : movement_to_edit.type,
                    "amount" : movement_to_edit.amount,
                    "description" : movement_to_edit.description,
                    "date" : movement_to_edit.date,
                    "categories" : movement_to_edit.category
                }

                edited_data = edit_movement_window(my_manager, data_for_edit_window)

                if edited_data:
                    if my_manager.edit_movement(
                        index_to_edit,
                        edited_data['kind'],
                        edited_data[ 'amount' ],
                        edited_data[ 'description'],
                        edited_data['date'],
                        edited_data['category']
                    ):
                        sg.popup_ok('Movement edited successfully!')
                        update_main_display(window, my_manager)
                    else: 
                        sg.popup_error("Could not edit movement. Please check data(positive amount, valid date/type).")
            else:
                sg.popup_error("Selected movement is no longer valid. Please refresh.")

window.close()