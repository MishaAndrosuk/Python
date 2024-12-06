first_cities = {'Kyiv', 'Lviv', 'Odessa', 'Kharkiv', 'Dnipro', 'Donetsk', 'Zaporizhzhia', 'Kryvyi Rih', 'Mykolaiv', 'Mariupol'}
second_cities = {'Lviv', 'Kharkiv', 'Dnipro', 'Zaporizhzhia', 'Kryvyi Rih', 'Mykolaiv', 'Berlin', 'Paris', 'London'}

print(f"Union: {first_cities.union(second_cities)}")
print(f"Intersection: {first_cities.intersection(second_cities)}")
print(f"Difference: {first_cities.difference(second_cities)}")
print(f"Symmetric difference: {first_cities.symmetric_difference(second_cities)}")