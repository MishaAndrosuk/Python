# class Passport:
#     def __init__(self, first_name, last_name, date_of_birth, passport_number, nationality):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.passport_number = passport_number
#         self.nationality = nationality

#     def create_passport(self, first_name, last_name, date_of_birth, passport_number, nationality):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.passport_number = passport_number
#         self.nationality = nationality

#     def read_passport(self):
#         print("Passport Information:")
#         print("First Name:", self.first_name)
#         print("Last Name:", self.last_name)
#         print("Date of Birth:", self.date_of_birth)
#         print("Passport Number:", self.passport_number)
#         print("Nationality:", self.nationality)

#     def update_passport(self, first_name=None, last_name=None, date_of_birth=None, passport_number=None, nationality=None):
#         if first_name:
#             self.first_name = first_name
#         if last_name:
#             self.last_name = last_name
#         if date_of_birth:
#             self.date_of_birth = date_of_birth
#         if passport_number:
#             self.passport_number = passport_number
#         if nationality:
#             self.nationality = nationality

#     def delete_passport(self):
#         self.first_name = None
#         self.last_name = None
#         self.date_of_birth = None
#         self.passport_number = None
#         self.nationality = None


# class ForeignPassport(Passport):
#     def __init__(self, first_name, last_name, date_of_birth, passport_number, nationality, foreign_passport_number):
#         super().__init__(first_name, last_name, date_of_birth, passport_number, nationality)
#         self.foreign_passport_number = foreign_passport_number
#         self.visas = []

#     def create_foreign_passport(self, first_name, last_name, date_of_birth, passport_number, nationality, foreign_passport_number):
#         self.create_passport(first_name, last_name, date_of_birth, passport_number, nationality)
#         self.foreign_passport_number = foreign_passport_number

#     def read_foreign_passport(self):
#         self.read_passport()
#         print("Foreign Passport Number:", self.foreign_passport_number)
#         print("Visas:", self.visas)

#     def update_foreign_passport(self, first_name=None, last_name=None, date_of_birth=None, passport_number=None, nationality=None, foreign_passport_number=None):
#         self.update_passport(first_name, last_name, date_of_birth, passport_number, nationality)
#         if foreign_passport_number:
#             self.foreign_passport_number = foreign_passport_number

#     def delete_foreign_passport(self):
#         self.delete_passport()
#         self.foreign_passport_number = None
#         self.visas = []

#     def add_visa(self, visa):
#         self.visas.append(visa)

#     def remove_visa(self, visa):
#         self.visas.remove(visa)



# people = Passport("Misha", "Androshchuk", "22/11/2007", "123456", "Ukrainian")
# people.read_passport()

# print("\n")

# people.update_passport("Mykhailo", "Androshchuk", "22/11/2007", "123456", "Ukrainian")
# people.read_passport()



#------------------------------------------------------------



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def calculate_count(start, end):
        return abs(end - start)

celsius = 25
fahrenheit = 77

converted_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
converted_celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
count = TemperatureConverter.calculate_count(celsius, fahrenheit)

print(f"{celsius} degrees Celsius is equal to {converted_fahrenheit} degrees Fahrenheit.")
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius.")
print(f"The number of temperature conversions needed is {count}.")
