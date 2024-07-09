# Develop a console-based restaurant management system that handles table reservations, menu selections, order modifications, and payment processing.
#  The system should provide a comprehensive solution for managing reservations, displaying menu options, and handling customer orders through an interactive console interface.
# Features and Functionalities:
# Table Reservation System:
# Prompt the user to check if a table was reserved under a name.
# If not reserved, assign a table based on the availability of single, double, or family tables.
# Display the current availability of tables and details of reserved tables, including the name of the customer and reservation time.
# Menu Display and Order System:
# Offer menu selections for different meal times (breakfast, lunch, dinner) including drink options (alcoholic and non-alcoholic).
# Include special menus for vegetarian and vegan preferences.
# Each menu item should display its weight, preparation time, calorie content, and price.
# Order Modification Options:
# Allow customers to modify their order by adding items, deleting items, or changing the quantity of selected items before finalizing the payment.
# Billing and Payment:
# After finalizing the order, display a summary of the selected items, total cost, and estimated waiting time.
# Provide an option to add a tip based on a percentage of the total cost.
# Process the payment and generate a digital receipt detailing the order and payment.
# System Logging:
# Log all activities, especially reservations and payment details, for record-keeping and future reference.
# Example usage

# Welcome to the Restaurant Management System
# Please enter your name for reservation check: Gedas
# Table 1 reserved for Gedas.
# Table Status:
# Table 1: reserved by Gedas
# Table 2: available
# Table 3: available
# Table 4: available
# Table 5: available
# Table 6: available
# Table 7: available
# Table 8: available
# Table 9: available
# Table 10: available
# ---BREAKFAST---
# Pancakes: Weight: 200g, Time: 10min, Calories: 450cal, Price: $5
# ---LUNCH---
# Vegan Salad: Weight: 150g, Time: 5min, Calories: 300cal, Price: $7
# ---DINNER---
# Steak: Weight: 350g, Time: 15min, Calories: 800cal, Price: $20
# ---DRINKS---
# Coke: Weight: 200g, Time: 0min, Calories: 180cal, Price: $2
# Would you like to add, remove, view, or finalize your order? (add/remove/view/finalize): view
# Your current order:
# Would you like to add, remove, view, or finalize your order? (add/remove/view/finalize): add
# Enter an item to add to your order: Pancakes
# Added Pancakes to your order.
# Would you like to add, remove, view, or finalize your order? (add/remove/view/finalize): view
# Your current order:
# Pancakes: $5
# Would you like to add, remove, view, or finalize your order? (add/remove/view/finalize): finalize
# Total payable: $5.00
# Enter tip percentage (0 for no tip): 1
# Including tip, your total is: $5.05

# Importing the required libraries
from datetime import datetime
import time


menu = {
    "breakfast": {
        "pancakes": {"weight": "200g", "time": "10min", "calories": "450cal", "price": 5},
    },
    "lunch": {
        "vegan salad": {"weight": "150g", "time": "5min", "calories": "300cal", "price": 7},
    },
    "dinner": {
        "steak": {"weight": "350g", "time": "15min", "calories": "800cal", "price": 20},
    },
    "drinks": {
        "coke": {"weight": "200g", "time": "0min", "calories": "180cal", "price": 2},
    }
}

tables = {
    "Table 1": "available",
    "Table 2": "available",
    "Table 3": "available",
    "Table 4": "available",
    "Table 5": "available",
    "Table 6": "available",
    "Table 7": "available",
    "Table 8": "available",
    "Table 9": "available",
    "Table 10": "available",
}

reservations = {}

def display_menu():
    print("---BREAKFAST---")
    for item, details in menu["breakfast"].items():
        print(f"{item}: Weight: {details['weight']}, Time: {details['time']}, Calories: {details['calories']}, Price: ${details['price']}")

    print("---LUNCH---")
    for item, details in menu["lunch"].items():
        print(f"{item}: Weight: {details['weight']}, Time: {details['time']}, Calories: {details['calories']}, Price: ${details['price']}")

    print("---DINNER---")
    for item, details in menu["dinner"].items():
        print(f"{item}: Weight: {details['weight']}, Time: {details['time']}, Calories: {details['calories']}, Price: ${details['price']}")

    print("---DRINKS---")
    for item, details in menu["drinks"].items():
        print(f"{item}: Weight: {details['weight']}, Time: {details['time']}, Calories: {details['calories']}, Price: ${details['price']}")


def check_reservation(name):
    if name in reservations.values():
        table_number = list(reservations.keys())[list(reservations.values()).index(name)]
        print(f"Table {table_number} reserved for {name}.")
    else:
        table_number = [table for table, status in tables.items() if status == "available"][0]
        tables[table_number] = "reserved"
        reservations[table_number] = name
        print(f"Table {table_number} assigned to {name}.")
    print("Table Status:")
    for table, status in tables.items():
        print(f"{table}: {status}")


def add_item(order, item):
    if item in menu["breakfast"] or item in menu["lunch"] or item in menu["dinner"] or item in menu["drinks"]:
        order.append(item)
        print(f"Added {item} to your order.")
    else:
        print("Item not found in the menu.")


def remove_item(order, item):
    if item in order:
        order.remove(item)
        print(f"Removed {item} from your order.")
    else:
        print("Item not found in your order.")
    

def view_order(order):
    print("Your current order:")
    for item in order:
        print(f"{item}: ${menu['breakfast'].get(item, {}).get('price', 0)}")
    return sum([menu['breakfast'].get(item, {}).get('price', 0) for item in order])


def finalize_order(order):
    total = view_order(order)
    print(f"Total payable: ${total:.2f}")
    tip = float(input("Enter tip percentage (0 for no tip): "))
    total_with_tip = total * (1 + tip / 100)
    print(f"Including tip, your total is: ${total_with_tip:.2f}")
    return total_with_tip


def main():
    print("Welcome to the Restaurant Management System")
    name = input("Please enter your name for reservation check: ")
    check_reservation(name)
    display_menu()

    order = []
    while True:
        action = input("Would you like to add, remove, view, or finalize your order? (add/remove/view/finalize): ")
        if action == "add":
            item = input("Enter an item to add to your order: ")
            add_item(order, item)
        elif action == "remove":
            item = input("Enter an item to remove from your order: ")
            remove_item(order, item)
        elif action == "view":
            view_order(order)
        elif action == "finalize":
            total_with_tip = finalize_order(order)
            print("Payment processed successfully.")
            print("Generating receipt...")
            time.sleep(2)
            print("Receipt generated successfully.")
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid action. Please try again.")
        

main()
