import FreeSimpleGUI as sg
from logic import Finance_manager
from interfaces import(
    add_movement_window,
    edit_movement_window,
    update_main_display
)

my_manager = Finance_manager()


layout = [
    [sg.Button('Add Income', key='-ADD_INCOME_BTN-'),
    sg.Button('Add Expense', key='-ADD_EXPENSE_BTN-'),
    sg.Button('Remove Movement', key='-REMOVE_MOVEMENT_BTN-'),
    sg.Button('Edit Movement', key='-EDIT_MOVEMENT_BTN-')],
    [sg.Table(values = [],
        headings = ['kind', 'Amount', 'Description', 'Date', 'Category'],
        display_row_numbers = False,
        auto_size_columns = True,
        num_rows = 10,
        justification = 'left',
        key = '-MOVEMENTS_TABLE-',
        enable_events = True,
        select_mode = 'browse')],


    [sg.Text('Current Balance:$0.00', key='-BALANCE_TEXT-', font=('Helvetica', 12, 'bold'))],
    [sg.Button('Exit', key = '-EXIT_BTN-')]
]


windows = sg.Window('Manager finances', layout, finalize=True)
update_main_display(windows, my_manager)
while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED or event == '-EXIT_BTN-':
        my_manager.save_data()
        break
    elif event == '-ADD_INCOME_BTN-':
        data_movement= add_movement_window(my_manager, 'income')
        if data_movement:
            if my_manager.add_movement(
                data_movement['kind'],
                data_movement['amount'],
                data_movement['description'],
                data_movement['date'],
                data_movement['category']
            ):
                sg.popup_ok("Income added successfully!")
                update_main_display(windows, my_manager)
            else:
                sg.popup_error("Could not add income. Please check the input data(positive amount, valid date/kind).")

    elif event == '-ADD_EXPENSE_BTN-':
        data_movement = add_movement_window(my_manager, kind ='expense')
        if data_movement:

            if data_movement['amount']<=0:
                sg.popup_error('Amount must be positive number greater than zero')
                continue

            if my_manager.add_movement(
                data_movement['kind'],
                data_movement['amount'],
                data_movement['description'],
                data_movement['date'],
                data_movement['category']
            ):
                sg.popup_ok("Expense added successfully!")
                update_main_display(windows, my_manager)
            else:
                sg.popup_error("Could not add expense. Please check the input data(positive amount, valid date/kind).")

    
    elif event == '-REMOVE_MOVEMENT_BTN-':
        selected_rows_indices = values['-MOVEMENTS_TABLE-']

        if not selected_rows_indices:
            sg.popup('Please select a movement from the table to remove.')
        else: 
            index_to_delete = selected_rows_indices[0]
            confirm = sg.popup_yes_no( f'Are you sure you want to delete the selected movement(row {index_to_delete + 1})?')
            if confirm == 'Yes':
                if my_manager.remove_movement(index_to_delete):
                    sg.popup_ok('Movement removed successfully.')
                    update_main_display(windows, my_manager)
                else:
                    sg.popup_error('Could not delete movement. Invalid index or internal error.')

            else: 
                sg.popup('Deletion canceled.')

    elif event == '-EDIT_MOVEMENT_BTN-':
        selected_rows_indices= values['-MOVEMENTS_TABLE-']
        if not selected_rows_indices:
            sg.popup('Please select a movement from the table to edit.')
        elif len(selected_rows_indices) > 1:
            sg.popup('Please select only one movement to edit.')
        else:
            index_to_edit = selected_rows_indices[0]
            if 0<=index_to_edit < len(my_manager.movements):
                movement_to_edit = my_manager.movements[index_to_edit]

                data_for_edit_window = {
                    'kind': movement_to_edit.kind,
                    'amount': movement_to_edit.amount,
                    'description': movement_to_edit.description,
                    'date': movement_to_edit.date,
                    'category': movement_to_edit.category
                } 
                edited_data = edit_movement_window(my_manager, data_for_edit_window)
                if edited_data:
                    if my_manager.edit_movement(
                        index_to_edit,
                        edited_data['kind'],
                        edited_data['amount'],
                        edited_data['description'],
                        edited_data['date'],
                        edited_data['category']
                    ):
                        sg.popup_ok('Movement edited successfully.')
                        update_main_display(windows, my_manager)
                    else:
                        sg.popup_error('Could not edit movement. Please check the input data(positive amount, valid date/kind).')
            else:
                sg.popup_error('Selected movement is no longer valid. Please refresh.')
                            
windows.close()
