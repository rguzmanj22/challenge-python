import csv

def read_csv_file(filename):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
