import csv

def update_figures():
    with open("figures.csv", 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        fig_rows = rows[1:]
        
        count = 1
        total = len(fig_rows)
        print("Which figure would you like to edit?")
        while True:
            for row in fig_rows:
                print(f"{count}. {row[0]}")
                count += 1
            
            print("0. Go Back")
            count = 1
            option = input(f"Pick a number between 1 and {total}, or press 0 to go back.")
            
            if option.isdigit() is False:
                print("Please pick a number.")
                print()
            
            elif int(option) == 0:
                break
            
            elif int(option) > total:
                print("Please pick a valid option.")
                print()
                
            else: 
                break

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
            
            if row[4] != "":
                website_list = row[4].split(";")
                for website in website_list:
                    store, url = website.split(":", 1)
                    
                    print(f"Store: {store.strip()} ({url.strip()})")
                
            print()
                
            
def add_figure():
    figure_details = {}
    
    while True:
        name = input("Figure Name: ")
        if name == "":
            print("Please enter a valid name.")
        else:
            break
    
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
        
        if choice.isdigit() is False:
            print("Please choose a valid option.")
            print()
            
        else:
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
                    update_figures()
                case 4:
                    print("=== DELETE FIGURES ===")
                case 5:
                    print("EXITING PROGRAM")
                    break 
                case _:
                    print("Invalid option. Please pick between options 1-5.")   
                    print()
                    
        
main() 