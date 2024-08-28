# Write a Python program to sort a list of tuples by the second item using a lambda function.

def sort_list_of_tuples_by_second_item(lst):
    return sorted(lst, key=lambda x: x[1])

def main():
    lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_of_tuples_by_second_item(lst))

main()