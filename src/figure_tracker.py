import data, update
FIGURE_FIELDS = ["Name", "Release Date", "Status", "Tier", "Stores"]
VALID_STATUSES = ["Leaked", "Announced", "Preorder", "Released", "Sold Out"]
STATUS_MENU = {i+1: name for i, name in enumerate(VALID_STATUSES)}
FIELDS_MENU = {i+1: name for i, name in enumerate(FIGURE_FIELDS)}

def get_choice(prompt, min_val, max_val):
    while True:
        choice = input(prompt)
        
        if not choice.isdigit():
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue
        
        num = int(choice)
        
        if num < min_val or num > max_val:
            print(f"Choice must be between {min_val} and {max_val}.")
            continue
            
        return num
        
def get_status_from_user():
    for i, status in STATUS_MENU.items():
        print(f"{i}. {status}")
        
    option = get_choice("Please enter your desired status (1-5): ", 1, len(VALID_STATUSES))
        
    return VALID_STATUSES[option-1]

def update_status(rows, option):
    new_status = get_status_from_user()
    new_rows = update.set_status(rows, option, new_status)
    
    print(f"Updated {rows[option][0]} status to {new_status}. Saving...")
    data.save_all_figures(new_rows)
                
def show_tier_menu():
    pass

def update_figures():
    rows = data.load_all_figures()
        
    fig_rows = rows[1:]
    
    count = 1
    total = len(fig_rows)
    
    print("Which figure would you like to edit?")
    while True:
        for row in fig_rows:
            print(f"{count}. {row[0]}")
            count += 1
        
        print(f"{count}. Go Back")
        option = get_choice("Please enter the number for the desired figure you want to update: ", 1, len(fig_rows) + 1)

        if option == len(fig_rows) + 1:
            break
        
        figure = fig_rows[option-1] 
    
        while True:
            print(f"Updating {figure[0]}. What field would you like to edit on this figure?")
            
            for i, field in FIELDS_MENU.items():
                print(f"{i}. {field}")
            
            print(f"{len(FIELDS_MENU) + 1}. Go Back")
            
            update = get_choice("Please enter a digit for the field you want to edit: ", 1, len(FIELDS_MENU) + 1)
            
            if update == len(FIELDS_MENU) + 1:
                break
            
            match(update):
                case 1:
                    break
                case 2:
                    break
                case 3:
                    print("== UPDATING STATUS == ")
                    update_status(rows, int(option))
                case 4: 
                    break
                case 5:
                    print("== UPDATING STORES == ")
                    break
                case 6:
                    break
                case _:
                    print("Please enter a valid option.")
                    print()
        count = 1
                        
                    

def show_figures():
    rows = data.load_all_figures()
        
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
        name = input("Figure Name (Enter 0 to cancel): ")
        if name == "":
            print("Please enter a valid name.")
        else:
            figure_details["name"] = name
            break
    
    release_date = input("Release Date: ")
    figure_details["release_date"] = release_date
    
    status = get_status_from_user()
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
    
    rows = data.load_all_figures()
        
    rows.append([figure_details["name"], figure_details["release_date"], figure_details["status"], figure_details["tier"], websites_str])
    
    data.save_all_figures(rows)
        
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