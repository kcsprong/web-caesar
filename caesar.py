import string

def encrypt(text,rot):
    newtext= ""
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext

def alphabet_position(letter):
    if letter.isalpha():
        letter = letter.lower()
        return list(string.ascii_lowercase).index(letter)
    else:
        return letter

def rotate_character(char,rot):
    if char.isalpha():
        if char.islower():
            return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]
        elif char.isupper():
            return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    else:
        return char
