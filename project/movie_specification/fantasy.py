from project.movie_specification.movie import Movie


class Fantasy(Movie):

    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def type(self):
        return 'Fantasy'

    @property
    def min_age(self):
        return 6