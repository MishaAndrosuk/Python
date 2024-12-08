#HomeWork

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# def odd_numbers(start, end):
#     for num in range(start, end+1):
#         if num % 2 != 0:
#             yield num

# start = int(input("Введіть початкове число: "))
# end = int(input("Введіть кінцеве число: "))

# if start >= end:
#     print("Error: Start number must be greater than end number.")
#     exit()

# result = odd_numbers(start, end)

# for num in result:
#     print(num)


#------------------------------------------------------------


def filter_range(numbers, start, end):
    for num in numbers:
        if num < start or num > end:
            yield num

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

if start >= end:
    print("Error: Start number must be greater than end number.")
    exit()

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
filtered_numbers = filter_range(numbers, start, end)

for num in filtered_numbers:
    print(num)