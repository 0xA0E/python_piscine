class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name.title()
        self.__height = height
        self.__age = age

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Height updated: {age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def current_state(self) -> None:
        print(f"Current plant: {self.__name}",
              f"({self.__height}cm, {self.__age} days)")


plant = SecurePlant("Rose", 20, 10)
print("=== Garden Security System ===")
plant.set_height(25)
plant.set_age(30)
print()
plant.set_height(-5)
print()
plant.current_state()
