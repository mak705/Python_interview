def count(string, letter_were_looking_for):
    result = 0
    for letter in string:
        if letter == letter_were_looking_for:
            result = result + 1
    return result
    
print count('supercalifragilisticexpialidocious', 'l')
