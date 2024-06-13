class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 20000000 or self.area > 3000000
    
    def compare_population_density(self, other_country):
        self_density = self.population / self.area
        other_density = other_country.population / other_country.area
        
        if self_density > other_density:
            return f"{self.name} has a larger population density than {other_country.name}"
        elif self_density < other_density:
            return f"{self.name} has a smaller population density than {other_country.name}"
        else:
            return f"{self.name} has the same population density as {other_country.name}"

country1 = Country("CountryA", 55000000, 4000000)
country2 = Country("CountryB", 15000000, 2000000)
country3 = Country("CountryC", 10000000, 1000000)

print(country1.is_big)
print(country2.is_big)
print(country3.is_big)

print(country1.compare_population_density(country2))
print(country1.compare_population_density(country3))
print(country2.compare_population_density(country3))
