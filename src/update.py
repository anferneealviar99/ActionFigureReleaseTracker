import data

def set_status(rows, option, new_status):
    # Set the new status to the figure
    new_rows = rows.copy()
    new_rows[option][2] = new_status
    
    return new_rows

def set_name(rows, option, new_name):
    new_rows = rows.copy()
    new_rows[option][0] = new_name 
    
    return new_rows