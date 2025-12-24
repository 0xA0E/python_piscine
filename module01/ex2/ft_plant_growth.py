class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name.title()
        self.__height = height
        self.__age = age

    def grow(self):
        self.__height += 1

    def age(self):
        self.__age += 1

    def get_info(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

print("=== Day 1 ===")
for plant in plants:
    plant.get_info()

idx = 0
while idx < 6:
    for plant in plants:
        plant.age()
        plant.grow()
    idx += 1

print("=== Day 7 ===")
for plant in plants:
    plant.get_info()
    print("Growth this week: +6cm")
