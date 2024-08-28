# Create a class method to return the reversed string of a given string.

def reverse_string(s):
    return s[::-1]

def main():
    s = input("Enter a string: ")
    print("Reversed string: ", reverse_string(s))

if __name__ == "__main__":
    main()