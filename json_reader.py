import json

def read_json_file(filename):
    """Reads a JSON file and returns the data."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from {filename}.")
        return None
