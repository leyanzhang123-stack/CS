if (
    10 <= (t := int(input("Enter the time in 24-hour format (0-23): "))) <= 16
    and (sun := input("Is the sun shining? (yes/no): ").lower() == "yes")
):
    print("Please use sunscreen.")