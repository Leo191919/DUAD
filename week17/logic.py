import datetime
from category_manager import CategoryManager
from movement_persistence import save_movements, load_movements


class Movement:
    def __init__(self, kind, amount, description, date, category):
        if kind.lower() not in ['income', 'expense']:
            raise ValueError(f"Invalid movement kind. Valid kind are: 'income' or 'expense', but got '{kind}'.")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError(f"Amount must be a positive number. Got:{amount} ")


        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Got: {date}")

        self.kind = kind.lower()
        self.amount = float(amount)
        self.description = description
        self.date = date
        self.category = category
        
        
    def get_details(self):
        return f"kind:{self.kind.capitalize()}, Amount:{self.amount:.2f}, Description: {self.description}, Date: {self.date}, Category: {self.category}"
    
    def __str__(self):
        return self.get_details()
    
    
    def to_dict(self):
        return{
            "kind": self.kind,
            "amount": self.amount,
            "description" : self.description,
            "date": self.date,
            "category": self.category 
        }
    
    
class Finance_manager:
    def __init__(self, filename = 'movements.json'):
        self.category_manager = CategoryManager()
        self.movements = []
        self.filename = filename
        self.load_data()


    def add_movement(self, kind_param, amount_param, description_param, date_param, category_param):

        try:
            new_movement = Movement(kind_param, amount_param, description_param, date_param, category_param)

            if category_param not in self.category_manager.get_categories():
                raise ValueError('Category not found in manager.')
                
            self.movements.append(new_movement)
            self.save_data()
            return True

        except ValueError as e:
            print(f"Error adding movement: {e}")
            return False 
        

    def remove_movement(self, index_to_remove):
        if 0<= index_to_remove< len(self.movements):
            del self.movements[index_to_remove]
            self.save_data()
            return True
        return False        


    def edit_movement(self,index, kind_param, amount_param, description_param, date_param, category_param):
        print(f"Editing movement at index: {index}")
        print(f"New data: kind = {kind_param}, amount = {amount_param}, description = {description_param}, date = {date_param}, category = {category_param}")   
        
        if category_param not in self.category_manager.get_categories():
            print(f"Error: Category not found")
            return False
        
        if 0 <= index < len(self.movements):
            try:
                update_movement = Movement(kind_param, amount_param, description_param,date_param, category_param)
                self.movements[index] = update_movement 
                self.save_data()
                return True
            except ValueError as e :
                print(f"Error editing movement: {e}")
                return False
        return False
    

    def calculate_total_balance(self):

        total_balance = 0
        for mov in self.movements:
            if mov.kind == "income":
                total_balance += mov.amount
            elif mov.kind == "expense":
                total_balance -= mov.amount
        return total_balance

    
    def save_data(self):
        data_to_save = [mov.to_dict() for mov in self.movements]
        save_movements(self.filename, data_to_save)


    def load_data(self):
        loaded_data = load_movements(self.filename)
        self.movements = []
        for item in loaded_data:
            try: 
                self.movements.append(Movement(
                item['kind'],
                item['amount'],
                item['description'],
                item['date'],
                item['category']
                ))
            except (ValueError, KeyError) as e :
                print(f"Skipping invalid movement data during load:{item} - Error {e}")   

my_manager = Finance_manager()

if __name__== "__main__":
    print("--- Initialized test of Finances Managed -- ")

    my_manager = Finance_manager()
    print("\nTry to add a movement with positive amount")

    my_manager.add_movement("income", 100, "Salary", "2025-10-01", "Job")
    my_manager.add_movement("income", 50, "Groceries", "2025-10-02", "Extra")



    print("\nTry to add a movement with negative amount")

    my_manager.add_movement("expense", 30.50, "Salary", "2025-10-01", "Job")
    my_manager.add_movement("expense", 75.00, "Groceries", "2025-10-02", "Extra")

    print("\n Try to add a movement with invalid amount")
    my_manager.add_movement("expense", -10, "Salary", "2025-10-01", "Job")
    my_manager.add_movement("expense", 0, "Groceries", "2025-10-02", "Extra")

    print("\nTry to add a movement with invalid amount(negative/zero)")
    my_manager.add_movement("expense", -10, "Invalid Amount test", "2025-10-01", "test" ) 
    my_manager.add_movement("expense", 0, "zero Amount Test", "2025/10/04", "Test")


    print(f"\nNumber total of movements registered: {len(my_manager.movements)}")

    print("\nDetails of movements registered:")
    for mov in my_manager.movements:
        print(mov.get_details())

    total_balance = my_manager.calculate_total_balance()
    print(f"\nTotal balance: {total_balance:.2f}")

    if len(my_manager.movements)> 0 : 
        print (f"\nRemoving movement at index 0:{my_manager.movements[0].get_details()}")
        if my_manager.remove_movement (0):
            print("Movement removed successfully!")
        else: 
            print("Failed to removed movement.")
    else: 
        print("\nNo movement to remove.")

    print (f"\nTotal number of movements after removal:{len (my_manager.movements)}")
    print(f"New total balance: {my_manager.calculate_total_balance():.2f}")



    print("\n--- End of test ---")