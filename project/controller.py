from project1.car.car import Car
from project1.car.muscle_car import MuscleCar
from project1.car.sports_car import SportsCar
from project1.driver import Driver
from project1.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if car_type == 'MuscleCar' or car_type == 'SportsCar':
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")
            if car_type == 'MuscleCar':
                new_car = MuscleCar(model, speed_limit)
                self.cars.append(new_car)
            elif car_type == 'SportsCar':
                new_car = SportsCar(model, speed_limit)
                self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    @staticmethod
    def check_if_car_exists(cars, car_type):
        for car in reversed(cars):
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    return car

    @staticmethod
    def check_if_driver_exists(drivers, driver_name):
        for driver in drivers:
            if driver.name == driver_name:
                return driver

    def add_car_to_driver(self, driver_name, car_type):
        current_car = self.check_if_car_exists(self.cars, car_type)
        current_driver = self.check_if_driver_exists(self.drivers, driver_name)
        if current_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if current_car is None:
            raise Exception(f"Car {car_type} could not be found!")
        if current_driver.car:
            old_model = ''
            for car in self.cars:
                if car == current_car:
                    car.is_taken = True
                if car == current_driver.car:
                    car.is_taken = False
                    old_model = car.model
            current_driver.car = current_car
            return f"Driver {driver_name} changed his car from {old_model} to {current_car.model}."
        for car in self.cars:
            if car == current_car:
                car.is_taken = True
                for driver in self.drivers:
                    if driver == current_driver:
                        driver.car = current_car
                        return f"Driver {driver_name} chose the car {current_car.model}."

    @staticmethod
    def check_if_race_exists(races, race_name):
        for race in races:
            if race.name == race_name:
                return race


    def add_driver_to_race(self, race_name, driver_name):
        current_race = self.check_if_race_exists(self.races, race_name)
        current_driver = self.check_if_driver_exists(self.drivers, driver_name)
        if current_race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if current_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if current_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        for driver in current_race.drivers:
            if driver == current_driver:
                return f"Driver {driver_name} is already added in {race_name} race."
        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        current_race = self.check_if_race_exists(self.races, race_name)
        if current_race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(current_race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[:3]
        result = ''
        for winner in winners:
            winner.number_of_wins += 1
            result += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"
        return result.strip()












