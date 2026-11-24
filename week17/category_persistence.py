import json 


def save_categories(filename, categories):
    try:
        with open(filename, 'w') as f:
            json.dump(categories, f, indent = 4)

    except IOError as e:
        print(f"Error saving categories to {filename}: {e}")

def load_categories(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No existing categories file '{filename}' found. Starting with default categories.")
        return ["Food", "Transport", "Entertainment", "Other"]
    except json.JSONDecodeError as e:
        print(f"Error reading JSON from {filename}: {e}. File might be corrupted. Using default categories.")
        return ["Food", "Transport", "Entertainment", "Other"]
    
    except IOError as e:
        print(f"Error loading categories from {filename}: {e}. Using default categories.")
        return ["Food", "Transport", "Entertainment", "Other"]
