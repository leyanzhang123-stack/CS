while True:
    a = int(input("Enter the number of the card: "))
    if a < 17:
        print("hit")
    elif a > 21:
        print("bust")
    else: 
        print("stay")