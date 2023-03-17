import csv
from datetime import datetime

BIRTHDAY = datetime.strptime("1993-04-10", "%Y-%m-%d")

def calculate_age(birthday, race_date):
    age = race_date.year - birthday.year - ((race_date.month, race_date.day) < (birthday.month, birthday.day))
    return age

def main():
    print("Enter the race details:")
    distance = input("Distance: ")
    time = input("Time: ")
    race = input("Race: ")
    venue = input("Venue: ")
    city = input("City: ")
    date_str = input("Date (MM/DD/YYYY): ")

    date = datetime.strptime(date_str, "%m/%d/%Y")
    age = calculate_age(BIRTHDAY, date)

    new_row = [distance, time, race, venue, f'"{city}"', f"{date.month}/{date.day}/{date.year}", age]

    with open("raceresults.csv", "r") as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    data.insert(1, new_row)

    with open("raceresults.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("The CSV file has been updated successfully.")

if __name__ == "__main__":
    main()