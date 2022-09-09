

def subtitution_cipher():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "fcpevqkzgmtrayonujdlwhbxsi"
    text = input("Enter plaintext: ")

    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter

    print(result) 


subtitution_cipher() 
