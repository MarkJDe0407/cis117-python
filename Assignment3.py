Highway_number = int(input("Enter a highway number: "))
if Highway_number >= 1 and Highway_number <= 99:
    print(f"Highway {Highway_number} is a Primary highway.")
    if Highway_number % 2 == 0:
        print(f"Highway {Highway_number} is an East/West highway.")
    else:
        print(f"Highway {Highway_number} is a North/South highway.")
elif Highway_number >= 100 and Highway_number <= 999:
    if Highway_number % 100 == 0:
        print(f"Highway {Highway_number} is not a valid Interstate highway.")
    else:
        print(f"Highway {Highway_number} is an auxiliary highway.")
        parent_highway = Highway_number % 100
        print(f"Parent highway is: I-{parent_highway:02d}")
else:
    print(f"Highway {Highway_number} is an invalid Interstate highway.")