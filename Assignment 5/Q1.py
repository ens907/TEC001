import re

def is_course_code(text):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False
    
print(is_course_code("TEC001"))
print(is_course_code("AU006"))
print(is_course_code("abcdefgh1374239"))
print(is_course_code("F25"))