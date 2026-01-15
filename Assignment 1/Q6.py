talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = int(input("Enter lots: "))


grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)


kilograms = int(grams // 1000)
grams_left = grams - kilograms * 1000

print("Weight in modern units:", kilograms, "kg and", grams_left, "g")