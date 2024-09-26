def encrypt(text, s):
    result = ""

    # Traverse through the given text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        
        # Leave spaces and other non-alphabetic characters as they are
        else:
            result += char

    return result

# Test the function
text = "CEASER CIPHER DEMO"
s = 4
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))
