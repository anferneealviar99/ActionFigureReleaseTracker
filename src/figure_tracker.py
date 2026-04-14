import data, update, date

FIGURE_FIELDS = ["Name", "Release Date", "Status", "Tier", "Stores"]
VALID_STATUSES = ["Leaked", "Announced", "Preorder", "Released", "Sold Out"]
TIERS = ["Preorder ASAP", "Watchlist", "Release Day", "Wait and Watch", "Pass"]

STATUS_MENU = {i+1: name for i, name in enumerate(VALID_STATUSES)}
FIELDS_MENU = {i+1: name for i, name in enumerate(FIGURE_FIELDS)}
TIERS_MENU = {i+1: name for i, name in enumerate(TIERS)}

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
    
def get_release_date(prompt):
    while True:
        release_date = input(prompt)
        
        valid_date = date.validate_date(release_date)
        
        if valid_date:
            return valid_date
        else:
            print("The date you have entered is invalid. Use YYYY-MM-DD, YYYY-MM, or YYYY.")
        
def get_status_from_user():
    for i, status in STATUS_MENU.items():
        print(f"{i}. {status}")
        
    option = get_choice("Please enter your desired status (1-5): ", 1, len(VALID_STATUSES))
        
    return VALID_STATUSES[option-1]

def get_name_from_user():
    new_name = input("What would you like to name this figure? ")
    return new_name

def update_name(rows, option):
    old_name = rows[option][0]
    new_name = get_name_from_user()
    update.set_name(rows, option, new_name)
    
    print(f"Changed {old_name} to {new_name}. Saving...")
    data.save_all_figures(rows)

def update_status(rows, option):
    new_status = get_status_from_user()
    update.set_status(rows, option, new_status)
    
    print(f"Updated {rows[option][0]} status to {new_status}. Saving...")
    data.save_all_figures(rows)
                
def get_tier_from_user():
    for i, tier in TIERS_MENU.items():
        print(f"{i}. {tier}")
        
    choice = get_choice("Please select the tier you want to change this figure to: ", 1, len(TIERS))
    
    return TIERS[choice-1]
        
def update_tier(rows, option):
    """ Updates the tier level of the figure to a different tier 
        Parameters: rows (the data), option (the figure in question)
    """

    new_tier = get_tier_from_user()
    update.set_tier(rows, option, new_tier)
    
    print(f"Updated {rows[option][0]} tier to {new_tier}. Saving...")
    data.save_all_figures(rows)
    
def update_date(rows, option):
    """ 
        Updates the release date of the figure 
        Parameters: rows (the list of figures), option (the chosen figure)
    """
    old_date = date.parse_date(rows[option][1])
    new_date = get_release_date("Please enter the updated release date for this figure (must be YYYY-MM-DD, YYYY-MM, or YYYY): ")
    parsed_new_date = date.parse_date(new_date)
    update.set_date(rows, option, new_date)
    
    print(f"Updated the release date of {rows[option][0]} from {old_date} to {parsed_new_date}.")
    
    data.save_all_figures(rows)
    
    print()
    
def update_stores(rows, option):
    pass

def get_figure(prompt, rows):
    fig_rows = rows[1:]
    total = len(fig_rows)
    
    if total == 0:
        print("No figures detected in the list. Please add a figure.")
        return 0

    while True:
        count = 1
        print(prompt)
        for row in fig_rows:
            print(f"{count}. {row[0]}")
            count += 1
            
        print(f"{count}. Go Back")
        
        option = get_choice("Please enter the number for the figure you want to select: ", 1, total + 1)
        
        return option
    
def delete_figure():
    rows = data.load_all_figures()
    
    option = get_figure(f"Which figure would you like to delete? Please choose between 1 and {len(rows)}", rows)
    
    if option == len(rows) or option == 0:
        return
    
    desired_row_to_delete = rows[option]
    print(f"Deleting {desired_row_to_delete[0]}...")
    
    prev_length = len(rows)
    rows.pop(option)
    curr_length = len(rows)
    
    if curr_length < prev_length:
        print(f"{desired_row_to_delete[0]} has been deleted. Saving...")
        data.save_all_figures(rows)
    else:
        print("Error.")
        

def update_figures():
    rows = data.load_all_figures()
   
    option = get_figure("Which figure would you like to edit? ", rows)
    
    if option == len(rows) or option == 0:
        return
    
    while True:
        print(f"Updating {rows[option][0]}. What field would you like to edit on this figure?")
        
        for i, field in FIELDS_MENU.items():
            print(f"{i}. {field}")
        
        print(f"{len(FIELDS_MENU) + 1}. Go Back")
        
        update = get_choice("Please enter a digit for the field you want to edit: ", 1, len(FIELDS_MENU) + 1)
        
        if update == len(FIELDS_MENU) + 1:
            break
        
        match(update):
            case 1:
                print("== UPDATING NAME ==")
                update_name(rows, int(option))
                break
            case 2:
                print("== UPDATING RELEASE DATE ==")
                update_date(rows, int(option))
                break
            case 3:
                print("== UPDATING STATUS == ")
                update_status(rows, int(option))
            case 4: 
                print("== UPDATING TIER ==")
                update_tier(rows, int(option))
            case 5:
                print("== UPDATING STORES == ")
                break
            case _:
                print("Please enter a valid option.")
                print()
                        
                    

def show_figures():
    rows = data.load_all_figures()
        
    fig_rows = rows[1:]
    
    for row in fig_rows:
        name = row[0]
        print(f"Name: {name}")
        
        release_date = row[1]
        print(f"Release Date: {date.parse_date(release_date)}")
        
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
    
    release_date = get_release_date("Please enter the release date of the figure (must be in YYYY-MM-DD, YYYY-MM or YYYY format):  ")
    figure_details["release_date"] = release_date
    
    status = get_status_from_user()
    figure_details["status"] = status
    
    tier = get_tier_from_user()
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
                    update_figures()
                case 4:
                    print("=== DELETE FIGURE ===")
                    delete_figure()
                case 5:
                    print("EXITING PROGRAM")
                    break 
                case _:
                    print("Invalid option. Please pick between options 1-5.")   
                    print()
                    
main() 