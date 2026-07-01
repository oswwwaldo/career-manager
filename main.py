import os
from data_models import Book, Textbook, Course, LiveCourse, Exercises, LimitedExercises, MilestoneMarker

#pylint: skip-file

library: dict[str, Book | Textbook | Course | LiveCourse | Exercises | LimitedExercises | MilestoneMarker] = {

    # Newly Sorted Backlog Books
    "Serious Python": Book(chapters=13, category="Technical", technology="Python"),
    "Clean Code: A Handbook of Agile Software Craftsmanship": Book(chapters=37, category="Software Engineering"),
    "Think Like A Programmer": Book(chapters=8, category="Software Engineering"),
    "Building a StoryBrand 2.0: Clarify Your Message So Customers Will Listen": Book(chapters=15, category="Marketing"),
}

# for item in library.values():
#     print(item)
#     if isinstance(item, Book):
#         print(str(item) + " is a book")
#     else:
#         print("3")

for key, value in library.items():
    print(key)

book_names = [key for key in library]

library_keys = library.keys()
# print(library_keys)