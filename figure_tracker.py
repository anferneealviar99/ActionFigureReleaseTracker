import csv

def show_figures():
    with open("figures.csv", 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        fig_rows = rows[1:]
        
        for row in fig_rows:
            name = row[0]
            print(f"Name: {name}")
            
            release_date = row[1]
            print(f"Release Date: {release_date}")
            
            status = row[2]
            print(f"Status: {status}")
            
            tier = row[3]
            print(f"Tier: {tier}")
            
            website_list = row[4].split(";")
            for website in website_list:
                store, url = website.split(":", 1)
                
                print(f"Store: {store.strip()} ({url.strip()})")
            
            print()
                
            
def add_figure():
    figure_details = {}
    
    name = input("Figure Name: ")
    figure_details["name"] = name
    
    release_date = input("Release Date: ")
    figure_details["release_date"] = release_date
    
    status = input("Status: ")
    figure_details["status"] = status
    
    tier = input("Tier: ")
    figure_details["tier"] = tier
    
    figure_details["websites"] = {}
    
    while True:
        # Allow to enter websites
        print("Enter the store name and URL. Type 'finish' to exit this menu.")
        store_name = input("Store Name: ")
        
        if store_name.lower() == "finish":
            break
        
        if store_name.strip() == "":
            print("Store name cannot be blank.")
            continue
        
        store_url = input("URL: ")
        
        if store_url.strip() == "":
            print("URL cannot be blank")
            continue
            
        figure_details["websites"][store_name] = store_url
    
    websites_str = '; '.join([f"{store}: {url}" for store, url in figure_details["websites"].items()])
    # Read existing data then write everything back to avoid overwrite
    
    try:
        with open("figures.csv", 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        rows = []
        
    # If file is empty or has no header, add header
    if not rows:
        rows = [["Name", "Release Date", "Status", "Tier", "Websites"]]
        
    rows.append([figure_details["name"], figure_details["release_date"], figure_details["status"], figure_details["tier"], websites_str])
    
    with open("figures.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        
    print(f"Added: {figure_details['name']}")
    

def show_menu():
    print("=== ACTION FIGURE RELEASE TRACKER ===")
    print("1. Add a figure")
    print("2. Show all figures")
    print("3. Update figures")
    print("4. Delete figures")
    print("5. Exit")

def main():
    while True:
        show_menu()
        
        choice = input("Please choose an option (1-5): ")
        
        match(int(choice)):
            case 1:
                print("=== ADD A FIGURE ===")
                add_figure()
            case 2:
                print("=== SHOW ALL FIGURES ===")
                print()
                show_figures()
            case 3:
                print("=== UPDATE FIGURES ===")
            case 4:
                print("=== DELETE FIGURES ===")
            case 5:
                print("EXITING PROGRAM")
                break 
            case _:
                print("Invalid option. Please pick between options 1-5.")   
                
        
        

main() 