#I actually spend some time working on this exercise but it didn't work out at all so i ended up seeking help from AI. It was pretty complicated at first but after I asked for directions, I understood how to solve this

def caesar_cipher(filename, n, direction):
    if direction == "right":
        shift = n
    else:
        shift = -n

    file = open(filename, 'r')
    ciphertext = ""

    for line in file:
        for char in line: #this part is to chrck if its an uppercase letter
            if 'A' <= char <= 'Z':
                x = ord(char)
                y = (x - 65 + shift) % 26 + 65
                ciphertext = ciphertext + chr(y) #chr() converts the ID back to the character (i just learnt it)
            
            elif 'a' <= char <= 'z': #same as the above but for lowercase letter
                x = ord(char)
                y = (x - 97 + shift) % 26 + 97
                ciphertext = ciphertext + chr(y)
            
            elif '0' <= char <= '9': #check if its a number
                pass
            
            else: #covers the leftovers like period, comma, ...
                ciphertext = ciphertext + char

    file.close()

    output_file = open("ciphertext.txt", "w")
    output_file.write(ciphertext)
    output_file.close()