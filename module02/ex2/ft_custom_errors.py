class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_custom_error(error_idx: int) -> None:
    match error_idx:
        case 0:
            raise PlantError("The tomato plant is wilting!")
        case 1:
            raise WaterError("Not enough water in the tank!")


def catch_custom_errors():
    try:
        print("Testing PlantError...")
        raise_custom_error(0)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        raise_custom_error(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_custom_error(0)
    except GardenError as e:
        print(f"Caught WaterError: {e}")

    try:
        raise_custom_error(1)
    except GardenError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("All custom error types work correctly!")


print("=== Custom Garden Errors Demo ===")
print()
catch_custom_errors()
