#Student Class

class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort


    def talk(self):
        return "I can talk!"


    def say_favourite_language(self, fav_language):
        fav_language = "Python"
        #return "I love " + fav_language
        return f"I love {fav_language}"