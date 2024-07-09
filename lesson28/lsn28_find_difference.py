# Add two given lists and find the difference between lists using map()

def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

def subtract_lists(list1, list2):
    return list(map(lambda x, y: x - y, list1, list2))

def main():
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    print("List 1:", list1)
    print("List 2:", list2)
    print("Sum of lists:", add_lists(list1, list2))
    print("Difference of lists:", subtract_lists(list1, list2))

main()