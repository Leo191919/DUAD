import json
import os
from datetime import datetime
from dataclasses import dataclass


DATA_FILE = 'movements.json'

def load_movements(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
                print (f"Warning {filename} content structure is invalid. Starting fresh.")
                return {}
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {filename}. Starting fresh.")
            return {}
    return {}

def save_movements(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving movements: {e}")
        return False
    
class CategoryManager:
    def __init__(self, initial_categories=None):
        if initial_categories is None:
            initial_categories = ['General', 'Food', 'Transport', 'Rent', 'Utilities', 'Others']
        self.categories = sorted(list(set(initial_categories)))

    def add_category(self, category: str):
        category = category.strip()
        if category and category not in self.categories:
            self.categories.append(category)
            self.categories.sort()
            return True
        return False


    def get_categories(self):
        return self.categories
    

    def to_list(self):
        return self.categories

@dataclass
class Movement:
    kind: str
    amount: float
    description: str
    date: str
    category: str

    
    def __post_init__(self):
        if self.kind.lower() not in ['income', 'expense']:
            raise ValueError(f"Invalid movement kind. Valid kind are: 'income' or 'expense', but got '{self.kind}'.")

        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            raise ValueError(f"Amount must be a positive number. Got:{self.amount} ")


        try:
            datetime.strptime(self.date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Got: {self.date}")

        self.kind = self.kind.lower()
        self.amount = float(self.amount)    

        
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
    def __init__(self, filename = DATA_FILE):
        self.category_manager = CategoryManager()
        self.movements = []
        self.filename = filename
        self.load_data()


    def add_movement(self, kind: str, amount: float, description: str, date: str, category: str):

        try:
            if category not in self.category_manager.get_categories():
                raise ValueError(f"Category '{category}' not found in manager.")
            
            new_movement = Movement(kind, amount, description, date, category)
            self.movements.append(new_movement)
            self.movements.sort(key=lambda m:datetime.strptime(m.date, '%Y-%m-%d'),reverse=True)
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


    def edit_movement(self,index: int, kind: str, amount:float, description: str, date: str, category: str):
    
        if not (0<= index < len(self.movements)):
            return False
    
        if category not in self.category_manager.get_categories():
            return False
            
        try:
            updated_movement = Movement(kind, amount, description, date, category)

            self.movements[index] = updated_movement
            self.movements.sort(key=lambda m: datetime.strptime(m.date, '%Y-%m-%d'), reverse=True)
            self.save_data()
            return True
        
        except ValueError as e:
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
        data_to_save ={
            "movements": [mov.to_dict() for mov in self.movements],
            "categories": self.category_manager.to_list()
        }
        save_movements(self.filename, data_to_save)

    def load_data(self):
        loaded_data = load_movements(self.filename)
        self.movements = []

        if isinstance (loaded_data.get('categories'),list):
            self.category_manager = CategoryManager(loaded_data['categories'])

        if isinstance (loaded_data.get('movements'), list):
            for item in loaded_data['movements']:
                try:
                    self.movements.append(
                        Movement(
                            item['kind'],
                            item['amount'],
                            item['description'],
                            item['date'],
                            item['category']
                        )
                    )
                except (ValueError, KeyError) as e:
                    print(f"Skipping invalid movement data during load:{item} - Error {e}")
        self.movements.sort(key=lambda m: datetime.strptime(m.date, '%Y-%m-%d'), reverse=True)


if __name__== "__main__":
    print("--- Initialized test of Finances Managed -- ")

    my_manager = Finance_manager()


    if not my_manager.category_manager.get_categories():
        print("Adding default categories for testing...")
        my_manager.category_manager = CategoryManager (["Job", "Extra", "Test"])

    print(f"Categories loaded: {my_manager.category_manager.get_categories()}")

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