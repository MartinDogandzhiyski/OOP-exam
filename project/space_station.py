from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    @staticmethod
    def create_astronaut_by_type(astronaut_type, name):
        astronaut_dict = {"Meteorologist": Meteorologist,
                          "Geodesist": Geodesist,
                          "Biologist": Biologist}
        if astronaut_type in astronaut_dict:
            astronaut = astronaut_dict[astronaut_type](name)
            return astronaut
        return False

    def find_astr_by_name(self, name):
        for astr in self.astronaut_repository.astronauts:
            if astr.name == name:
                return astr
        return False

    def add_astronaut(self, astronaut_type, name):
        if not self.create_astronaut_by_type(astronaut_type, name):
            raise Exception("Astronaut type is not valid!")
        astronaut = self.create_astronaut_by_type(astronaut_type, name)
        if astronaut in self.astronaut_repository.astronauts:
            return f"{name} is already added."
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        for pl in self.planet_repository.planets:
            if pl.name == name:
                return f"{name} is already added."
        planet = Planet(name)
        planet.items = [x for x in items.split(', ')]
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.find_astr_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astr in self.astronaut_repository.astronauts:
            astr.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        for pl in self.planet_repository.planets:
            if pl.name == planet_name:
                sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
                best_astronauts = [x for x in sorted_astronauts if x.oxygen > 30][:5]

                if not best_astronauts or not sorted_astronauts:
                    raise Exception("You need at least one astronaut to explore the planet!")
                mission = False
                astronauts_on_mission = 1
                while best_astronauts:
                    astronaut = best_astronauts[0]
                    astronaut.breathe()
                    if astronaut.oxygen < 0:
                        astronaut.oxygen = 0
                        astronauts_on_mission += 1
                        best_astronauts.remove(astronaut)
                        continue
                    astronaut.backpack.append(pl.items.pop())
                    if not pl.items:
                        mission = True
                        SpaceStation.successful_missions += 1
                        break
                if mission:
                    return f"Planet: {planet_name} was explored. {astronauts_on_mission} astronauts participated in collecting items."
                else:
                    SpaceStation.unsuccessful_missions += 1
                    return "Mission is not completed."
        raise Exception("Invalid planet name!")

    def report(self):
        result = f"{SpaceStation.successful_missions} successful missions!\n"
        result += f"{SpaceStation.unsuccessful_missions} missions were not completed!\n"
        result += f"Astronauts' info:\n"
        for astr in self.astronaut_repository.astronauts:
            result += f"Name: {astr.name}\n"
            result += f"Oxygen: {astr.oxygen}\n"
            if astr.backpack:
                result += f"Backpack items: {', '.join(astr.backpack)}\n"
            else:
                result += f"Backpack items: none\n"
        return result.strip()






