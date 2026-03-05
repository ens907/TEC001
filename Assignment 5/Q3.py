import re

def sum_numbers(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    
    total = 0
    for num in numbers:
        total = total + int(num)
    return total

text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
result = sum_numbers(text)
print(result)