class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.title()
        self.height = height
        self.age = age


def print_info(plant: Plant) -> None:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]


print("=== Garden Plant Registery ===")
for plant in plants:
    print_info(plant)
