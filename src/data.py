import csv
def save_all_figures(rows):
    """
        Saves all current rows, including header, to a CSV file
        
        Args: rows - a list of all rows in the CSV 
    """
    with open("figures.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("All figures saved!")
    print()
    
def load_all_figures():
    """ 
        Tries to load all the rows, including the header, into the CSV file
        If there is no CSV file detected, it will return the header row, otherwise it will return all rows
    """
    try:
        with open("figures.csv", 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            if not rows:
                rows = [["Name", "Release Date", "Status", "Tier", "Websites"]]        
            return rows
        
    except FileNotFoundError:
        return [["Name", "Release Date", "Status", "Tier", "Websites"]]
        