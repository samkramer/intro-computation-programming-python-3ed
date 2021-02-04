# 7.2 Using Predefined Packages
import calendar as cal
import datetime

# Code from page 141
def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    
    # Check for Thursday in first week
    #   Note: if day does *not* occur in month,
    #   corresponding element in list will be 0
    if month[0][cal.THURSDAY] != 0:
        # Fourth Thursday occurs in fourth week
        thanksgiving = month[3][cal.THURSDAY]
    else:
        # Fourth Thursday occurs in fifth week
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


# Finger exercise: write a function that meets the specification
def shopping_days(year):
    """
    year a number >= 1941
    returns the number of days between U.S. Thanksgiving and
        Christmas in year
    """
    assert year >= 1941
    thanksgiving_day = find_thanksgiving(year)
    thanksgiving = datetime.date(year, 11, thanksgiving_day)
    christmas = datetime.date(year, 12, 25)
    return (christmas - thanksgiving).days
    

if __name__ == "__main__":
    my_cal = cal.TextCalendar()
    print(my_cal.formatmonth(2021, 2))  # February 2021

    # Day of week Christmas will fall in 2020
    # - cal.weekday: returns an integer representing day of week
    # - cal.day_name: list of days of the week in English
    print(f"Christmas Day in 2020: {cal.day_name[cal.weekday(2020, 12, 25)]}")
    
    print()

    # Test find_thanksgiving
    print('In 2011', 'U.S. Thanksgiving was on November',
          find_thanksgiving(2011))
    
    print()
    
    # Test shopping_days
    # 2020: 29 days
    year = 2020
    num_days = shopping_days(year)
    print(f"In {year} number of days between Thanksgiving "
          f"and Christmas is {num_days}")