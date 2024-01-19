class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self._name = name
        self._region = region
        self._country = country
        self._population = population
        self._postal_code = postal_code
        self._phone_code = phone_code

    def get_name(self):
        return self._name

    def get_region(self):
        return self._region

    def get_country(self):
        return self._country

    def get_population(self):
        return self._population

    def get_postal_code(self):
        return self._postal_code

    def get_phone_code(self):
        return self._phone_code


class Country:
    def __init__(self, name, continent, population, phone_code, capital):
        self._name = name
        self._continent = continent
        self._population = population
        self._phone_code = phone_code
        self._capital = capital
        self._cities = []

    def get_name(self):
        return self._name

    def get_continent(self):
        return self._continent

    def get_population(self):
        return self._population

    def get_phone_code(self):
        return self._phone_code

    def get_capital(self):
        return self._capital

    def get_cities(self):
        return self._cities

    def add_city(self, city):
        self._cities.append(city)

    def remove_city(self, city_name):
        self._cities = [city for city in self._cities if city.get_name() != city_name]


# Приклад використання
city1 = City("Київ", "Київська область", "Україна", 2800000, "02000", "+380")
city2 = City("Львів", "Львівська область", "Україна", 720000, "79000", "+380")

cities_in_country = [city1, city2]

country = Country("Україна", "Європа", 42000000, "+380", "Київ")

country.add_city(city1)
country.add_city(city2)

print(f"Назва країни: {country.get_name()}")
print(f"Кількість жителів: {country.get_population()}")
print(f"Столиця: {country.get_capital()}")

print("\nМіста в країні:")
for city in country.get_cities():
    print(f"- {city.get_name()}, Населення: {city.get_population()}, Поштовий індекс: {city.get_postal_code()}, Телефонний код: {city.get_phone_code()}")