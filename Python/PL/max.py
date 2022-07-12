n = input()

int_n = int(n)
arr_numbers = []

for i in range(int_n):
    numbers = input()
    int_numbers = int(numbers)
    arr_numbers.append(int_numbers)

maxmax = max(arr_numbers)
print(maxmax)