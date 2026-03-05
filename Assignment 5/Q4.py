import re

def redact_phone(text):
    text = re.sub(r'\+84\d+', '[REDACTED]', text)
    text = re.sub(r'\d{10}', '[REDACTED]', text)
    return text

text = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
result = redact_phone(text)
print(result)