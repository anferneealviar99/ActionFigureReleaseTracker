import data

def set_status(rows, option, new_status):
    # Set the new status to the figure
    rows[option][2] = new_status

def set_date(rows, option, new_date):
    rows[option][1] = new_date
    
def set_name(rows, option, new_name):
    rows[option][0] = new_name 

def set_tier(rows, option, new_tier):
    rows[option][3] = new_tier
    