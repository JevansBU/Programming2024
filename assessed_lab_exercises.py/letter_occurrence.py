def letter_occurrence(input_string):
    # complete function implementation...
    
    count = 0
    for letter in input_string:
        if letter == 'a' or letter == 'A':
            count += 1 
        else:
            pass
    return count


print(letter_occurrence("Amazing")) #2
print(letter_occurrence("Always aim ambitiousl")) #4 
print(letter_occurrence("Hello World")) #0
