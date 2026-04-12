import regex as re
from datetime import datetime

def get_month(month):
    month_int = int(month)
    
    match(month_int):
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"

def is_real_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
        
def validate_date(release_date):
    """ Accept inputs for the release date only if format matches YYYY-MM-DD, YYYY-MM, or YYYY """
    
    if re.match(r"^\d{4}-\d{2}-\d{2}$", release_date):
        valid_date = release_date
    elif re.match(r"^\d{4}-\d{2}$", release_date):
        valid_date = release_date + "-01" # first day of the month
    elif re.match(r"^\d{4}$", release_date):
        valid_date = release_date + "-12-01" # last month, first day of the month
        
    if is_real_date (valid_date):
        return valid_date
    else:
        return None
    
def parse_date(date_str):
    date_list = date_str.split("-")
    
    year = date_list[0]
    month = get_month(date_list[1])
    day = date_list[2]
    
    parsed_date = " ".join([month, day, year])
    
    return parsed_date
