def find_keyword_lines(filename, keyword):
    file = open(filename, 'r')
    
    line_numbers = []
    current_line = 1
    
    for line in file:
        if keyword in line:
            line_numbers.append(current_line)
        
        current_line = current_line + 1
        
    file.close()
    return line_numbers