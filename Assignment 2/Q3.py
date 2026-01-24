sex = input("Enter biological sex: ")
hemoglobin = float(input("Enter hemoglobin value: "))

if sex == "female":
    if hemoglobin < 117:
        print("Hemoglobin is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")
elif sex == "male":
    if hemoglobin < 134:
        print("Hemoglobin is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")
