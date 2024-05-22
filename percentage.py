total_sum = 0
for i in range(3):
    number = float(input(f'numeris {i + 1}:'))
    total_sum += number
average = total_sum / 3
print(f'1 : {total_sum}, 2: {average}')