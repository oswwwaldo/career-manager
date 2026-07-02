import os, sys
from data_models import Model, Book, Textbook, Course, LiveCourse, Exercises, LimitedExercises, MilestoneMarker
from datetime import date, datetime
import calendar 

#region
# 2026:
#     january
#     feburary
#     march
#     april   
#     may
#     june
#         past data
#     julyweek 
#         current month
#             week 1
#                 month starts wednesday
#                 week actually started sunday (28th)
#                     sunday
#                     monday
#                     tuesday
#                     wedsneday
#                     thursday
#                     friday
#                     saturday
#             week 2
#             week 3
#             week 4
#             week 5
#                 month ends friday
#                 week actually ended saturday (1st)
#     august
#         future month
#     september
#     october
#     november
#     december
#endregion
#pylint: skip-file

for i in range (0, 20):
    print()

library: dict[str, Book | Textbook | Course | LiveCourse | Exercises | LimitedExercises | MilestoneMarker] = {
    "Serious Python": Book(chapters=13, category="Technical", technology="Python", frequency_offset=1),
    "Clean Code: A Handbook of Agile Software Craftsmanship": Book(chapters=37, category="Software Engineering"),
    "Think Like A Programmer": Book(chapters=8, category="Software Engineering"),
    "Python Crash Course: A Hands-On, Project-Based Introduction to Programming": Book(chapters=1, category="Technical", technology="Python"),
    "The Pragmatic Programmer": Book(chapters=53, category="Software Engineering"),
    "Building a StoryBrand 2.0: Clarify Your Message So Customers Will Listen": Book(chapters=15, category="Marketing"),
    "How To Win Friends & Influence People": Book(chapters=9, category="Psychology"),
    "Living with Limerence": Book(chapters=19, category="Psychology"),
    "A Philosophy of Software Design": Book(chapters=14, category="Software Design", technology="Software Engineering"),
    "Code: The Hidden Language of Hardware and Software": Book(chapters=21, category="Technical", technology="Computer Science Fundamentals"),
    "Eloquent JavaScript": Book(chapters=22, category="Technical", technology="JavaScript"),
    
    "A Common-Sense Guide to Data Structures and Algorithms": Textbook(chapters=20, category="Technical", technology="Data Structures and Algorithms", required_reading=True),

    "Marcy Lab School of Software Engineering Fellowship Starts":MilestoneMarker(type="Academic Milestone", date="September 22nd"),
}

target_list = {} 
reading_lists = {} 

now = datetime.now()
year, month, day = now.year, now.month, now.day
user_prefers_sunday = True

sunday_calendar = calendar.Calendar(firstweekday=calendar.SUNDAY)
monday_calendar = calendar.Calendar(firstweekday=calendar.MONDAY)

selected_reading_list = None

if user_prefers_sunday:
    month_matrix = sunday_calendar.monthdayscalendar(year, month) 
else:
    month_matrix = monday_calendar.monthdayscalendar(year, month)

week_of_month = 0
for index, week in enumerate(month_matrix):
    if day in week:
        week_of_month = index + 1 
        break

def record_user_input():
    print("Use (0-9) to navigate the menu")
    user_input = None

    while user_input is None:
        raw = input("Enter in your number: ").strip()

        try:
            user_input = int(raw)

            if user_input > 10 or user_input <= -1:
                print("Invalid number range, please use 0-9 to navigate the menu")
                user_input = None
            else:
                print("...")
                return user_input

        except ValueError:
            if raw.startswith("python -u"):
                print("\033[96m\nVS Code injected a run command. Exiting cleanly...\033[0m")
                sys.exit(0)
            print("Invalid input, please enter in a number.")

def load_library():
    month_name = calendar.month_name[month]

    # Hardcoding these for testing for now
    reading_lists[(year, 'June')] = {}

    if (year, month_name) in reading_lists:
        print("Current month reading list already exists.")
    else:
        reading_lists[(year, month_name)] = {} 

    reading_lists[(year, 'August')] = {}
    reading_lists[(year, 'September')] = {}

    print(f"\nLoad list:")
    for i, lst in enumerate(reading_lists.keys()):
        print(f"{i:02d}. — [{lst}]")

    choice = record_user_input()
    if choice == 1:
        for i, (key, value) in enumerate(library.items()):
            if i >= 5:
                break
            reading_lists[(year, month_name)][key] = value

    keys = list(reading_lists.keys())
    selected_list = keys[choice]
    selected_reading_list = reading_lists[selected_list]
    print(f"Selected: {selected_reading_list}")
    print(selected_reading_list.items())
    return selected_reading_list

def load_calendar(selected_reading_list):
    flattened_month_matrix = [day for week in month_matrix for day in week if day > 0]
    
    if selected_reading_list is None:
        print(str(flattened_month_matrix))
        return "Load a reading list first."

    print(f"Determining reading list...")
    print(f"Selected: {selected_reading_list}")


    for i in range(day, len(flattened_month_matrix)):
        print("July " + str(i))

        for index, (key, value) in enumerate(selected_reading_list.items(), start = 1):
            if value.frequency_offset:
                print(f" — {key} Chapter {value.current_chapter + i}")
                # value.chapters


    print(flattened_month_matrix)
    pass

def schedule_an_item():
    pass


# User -> Books -> creates List -> Schedules list over intervals
# User can update books, delete, remove and ultimately modify said list and schedule
def menu():
    while True:
        print()
        print("Welcome to Career Manager")
        print(f"Today is day {day} of {calendar.month_name[month]}, {year}.")
        print(f"00. — [Continue execution]")
        print(f"01. — [Load list]")                          # Load a reading list
        print(f"02. — [Load calendar and schedule]")         # Create calendar object and schedule
        print(f"03. — [Add a book/item]")                    # Create an item and add to library
        print(f"04. — [Remove a book/item]")                 # Remove an item from library
        print(f"05. — [Start]")                              # Create a list of books, courses and material you'd like to read
        print(f"09. — [Exit program]")
        print()

        choice = record_user_input()

        match choice:
            case 1:
                selected_reading_list = load_library()
            case 2:
                load_calendar(selected_reading_list)
            case 3:
                schedule_an_item()
            case 4:
                pass
            case 9:
                sys.exit(0)
            case _:
                print("Out of range, try again.")

menu()