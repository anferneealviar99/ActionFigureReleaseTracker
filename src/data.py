import csv
def save_all_figures(rows):
    
    with open("figures.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("All figures saved!")
    
def load_all_figures():
    with open("figures.csv", 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    return rows