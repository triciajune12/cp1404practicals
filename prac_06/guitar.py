CURRENT_YEAR = 2023
VINTAGE_CLASSIFICATION = 50
# GUITAR_AGE =


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """A guitar class that stores name, year and cost of a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """A string that returns the guitar details"""
        return f"{self.name}, ({self.year}) : {self.cost}"

    def get_age(self):
        """A function to work out the age of the guitar using the CURRENT_YEAR"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """A function to work out if the guitar is vintage from the get_age"""
        return self.get_age() >= VINTAGE_CLASSIFICATION


