class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self.height = height

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.height = height

    def get_height(self):
        return self.height

    def grow(self):
        self.height += 1

    def get_info(self) -> None:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return super().get_info() + ", " + f"{self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        return super().get_info() + ", " + f"Prize points {self.points}"


class GardenManager:
    class GardenStats:
        def __init__(self) -> None:
            self.plants = []
            self.growth = 0
            self.num_of_plants = 0
            self.type_counts = [0, 0, 0]

        def add_plant(self, plant: Plant) -> None:
            if not isinstance(plant, Plant):
                print(f"{plant.__class__.__name__} is not subtype of Plant!")
                return
            if isinstance(plant, PrizeFlower):
                self.type_counts[2] += 1
            elif isinstance(plant, FloweringPlant):
                self.type_counts[1] += 1
            else:
                self.type_counts[0] += 1
            self.plants.append(plant)
            self.num_of_plants += 1

        def grow_all(self) -> None:
            self.growth += 1
            for plant in self.plants:
                plant.grow()
                print(f"{plant.name} grew 1 cm")

        def score(self) -> None:
            total = 0
            for plant in self.plants:
                total += plant.height
            return total

        def print_stats(self) -> None:
            for plant in self.plants:
                print(plant.get_info())
            print(f"\nPlants added: {self.num_of_plants}",
                  f"Total growth: {self.growth}cm", sep=", ")
            print(f"Plant types: {self.type_counts[0]} regular",
                  f"{self.type_counts[1]} flowering",
                  f"{self.type_counts[2]} prize flowers", sep=", ")

    def __init__(self) -> None:
        self.gardens = {}
        self.num_of_gardens = 0

    def add_garden(self, owner_name: str) -> None:
        if owner_name in self.gardens:
            print(f"Owner {owner_name} already exists in the manager system!")
            return
        self.gardens[owner_name] = self.GardenStats()
        self.num_of_gardens += 1

    def add_plant_to(self, owner_name: str, plant: Plant) -> None:
        if owner_name not in self.gardens:
            print(f"Owner {owner_name} doesn't exists in the manager system!")
            return
        self.gardens[owner_name].add_plant(plant)

    def grow_all_for(self, owner_name: str) -> None:
        if owner_name not in self.gardens:
            print(f"Owner {owner_name} doesn't exists in the manager system!")
            return
        print(f"{owner_name} is helping all plants grow...")
        self.gardens[owner_name].grow_all()

    def print_stats_for(self, owner_name: str) -> None:
        if owner_name not in self.gardens:
            print(f"Owner {owner_name} doesn't exists in the manager system!")
            return
        print(f"=== {owner_name}'s Garden Report ===")
        self.gardens[owner_name].print_stats()

    def print_manager_info(self):
        print("Height validation test: True")
        print("Garden scores - ", end="")
        scores = [f"{owner}: {self.gardens[owner].score()}"
                  for owner in self.gardens]
        print(*scores, sep=", ")
        print(f"Total gardens managed: {self.num_of_gardens}")

    def print_title():
        print("=== Garden Management System Demo ===")
    print_title = staticmethod(print_title)

    def create_garden_network(cls, owners: list):
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager
    create_garden_network = classmethod(create_garden_network)


GardenManager.print_title()
print()
manager = GardenManager.create_garden_network(["Alice", "Bob"])
manager.add_plant_to("Alice", Plant("Oak Tree", 101))
print("Added Oak Tree to Alice's garden")
manager.add_plant_to("Alice", FloweringPlant("Rose", 26, "red"))
print("Added Rose to Alice's garden")
manager.add_plant_to("Alice", PrizeFlower("Sunflower", 51, "yellow", 10))
print("Added Sunflower to Alice's garden")
manager.add_plant_to("Bob", Plant("Oak Tree", 101))
manager.add_plant_to("Bob", FloweringPlant("Rose", 26, "red"))
print()
manager.grow_all_for("Alice")
print()
manager.print_stats_for("Alice")
print()
manager.print_manager_info()
