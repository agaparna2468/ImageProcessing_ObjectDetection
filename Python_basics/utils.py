def find_max(numbers):
    maxm = numbers[0]
    for num in numbers:
        if (num  >  maxm):
            maxm = num
    return maxm