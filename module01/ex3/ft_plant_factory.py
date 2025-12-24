class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name.title()
        self.__height = height
        self.__age = age

    def creation_msg(self) -> None:
        print(f"Created: {self.__name} ({self.__height}cm, {self.__age} days)")


def ft_plant_factory(name: str, height: int, age: int) -> Plant:
    return Plant(name, height, age)


plants = [
    ft_plant_factory("Rose", 25, 30),
    ft_plant_factory("Sunflower", 80, 45),
    ft_plant_factory("Cactus", 15, 120),
    ft_plant_factory("Oak", 80, 45),
    ft_plant_factory("Fern", 15, 120)
]

print("=== Plant Factory Output ===")
for plant in plants:
    plant.creation_msg()

print("\nTotal plants created: 5")
