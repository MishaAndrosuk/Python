# Завадння 1,2

# fruits = ('applebanana', 'banana', 'orange', 'mango-apple', 'kiwi', 'grape')

# fruit_name = input("Enter the name of a fruit: ")

# count = 0
# for fruit in fruits:
#     if fruit_name in fruit:
#         count += 1

# print("Number of", fruit_name, "fruits:", count)




# Завдання 3

cars = ('audi', 'bmwmer', 'subaru', 'toyota', 'mercedes', 'volkswagen', 'bmw')

word_to_change = input("Enter the word you want to change: ")
new_word = input("Enter the new word: ")

if word_to_change in cars:
    cars = tuple(car.replace(word_to_change, new_word) for car in cars)
    print(cars)
else:
    print("The word is not in the tuple")



# Завдання 4    

# numbers = (1, 22, 3200, 114, 25, 63, 7, 85, 98, 100)

# digit_count = {}

# for num in numbers:
#     num_str = str(num)
#     num_digits = len(num_str)
    
#     if num_digits in digit_count:
#         digit_count[num_digits] += 1
#     else:
#         digit_count[num_digits] = 1

# for digits, count in digit_count.items():
#     print(f"{digits} цифр — {count} елементів")