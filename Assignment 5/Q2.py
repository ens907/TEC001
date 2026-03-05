import re

def is_hex_color(text):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.search(pattern, text):
        return True
    else:
        return False

print(is_hex_color("#AD3453"))  
print(is_hex_color("#000000"))   
print(is_hex_color("dd5733"))    
print(is_hex_color("#FF57"))     
