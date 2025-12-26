def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError("Error: Water level " +
                         f"{water_level}" +
                         " is too high (max 10)"
                         )
    if water_level < 1:
        raise ValueError("Error: Water level " +
                         f"{water_level}" +
                         " is too low (min 1)"
                         )

    if sunlight_hours > 12:
        raise ValueError("Error: Sunlight hours " +
                         f"{sunlight_hours}" +
                         " is too high (max 12)"
                         )
    if sunlight_hours < 2:
        raise ValueError("Error: Sunlight hours " +
                         f"{sunlight_hours}" +
                         " is too low (min 2)"
                         )
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("Testing with good values...")
    check_plant_health("tomato", 5, 6)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(e)

    print("\nTesting sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


print("=== Garden Plant Health Checker ===\n")
test_plant_checks()
