def get_average_score(filename):
    file = open(filename, 'r')
    
    total_score = 0
    student_count = 0
    
    for line in file:
        parts = line.split(",")
        score_text = parts[1]
        score_number = int(score_text)
        
        total_score = total_score + score_number
        student_count = student_count + 1
        
    file.close()
    
    average = total_score / student_count
    return average