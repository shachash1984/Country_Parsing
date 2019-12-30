#! /usr/bin/python


class Country:
    index = {'name': 0, 'population': 1, 'capital': 2, 'city_pop': 3, 'continent': 4,
             'ind_date': 5, 'currency': 6, 'religion': 7, 'language': 8}

    # Insert your code here
    # 1a) Implement a constructor
    def __init__(self, line):
        if line.strip():
            values = line.split(',')
            self.name = values[0]
            self.population = values[1]
            self.capital = values[2]
            self.city_pop = values[3]
            self.continent = values[4]
            self.ind_date = values[5]
            self.currency = values[6]
            self.religion = values[7]
            self.language = list(values[:-1])
        else:
            self.name = None
            self.population = None
            self.capital = None
            self.city_pop = None
            self.continent = None
            self.ind_date = None
            self.currency = None
            self.religion = None
            self.language = None

    @property
    def country_name(self):
        return self.name

    @property
    def country_population(self):
        return self.population

    # 1b) Implement a print method
    def __repr__(self):
        return "name: {}, population: {}, capital: {}, city_pop: {}, continent: {}, ind_date: {}, currency: {}, religion: {}, language: {}".format(
            self.country_name, self.country_population, self.capital, self.city_pop,
            self.continent, self.ind_date, self.currency, self.religion,
            str(self.language))

    def print(self):
        print(self.name)

    """def __add__(self, other):
        my_pop = int(self.country_population)
        other_pop = int(other.country_population)
        my_pop += other_pop
        self.population = str(my_pop)
    """
    # 1c) Overloaded stringification

    # Getter methods
    # 1d) Implement a getter method for country name

    # 1e) Overloaded + and -

    # If time allows:
    # 1f)  Overloaded == (for index search)
