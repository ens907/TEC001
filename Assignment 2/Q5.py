def unit_price(diameter, price):
    area = 3.14 * (diameter / 2) ** 2
    return price / area

pizza1_diameter = float(input("Enter the diameter of the 1st pizza in cm: "))
pizza1_price = float(input("Enter the price of the 1st pizza: "))
pizza2_diameter = float(input("Enter the diameter of the 2nd pizza in cm: "))
pizza2_price = float(input("Enter the price of the 2nd pizza: "))

ratio1 = unit_price(pizza1_diameter, pizza1_price)
ratio2 = unit_price(pizza2_diameter, pizza2_price)

if ratio1 < ratio2:
    print("The 1st pizza is the better deal.")
elif ratio2 < ratio1:
    print("The 2nd pizza is the better deal.")
else:
    print("Both pizzas are the same deal.")
