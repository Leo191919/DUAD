import FreeSimpleGUI as sg
from datetime import datetime
from logic import Finance_manager


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


def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

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
        sg.CalendarButton("Choose Date", target = "-DATE_INPUT-", format = "%Y-%m-%d")],

        [sg.Text("Category")],
        [sg.Combo(manager.category_manager.get_categories(), key = "-CATEGORY_INPUT-", readonly = True)],
        [sg.Button("Manage Categories", key = "-MANAGE_CATEGORIES_BTN-")],
        [sg.Button("Add", key = "-ADD_MOVEMENT_BTN-"), sg.Button("Cancel", key ="-CANCEL_BTN-")],
        ]

    emergent_window = sg.Window("Add New Movement", layout_add_movement)

    while True:
        event_emergent, values_emergent = emergent_window.read()

        if event_emergent == sg.WIN_CLOSED or event_emergent == "-CANCEL_BTN-":
            break
        
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

            if not is_valid_date_format(date):
                sg.popup_error("Invalid date format. Use YYYY-MM-DD.")
                continue
    
            try: 
                amount_movement = float(values_emergent['-AMOUNT_INPUT-'])
            except ValueError:
                sg.popup_error("Please enter a valid amount.")
                continue

            kind_movement = "income" if values_emergent['-KIND_INCOME-'] else "expense"            

            data_movement = { 
                "kind": kind_movement,
                "amount": amount_movement,
                "description": description,
                "date": date,
                "category": category,
            }
            emergent_window.close()
            return data_movement
    
    emergent_window.close()
    return None
        


def edit_movement_window(manager,movement_data):
    is_income = movement_data['kind'].lower() == 'income'
    is_expense = movement_data['kind'].lower() == 'expense'
    
    edited_data = None

    layout_edit_movement= [
        [sg.Text("Kind movement(Income/Expense):")],
        [sg.Radio("Income", "RADIO1", default = is_income, key = '-KIND_INCOME-' )],
        [sg.Radio("Expense", "RADIO1", default= is_expense, key = '-KIND_EXPENSE-' )],

        [sg.Text("Amount:")],
        [sg.Input(default_text= f"{movement_data['amount']}", key= '-AMOUNT_INPUT-')],

        [sg.Text("Description:")],
        [sg.Input(default_text=movement_data['description'], key= '-DESCRIPTION_INPUT-' )],

        [sg.Text("Date (YYYY-MM-DD):")],
        [sg.Input(default_text=movement_data['date'], key = '-DATE_INPUT-', size=(12,1), disabled = True),
        sg.CalendarButton("Choose Date", target = "-DATE_INPUT-", format ="%Y-%m-%d")],
        
        [sg.Text("Category")],
        [sg.Combo(manager.category_manager.get_categories(), key = "-CATEGORY_INPUT-", readonly =  True,
                default_value= movement_data['category'] )],

        [sg.Button("Manage Categories", key = '-MANAGE_CATEGORIES_BTN-')],
        [sg.Button("Save Changes", key = '-SAVE_CHANGES_BTN-'), sg.Button( "Cancel", key = '-CANCEL_BTN-' )]
    ]

    emergent_window = sg.Window("Edit Movement", layout_edit_movement)

    
    while True:
        event_emergent, values_emergent = emergent_window.read()


        if event_emergent == sg.WIN_CLOSED or event_emergent == '-CANCEL_BTN-':
            break

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

            date = values_emergent['-DATE_INPUT-'].strip()

            if not is_valid_date_format(date):
                sg.popup_error("Invalid date format. Use YYYY-MM-DD.")
                continue

            edited_data = {
                "kind": kind_movement,
                "amount": amount_movement, 
                "description": values_emergent['-DESCRIPTION_INPUT-'],
                "date" : values_emergent['-DATE_INPUT-'],
                "category" : values_emergent['-CATEGORY_INPUT-']
                            
            }
            break

    emergent_window.close()
    return edited_data
        

def get_movements_for_table(manager):
    table_data = [] 
    for mov in manager.movements: 
        table_data.append([
            mov.kind.capitalize(),
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
