year = int(input("Введите год: "))
if (year < 4):
    print("Год не является високосным.")
elif ((year % 4) != 0):
    print("Год не является високосным.")
else:
    if ((year % 100) != 0):
        print("Год является високосным.")
    else:
        if ((year % 400) == 0):
            print("Год является високосным.")
        else:
            print("Год не является високосным.")