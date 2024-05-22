size = int(input("Enter the triangle size: "))
for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # move to the next line after each row