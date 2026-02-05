while True:
    inches = float(input("Enter length in inches: "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(centimeters, 'cm')