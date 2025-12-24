class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.title()
        self.height = height
        self.age = age

    def cls_info(self):
        cls = self.__class__.__name__
        return f"{self.name} ({cls}): {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def print_info(self):
        print(super().cls_info(), f"{self.color} color", sep=", ")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")

    def print_info(self):
        print(super().cls_info(), f"{self.diameter}cm diameter", sep=", ")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self):
        print(super().cls_info(), self.harvest_season, sep=", ")


print("=== Garden Plant Types ===")
plants = [
    Flower("Rose", 20, 10, "red"),
    Flower("Rose", 20, 10, "red")
]
for plant in plants:
    plant.print_info()
    plant.bloom()

print()

plants = [
    Tree("Oak", 500, 90, 50),
    Tree("Oak", 500, 90, 50)
]
for plant in plants:
    plant.print_info()
    plant.produce_shade()

print()

plants = [
    Vegetable("Tomato", 80, 90,
              "summer harvest", "Tomato is rich in vitamin C"),
    Vegetable("Tomato", 80, 90,
              "summer harvest", "Tomato is rich in vitamin C")
]

for plant in plants:
    plant.print_info()
    print(plant.nutritional_value)
