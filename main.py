class City:
    def __init__(self, name: str, region: str, country: str, population: int, postal_code: str, phone_code: str):
        self._name = None
        self._region = None
        self._country = None
        self._population = None
        self._postal_code = None
        self._phone_code = None

        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Назва міста повинна бути непорожнім рядком")

    @property
    def region(self) -> str:
        return self._region

    @region.setter
    def region(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._region = value
        else:
            raise ValueError("Назва регіону повинна бути непорожнім рядком")

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._country = value
        else:
            raise ValueError("Назва країни повинна бути непорожнім рядком")

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, value: int):
        if isinstance(value, int) and value >= 0:
            self._population = value
        else:
            raise ValueError("Населення повинно бути не від'ємним цілим числом")

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._postal_code = value
        else:
            raise ValueError("Поштовий індекс повинен бути непорожнім рядком")

    @property
    def phone_code(self) -> str:
        return self._phone_code

    @phone_code.setter
    def phone_code(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._phone_code = value
        else:
            raise ValueError("Телефонний код повинен бути непорожнім рядком")


class Country:
    def __init__(self, name: str, continent: str, population: int, phone_code: str, capital: str):
        self._name = None
        self._continent = None
        self._population = None
        self._phone_code = None
        self._capital = None
        self._cities = None

        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Назва країни повинна бути непорожнім рядком")

    @property
    def continent(self) -> str:
        return self._continent

    @continent.setter
    def continent(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._continent = value
        else:
            raise ValueError("Назва континенту повинна бути непорожнім рядком")

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, value: int):
        if isinstance(value, int) and value >= 0:
            self._population = value
        else:
            raise ValueError("Населення повинно бути не від'ємним цілим числом")

    @property
    def phone_code(self) -> str:
        return self._phone_code

    @phone_code.setter
    def phone_code(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._phone_code = value
        else:
            raise ValueError("Телефонний код повинен бути непорожнім рядком")

    @property
    def capital(self) -> str:
        return self._capital

    @capital.setter
    def capital(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._capital = value

    @property
    def cities(self) -> list:
        return self._cities

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
    print(
        f"- {city.name}, Населення: {city.population}, Поштовий індекс: {city.postal_code}, Телефонний код: {city.phone_code}")