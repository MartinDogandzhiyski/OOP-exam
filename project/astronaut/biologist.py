from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 70)

    @property
    def oxygen_breathe(self):
        return 5

