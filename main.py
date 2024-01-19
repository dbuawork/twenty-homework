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


# Приклад використання
city1 = City("Київ", "Київська область", "Україна", 2800000, "02000", "+380")

# Доступ до полів через методи
print(f"Назва міста: {city1.get_name()}")
print(f"Регіон: {city1.get_region()}")
print(f"Країна: {city1.get_country()}")
print(f"Населення: {city1.get_population()}")
print(f"Поштовий індекс: {city1.get_postal_code()}")
print(f"Телефонний код: {city1.get_phone_code()}")