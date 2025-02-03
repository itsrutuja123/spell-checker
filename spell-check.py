from spellchecker import SpellChecker

def spell_check(text):
    # Initialize the SpellChecker object
    spell = SpellChecker()
    
    # Tokenize the text into words
    words = text.split()
    
    # Get the misspelled words
    misspelled = spell.unknown(words)
    
    # Correct each word in the text
    corrected_words = []
    for word in words:
        if word in misspelled:
            # If the word is misspelled, get the best correction
            corrected = spell.correction(word)
            corrected_words.append(corrected)
        else:
            corrected_words.append(word)
    
    # Join the corrected words back into a sentence
    corrected_text = ' '.join(corrected_words)
    
    return corrected_text

# Taking input from the user
user_text = input("Please enter a sentence for spell checking: ")

# Displaying the original and corrected text
print("Original Text: ", user_text)
print("Corrected Text: ", spell_check(user_text))

