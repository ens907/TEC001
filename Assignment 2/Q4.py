year = int(input("Enter a year:"))


if int(year) % 100 == 0:
    if int(year) % 400 == 0:
        print("It is a leap year.")
    else:   
        print("It is not a leap year.")
elif int(year) % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")