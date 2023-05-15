def find_largest_number(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers(0)
    for number in numbers:
        if number > largest:
            largest = number

    return largest


num_list = (1, 2, 3, 4, 5)
largest_number = find_largest_number(num_list)
print("The largest number in the list is:", largest_number)
