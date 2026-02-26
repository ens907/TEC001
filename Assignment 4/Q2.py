number = int(input("Enter a number: "))
prime = True

if number < 2:
    prime = False

for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")