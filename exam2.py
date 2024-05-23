# Function: Calculate Discounted Price
# Objective: Write a function `calculate_discounted_price` that computes the final price of an item
# after applying a discount percentage.
# Parameters:
# - original_price: An integer representing the original price of the item.
# - discount_percentage: An integer representing the discount rate applied to the original price.
# Returns:
# - The final price after the discount, as a float rounded to two decimal places.

def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return round(final_price, 2)

original_price = float(input('Input price : '))
discout_percentage = float(input('Input discount amount : '))
final_price = calculate_discounted_price(original_price, discout_percentage)
print(f'This is final price : {final_price}')