# import time

# def calculate_time(func):
#     def wrapper():
#         start_time = time.time()
#         result = func()
#         end_time = time.time()
#         execution_time = end_time - start_time
#         return result, execution_time
#     return wrapper

# @calculate_time
# def generate_even_numbers():
#     even_numbers = [num for num in range(0, 100001) if num % 2 == 0]
#     return even_numbers

# even_numbers, execution_time = generate_even_numbers()
# print("Парні числа:", even_numbers)
# print("Для обчислення потрібно:", execution_time, "секунд")




def fix_input_params(func):
    def wrapper(*args, **kwargs):
        corrected_args = []
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                corrected_args.append(1)
            else:
                corrected_args.append(arg)
        return func(*corrected_args, **kwargs)
    return wrapper


@fix_input_params
def calculate_rectangle_area(length, width):
    return length * width

print(calculate_rectangle_area(10, -5))  # 50
