import json 


def save_movements(filename, movements):
    try:
        with open (filename, 'w') as f:
            json.dump(movements, f, indent = 4)

    except IOError as e:
        print(f"Error saving movements to {filename} : {e}")

def load_movements(filename):
    try: 
        with open (filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No existing movements file '{filename}' found, starting with empty movements")
        return []
    except json.JSONDecodeError as e:
        print(f"Error reading JSON from '{filename}': {e}. File might be corrupted.")
        return []
    except IOError as e:
        print(f"Error loading movements from {filename}: {e}")
        return []
    
