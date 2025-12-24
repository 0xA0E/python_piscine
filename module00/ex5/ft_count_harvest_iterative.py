def ft_count_harvest_iterative() -> None:
    n = int(input("Days until harvest: "))
    idx = 1
    while idx <= n:
        print(f"Day {idx}")
        idx += 1
    print("Harvest time!")
