class City:
    def __init__(self, name: str, region: str, country: str, population: int, postal_code: str, phone_code: str):
        self._name = name
        self._region = region
        self._country = country
        self._population = population
        self._postal_code = postal_code
        self._phone_code = phone_code

    @property
    def name(self) -> str:
        return self._name

    @property
    def region(self) -> str:
        return self._region

    @property
    def country(self) -> str:
        return self._country

    @property
    def population(self) -> int:
        return self._population

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @property
    def phone_code(self) -> str:
        return self._phone_code

    @name.setter
    def name(self, value: str):
        self._name = value

    @region.setter
    def region(self, value: str):
        self._region = value

    @country.setter
    def country(self, value: str):
        self._country = value

    @population.setter
    def population(self, value: int):
        self._population = value

    @postal_code.setter
    def postal_code(self, value: str):
        self._postal_code = value

    @phone_code.setter
    def phone_code(self, value: str):
        self._phone_code = value


class Country:
    def __init__(self, name: str, continent: str, population: int, phone_code: str, capital: str):
        self._name = name
        self._continent = continent
        self._population = population
        self._phone_code = phone_code
        self._capital = capital
        self._cities = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def continent(self) -> str:
        return self._continent

    @property
    def population(self) -> int:
        return self._population

    @property
    def phone_code(self) -> str:
        return self._phone_code

    @property
    def capital(self) -> str:
        return self._capital

    @property
    def cities(self) -> list:
        return self._cities

    @name.setter
    def name(self, value: str):
        self._name = value

    @continent.setter
    def continent(self, value: str):
        self._continent = value

    @population.setter
    def population(self, value: int):
        self._population = value

    @phone_code.setter
    def phone_code(self, value: str):
        self._phone_code = value

    @capital.setter
    def capital(self, value: str):
        self._capital = value

    @cities.setter
    def cities(self, value: list):
        self._cities = value

    def add_city(self, city: City):
        self._cities.append(city)

    def remove_city(self, city_name: str):
        self._cities = [city for city in self._cities if city.name != city_name]


# Приклад використання
city1 = City("Київ", "Київська область", "Україна", 2800000, "02000", "+380")
city2 = City("Львів", "Львівська область", "Україна", 720000, "79000", "+380")

cities_in_country = [city1, city2]

country = Country("Україна", "Європа", 42000000, "+380", "Київ")

country.add_city(city1)
country.add_city(city2)

print(f"Назва країни: {country.name}")
print(f"Кількість жителів: {country.population}")
print(f"Столиця: {country.capital}")

print("\nМіста в країні:")
for city in country.cities:
    print(f"- {city.name}, Населення: {city.population}, Поштовий індекс: {city.postal_code}, Телефонний код: {city.phone_code}")