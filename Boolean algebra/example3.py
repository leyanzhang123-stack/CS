if (
    day := int(input("Enter the number of day in a week: ")) in [6, 7]
    or (vacation := input("Is James on vacation? (yes/no): ").lower() == "yes")
):
    print("True")
else:
    print("False")