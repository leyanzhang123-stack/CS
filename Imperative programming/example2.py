mark = int(input("Enter the mark:"))
if mark >= 90:
    print("Grade: 10")
elif mark >= 70:  # FIX: the table says 70 marks for grade 9, not 80
    print("Grade: 9")
else:
    print("Grade: 8")
