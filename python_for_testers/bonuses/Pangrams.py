def is_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in text.lower():
            return False
    return True


text_to_send = 'the quick brown fox jumps over the lazy dog'
if (is_pangram(text_to_send) == True):
    print("Yes, is pangrams!")
else:
    print("No, is pangrams!")
