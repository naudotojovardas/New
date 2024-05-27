def vs(a=10, b="l"):
    try:
        outcome = (a / b)
        return outcome
    except (ZeroDivisionError, TypeError) as e:
        print(f'Attempted division:', {e})
    finally:
        print('Attempted division')

print(vs(a=10, b="l"))

