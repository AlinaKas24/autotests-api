from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Users"
    FILES = "Filed"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"
