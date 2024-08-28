# Create a SpaceStation class with the following specifications:
# The SpaceStation class should have an attribute astronauts which is a list of dictionaries. -
# - Each dictionary represents an astronaut and has keys: name, nationality, and mission_duration.
# It should have an instance method add_astronaut that takes a name, nationality, and mission duration, -
# - creates a new astronaut dictionary, and adds it to the astronaut's list.
# It should have an instance method find_astronaut that takes a name and returns the astronaut dictionary with that name, or None if no such astronaut is found.
# Add a class method from_astronaut_list that takes a list of astronauts (each represented as a dictionary) and returns a new SpaceStation instance with those astronauts.
# Add a static method is_long_term_mission that takes an astronaut dictionary and returns True if the astronaut's mission duration is more than 6 months, and False otherwise.
# Add an instance method remove_astronaut that takes a name and removes the astronaut with that name from the astronauts' list.
# MY MODS:
# I added a time.sleep(2) to simulate a delay in the methods that add, find, and remove astronauts.
# I added print statements instead of returning true or false to make the output more readable and more realistic.


import time


class SpaceStation:
    def __init__(self, astronauts = []):
        self.astronauts = astronauts

    def add_astronaut(self, name):
        self.astronauts.append(name)
        print(f"Adding {name}...")
        time.sleep(2)
        return (f"Added {name}")

    def find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                print(f"Finding {name}...")
                time.sleep(2)
                return (f"Found {name}")
        print(f"Finding {name}...")
        time.sleep(2)
        return (f"No astronaut with name {name} found.")

    @classmethod
    def from_astronaut_list(cls, astronauts):
        instance = cls()
        instance.astronauts = astronauts
        return instance

    @staticmethod
    def is_long_term_mission(astronauts: list, name):
        for astronaut in astronauts:
            if name == astronaut["name"]:
                if astronaut['mission_duration'] > 6:
                    return (f"{astronaut['name']} is on a long term mission.")
                else:
                    return (f"{astronaut['name']} is on a short term mission.")

    def remove_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                self.astronauts.remove(astronaut)
                print(f"Removing...")
                time.sleep(2)
                return (f"Removed {name}")
        print('Removing...')
        time.sleep(2)
        return (f"No astronaut with name {name} found.")


astronauts = [
    {'name': 'Mark', 'nationality': 'American', 'mission_duration': 6},
    {'name': 'Olga', 'nationality': 'Russian', 'mission_duration': 8},
    {'name': 'David', 'natonality': 'American', 'mission_duration': 5},
]

station = SpaceStation.from_astronaut_list(astronauts)
print(station.astronauts)
print(station.find_astronaut('Olga'))
print(station.is_long_term_mission(astronauts, "Olga"))
print(station.remove_astronaut('David'))
print(station.astronauts)