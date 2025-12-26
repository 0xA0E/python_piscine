def garden_operations(error_idx: int) -> None:
    '''Error generator'''
    match error_idx:
        case 0:
            int("abc")
        case 1:
            10 / 0
        case 2:
            with open("missing.txt"):
                pass
        case 3:
            {}['missing\\_plant']
        case 4:
            int("abc")
            10 / 0
            with open("missing.txt"):
                pass
            {}['missing\\_plant']


def test_error_types() -> None:
    '''Testing error types and handling'''
    try:
        print("Testing ValueError...")
        garden_operations(0)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(1)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    try:
        print("Testing FileNotFoundError...")
        garden_operations(2)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print()

    try:
        print("Testing KeyError...")
        garden_operations(3)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
        print()

    try:
        print("Testing multiple errors together")
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Gaught an error, but program continues!")
        print()

    print("All error types tested successfully!")


print("=== Garden Error Types Demo ===")
print()
test_error_types()
