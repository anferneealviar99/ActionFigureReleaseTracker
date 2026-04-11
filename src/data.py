import csv
def save_all_figures(rows):
    
    with open("figures.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("All figures saved!")
    print()
    
def load_all_figures():
    try:
        with open("figures.csv", 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            if not rows:
                rows = [["Name", "Release Date", "Status", "Tier", "Websites"]]        
            return rows
        
    except FileNotFoundError:
        return [["Name", "Release Date", "Status", "Tier", "Websites"]]
        