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
            case 2:
                print("=== SHOW ALL FIGURES ===")
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