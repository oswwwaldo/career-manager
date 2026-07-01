import os
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

july_2026_reading_list = {}
for i, (key, value) in enumerate(library.items()):
    if i >= 5:
        break
    july_2026_reading_list[key] = value


now = datetime.now()
year, month, day = now.year, now.month, now.day
user_prefers_sunday = True

sunday_calendar = calendar.Calendar(firstweekday=calendar.SUNDAY)
monday_calendar = calendar.Calendar(firstweekday=calendar.MONDAY)

if user_prefers_sunday:
    month_matrix = sunday_calendar.monthdayscalendar(year, month) 
else:
    month_matrix = monday_calendar.monthdayscalendar(year, month)

week_of_month = 0
for index, week in enumerate(month_matrix):
    if day in week:
        week_of_month = index + 1 
        break

print(f"Today is day {day} of {calendar.month_name[month]}, {year}.")
print(f"It falls in week {week_of_month} of the month.")    
print(f"Current month matrix: {month_matrix}")

print()
print("Welcome to Career Manager")
print(f"— 01. [Load list]")
print(f"— 02. [Load calendar]")
print(f"— 03. [Schedule an item]")

print("Use (0-9) to navigate the menu")

user_input = None

while (user_input == None):
    user_input = int(input())
    if user_input > 10 | user_input < 0:
        print("Invalid number range, please use 0-9 to navigate the menu")
        user_input = None
    else:
        print("...")
        break


print("Determining reading list...")

flattened_month_matrix = [day for week in month_matrix for day in week if day > 0]

for i in range(day, len(flattened_month_matrix)):
    print("July " + str(i))

    for index, (key, value) in enumerate(july_2026_reading_list.items(), start = 1):
        if value.frequency_offset:
            print(f" — {key} Chapter {i}")
            # value.chapters


print(flattened_month_matrix)
# for i in range(0, len(month_matrix)):
#     if i > 0:
#         print(i)



# days_in_feb_leap = calendar.monthrange(2028, 2)[1]  # Returns 29
# days_in_feb_reg = calendar.monthrange(2027, 2)[1]   # Returns 28
# days_in_october = calendar.monthrange(2026, 10)[1]  # Returns 31

# calendar = calendar.fromkeys(months_of_the_year) # sets everything to none

# we have to add days, and weeks to each month
# July = {
#     "Week_1": #28th, 29th, 30th ["1st", "2nd", "3rd", "4th"]
#     "Week_2": ["5th, "6th", "7th", "8th", "9th", "10th", "11th"]
#     "Week_3": ["12th", "13th", "14th", "15th", "16th", "17th", "18th"]
#     "Week_4": ["19th", "20th", "21st", "22nd", "23rd", "24th", "25th"]
#     "Week_5": ["26th, "27th", "28th", "29th", "30th", "31st"] # 1st
# }

# for week in July.keys():


# June 1st = {
#     "Serious Python"  — "Chapter 5" — link to original object instance
#     "Serious Python"  — "Chapter 5" — link to original object instance
#     "Serious Python"  — "Chapter 5" — link to original object instance
# }

# a function would populate everyday
# a function would have a subtract the target_chapter from the book object depending on the day's dictionary

# Year (dict) -> Month (dict) -> Week (dict) -> Day (dict) -> Reading List

# assume user chooses current month
# calendar["July"] = 

# for key, value in library.items():
#     print(key)

#     if isinstance(value, Book):
#         print(str(key) + " is a book.")

# book_names = [key for key in library]

# library_keys = library.keys()

# print(date.today().strftime("%m/%d/%Y"))

# loggedIn = True

# def print_ui():
#     if (loggedIn):
#         print("Today is " + date.today().strftime("%m/%d/%Y"))
#         print("\nYou have...")
        
#         for key, value in todays's date_dict:
#             print(f"—{key} Chapter {value.chapters}")

# print_ui()