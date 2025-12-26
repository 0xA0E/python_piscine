def water_plants(plant_list: list[str]) -> None:
    '''water the plants safely'''
    try:
        print("Opening watering system")
        for plant in plant_list:
            print(f"Watering {plant.lower()}")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    '''test the water_plants function'''
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    water_plants(["tomato", None])
    print("\nClean up always happens, even with errors!")


print("=== Garden Watering System ===\n")
test_watering_system()
