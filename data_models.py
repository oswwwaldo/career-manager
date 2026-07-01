""" Dataclasses only (Book, Course, MilestoneMarker, etc.) """
#pylint: skip-file


from dataclasses import dataclass
from enum import Enum, unique
from typing import Optional

@dataclass
class Book:
    """Represents a book or any piece of literature"""
    chapters: int
    category: str
    technology: Optional[str] = None
    uri_link: Optional[str] = None

@dataclass
class Textbook(Book):
    """Required readings will have deadline restrictions and higher priorities placed on them"""
    required_reading: Optional[bool] = False

@dataclass
class Course:
    """Can be a series of videos or a structured async course, i.e Odin Project or CompTIA"""
    chapters: int
    category: str
    platform: str
    has_certificate: bool
    technology: Optional[str] = None
    uri_link: Optional[str] = None

@dataclass(kw_only=True) # allows mixing optional and required parameters around, useful for inheritance—keep in mind you can't declare an object using positional arguments anymore
class LiveCourse(Course):
    """A structured sync course, i.e TIP 101 or MAT 301"""
    credit_hours: int
    lecture_frequency: str # class Schedule =>> Tuesdays 7pm-9pm, Thursdays 7pm-9pm
    labs_frequency: str # Wednesdays 7pm - 9pm
    assignment_frequency: str

@dataclass
class Exercises:
    """A series of challenges, i.e JS30, HackerRank etc."""
    kind: str
    technology: Optional[str] = None
    uri_link: Optional[str] = None

@dataclass
class LimitedExercises(Exercises):
    number_of_exercises: int

@dataclass
class MilestoneMarker:
    """Marks when something critical happens, like the Summer semester ends"""
    type: str
    date: str

@unique
@dataclass
class Schedule(Enum):
    """Raise a "ValueError: duplicate values found" if there's a schedule conflict"""
    ...

class Calendar:
    """Holds days, weeks, months and years"""

class CalendarView:
    """The GUI object of Calendar, representing a limited 30 day view"""

class User:
    ...
