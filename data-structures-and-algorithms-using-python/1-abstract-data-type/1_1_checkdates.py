"""
Extracts a collection of birth dates from the user and determines
if each individual is at least 21 years of age.
"""
from datetime import date
import datetime


def main():
    # Date before which a person must have been born to be 21 or older.
    born_before = datetime.date(1988, 6, 1)
    # Extract birth dates from the user and determine if 21 or older.
    date = prompt_and_extract_date()
    while date is not None:
        if date <= born_before:
            print("Is at least 21 years of age: ", date)
        prompt_and_extract_date()


def prompt_and_extract_date():
    """
    Prompts for and extracts the Gregorian date components. Returns a
    Date object or None when the user has finished entering dates.
    """
    print("Enter a birth date.")
    month = int(input("month (0, to quit):"))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return datetime.date(year, month, day)


if __name__ == "__main__":
    main()
