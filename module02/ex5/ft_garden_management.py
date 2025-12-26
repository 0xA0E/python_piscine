class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class GardenManager:
    def __init__(self, tank_level) -> None:
        self.plants = {}
        self.tank_level = tank_level

    def check_natural_env(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        error_msg = f"Error checking {plant_name}: "
        if water_level > 10:
            raise WaterError(
                error_msg +
                "Water level " +
                f"{water_level}" +
                " is too high (max 10)"
            )
        if water_level < 1:
            raise WaterError(
                error_msg +
                "Water level " +
                f"{water_level}" +
                " is too low (min 1)"
            )

        if sunlight_hours > 12:
            raise SunlightError(
                error_msg
                + "Sunlight hours "
                + f"{sunlight_hours}"
                + " is too high (max 12)"
            )
        if sunlight_hours < 2:
            raise SunlightError(
                error_msg
                + "Sunlight hours "
                + f"{sunlight_hours}"
                + " is too low (min 2)"
            )
        print(
            f"{plant_name} healthy " +
            f"(water: {water_level}, sun: {sunlight_hours})"
        )

    def check_plant_health(
        self,
        plant_name: str,
    ) -> None:
        try:
            self.check_natural_env(
                plant_name,
                self.plants[plant_name][0],
                self.plants[plant_name][1],
            )
        except GardenError as e:
            print(e)

    def add_plant(self, plant_name: str,
                  water_level: int, sunlight_hours: int) -> None:
        if plant_name == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants[plant_name] = (water_level, sunlight_hours)
        print(f"Added {plant_name} successfully")

    def water_plant(self, plant_name: str) -> None:
        print(f"Watering {plant_name} - success")

    def water_plants(self):
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                self.water_plant(plant)
        except Exception as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_tank_level(self):
        if self.tank_level < 10:
            raise GardenError("Not enough water in tank")


print("=== Garden Management System ===\n")
print("Adding plants to garden...")
garden = GardenManager(6)
garden.add_plant("tomato", 5, 8)
garden.add_plant("lettuce", 15, 8)
try:
    garden.add_plant("", 15, 8)
except PlantError as e:
    print(e)
print()
garden.water_plants()
print()
print("Checking plant health")
garden.check_plant_health("tomato")
try:
    garden.check_plant_health("lettuce")
except GardenError as e:
    print(e)
print()
print("Testing error recovery...")
try:
    garden.check_tank_level()
except GardenError as e:
    print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
print("\nGarden management system test complete!")
