from project.movie_specification.movie import Movie


class Action(Movie):

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def type(self):
        return "Action"

    @property
    def min_age(self):
        return 12