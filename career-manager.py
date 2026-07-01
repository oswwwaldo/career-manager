""" Old """

#region
# use it with os.startlink()
#Ignoring pylint for now...
#pylint: skip-file
#endregion
import os
import data_models

library: dict[str, Book | Textbook | Course | LiveCourse | Exercises | LimitedExercises | MilestoneMarker] = {

    # Newly Sorted Backlog Books
    "Serious Python": Book(chapters=13, category="Technical", technology="Python"),
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
    
    # Newly Sorted Textbooks
    "A Common-Sense Guide to DSA": Textbook(chapters=20, category="Technical", technology="Data Structures and Algorithms", required_reading=True),

    "Marcy Lab School of Software Engineering Fellowship Starts":MilestoneMarker(type="Academic Milestone", date="September 22nd"),
    "HackerRank 30 Days of Code": Exercises(project_number=30, reoccuring=True, technology="Python"),
    "The Big Book of Small Python Projects": LimitedExercises(chapters=81, category="Technical", technology="Python"),
}

library_keys = library.keys()

def record_input():
    input = int(input())

    print("Reading bookdata...")
    print("What is your goal?")
    user_goal = str(input())
    # possibly output to LLM for processing

    print("How frequent would you like your reading list to be?")
    print("1 - Everyday")
    user_frequency = int(input())

    print("Of your list, how many books do you feel comfortable in tackling daily?")
    user_daily_read_goal = int(input())


def print_schedule(library):
    for item in library:
        pass


library["GAE"] = Course(chapters=69, category="Test",platform="VsCode", has_certificate=False)