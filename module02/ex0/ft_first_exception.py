def check_temperature(temp_str) -> None:
    '''checks the validity of the temperature'''
    print(f"Testing temperature {temp_str}")
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (max 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except Exception:
        print(f"Error: {temp_str} is not a valid number")


print("=== Garden Temperature Checker ===")
print()
check_temperature("25")
print()
check_temperature("abc")
print()
check_temperature("100")
print()
check_temperature("-50")
print("\nAll tests completed - program didn't crash!")
