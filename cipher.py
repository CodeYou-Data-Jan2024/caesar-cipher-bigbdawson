text = input("Please enter a sentence:")
text = text.lower()
reply=""
alphabet = "abcdefghijklmnopqrstuvwxyz"

for t in text:
    for a in alphabet:
        letter = t
        if a == t:
            shift = alphabet.index(a) + 5
            reply += alphabet[shift]
        if letter != t:
            reply += t
print("The encrypted sentence is:", reply)