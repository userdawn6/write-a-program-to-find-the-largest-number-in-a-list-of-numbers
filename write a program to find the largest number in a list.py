def find_largest_number(numbers):
    if len(numbers) == 0:
        return None

    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


number_list = (1, 2, 3, 4, 5)
largest_number = find_largest_number(number_list)
print("The largest number in this list is = ", largest_number)
