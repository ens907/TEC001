phrase = input("Enter a phrase: ")
words = phrase.split()
acronym = ""

for x in words:
    acronym = acronym + x[0].upper()
print("The acronym is:", acronym)