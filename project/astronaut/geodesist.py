from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name):
        super().__init__(name, 50)

    @property
    def oxygen_breathe(self):
        return 10