from datetime import datetime
class User:
    def __init__(self, name, year):
        self.name = name
        self.birthyear = year

    def get_name(self):
        return self.name.capitalize()

    def get_age(self, current_year):
        return current_year - self.birthyear

    