def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def worker(n: int, idx: int) -> None:
        if idx > n:
            return
        print(f"Day {idx}")
        worker(n, idx + 1)

    worker(n, 1)
    print("Harvest time!")
