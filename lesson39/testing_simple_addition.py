# Testing simple addition

def sum_of_three_ints(a: int, b: int, c: int) -> int:
    return a + b + c

def test_add():
    # try: 
        assert sum_of_three_ints(1, 2, 3) == 6
        assert sum_of_three_ints(1, 2, -3) == 0
        assert sum_of_three_ints(1, -2, -3) == -4
        assert sum_of_three_ints(-1, -2, -3) == -6
        assert sum_of_three_ints(0, 0, 0) == 0
        assert sum_of_three_ints(0, 0, 1) == 1
        assert sum_of_three_ints(1054875156, 1, 9878465498498) == 9879520373655
    #     assert sum_of_three_ints(0, 1, c) == 1
    #     assert sum_of_three_ints(1, 0) == 1
    # except TypeError as e:
    #     return f'error: {e}'
    # except NameError as e:
    #     return f'error: {e}'
    # else:
        return "All tests passed"

# Run the test
print(test_add())



