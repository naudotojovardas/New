def calculate_bmi(height, weight):
    return weight / (height ** 2)

height = float(input('input height: '))
weight = float(input('input weight: '))
bmi = calculate_bmi(height, weight)
print(f'bmi is : {bmi}')