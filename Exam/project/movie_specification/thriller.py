from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)


    @property
    def type(self):
        return 'Thriller'

    @property
    def min_age(self):
        return 16
