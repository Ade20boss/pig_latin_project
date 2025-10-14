import string
def collect_message():
    """
    Prompt the user to input an English message and return the message as a string.
    This function serves as a utility for collecting user input meant for translation
    into Pig Latin.
    :return: The English message entered by the user
    :rtype: str
    """
    # Prompt the user to enter an English message
    message = input("Enter the English message to translate to Pig latin: ")
    # Return the message
    if not message.strip():
        print("You didn't enter a message")
    return message
def is_number_in_word(word):
    """
    Checks if a string contains at least one numeric digit.

    This function iterates through each character in the input string and
    determines if the string contains any numeric digits. If a numeric digit
    is found, the function immediately returns True. If no numeric digit is
    found after iterating through the entire string, it returns False.

    :param word: The string to be checked for numeric digits.
    :type word: str
    :return: True if the string contains at least one numeric digit, False otherwise.
    :rtype: bool
    """
    # Iterate through each character in the word
    for i in word:
        # Check if the character is a digit
        if i.isdigit():
            return True
    return False
def check_vowel(letter):
    """
    Checks if a given letter is vowel.
    :param letter:
    :return: bool
    """
    return letter.lower() in "aeiou"


def handle_numbers(word):
    """
    Handles the transformation of a given word into a specific format by applying a
    Pig Latin-like translation on its alphabetical characters while preserving the
    original positions of numerical characters. Maintains any non-alphabetical
    characters in their original positions.

    :param word: The input string containing a combination of alphabetical,
        numerical, and possibly special characters.
    :type word: str
    :return: A transformed string with the Pig Latin applied to its alphabetical
        characters while maintaining the original positions of numerical characters.
    :rtype: str
    """
    # Create a list of only the alphabetical characters from the word
    words = [c for c in word if c.isalpha()]
    # Create a dictionary to store the original index and value of each digit
    number_dict = {i: c for i, c in enumerate(word) if c.isdigit()}
    # Define the vowels for Pig Latin translation
    new_word = ""
    # Check if the first alphabetical character is a vowel
    if check_vowel(words[0]):
        # If the first letter is a vowel, add "yay" to the end
        new_word = "".join(words[1:]) + words[0] + "yay"
    # Check if the first alphabetical character is a consonant
    elif not check_vowel(words[0]):
        # Check if the first letter is capitalized
        if words[0].isupper():
            # If capitalized, move the first two letters to the end, change the second letter to uppercase, and add "ay"
            new_word = "".join(words[2:]) + words[1].upper() + words[0].lower() + "ay"
        else:
            # If not capitalized, move the first letter to the end and add "ay"
            new_word = "".join(words[1:]) + words[0] + "ay"
    # Convert the translated word to a list of characters
    new_word = list(new_word)
    # Get the length of the new word
    reconstruct = []
    # Initialize the index of the first letter
    index_of_first_letter = 0
    # Reconstruct the word by inserting the numbers back into their original positions
    for key, value in number_dict.items():
        reconstruct.insert(key, value)
    # Join the list of characters back into a string
    new_word = "".join(new_word)
    # Find the index of the first alphabetical character in the original word
    for j in word:
        if j.isalpha():
            index_of_first_letter = word.index(j)
            break
    # Insert the translated word at the position of the first alphabetical character
    reconstruct.insert(index_of_first_letter, new_word)
    # Join the list into a final string
    reconstruct = "".join(reconstruct)
    # Return the reconstructed word
    return reconstruct


def english_to_pig_latin():
    """
    Translates the input sentence from English to Pig Latin.

    This function processes an input sentence by transforming each word into its
    Pig Latin equivalent. Words that begin with a vowel have "yay" attached to the
    end, while words beginning with consonants have the first letter moved to the
    end and appended with "ay". Words containing numbers are handled separately,
    and punctuation is preserved.

    :returns: The translated Pig Latin sentence as a string.
    :rtype: str
    """
    # Collect the message from the user
    text = collect_message()
    # Split the message into a list of words
    text = text.split()
    # Define the vowels
    # Initialize an empty list to store the translated words
    pig_latin_text = []
    # Iterate through each word in the text
    for word in text:
        # Initialize an empty string for punctuation
        punctuation = ""
        # Check if the last character is punctuation
        if word[-1] in string.punctuation:
            # Store the punctuation and remove it from the word
            punctuation = word[-1]
            word = word[:-1]
        # Check if the first letter is a vowel and the word does not contain numbers
        if check_vowel(word[0]) and is_number_in_word(word) == False:
            # Add "yay" to the end and reattach punctuation
            word = word + "yay" + punctuation
            # Append the translated word to the list
            pig_latin_text.append(word)
        # Check if the first letter is a consonant, not a digit, and the word does not contain numbers
        elif not check_vowel(word[0])and word[0].isdigit() == False and is_number_in_word(word) == False:
            # Check if the first letter is capitalized
            if word[0].isupper():
                # Move the first letter to the end, make it lowercase, capitalize the new first letter, and add "ay"
                word = word[1:].capitalize() + word[0].lower() + "ay" + punctuation
                # Append the translated word
                pig_latin_text.append(word)
            else:
                # Move the first letter to the end and add "ay"
                word = word[1:] + word[0] + "ay" + punctuation
                # Append the translated word
                pig_latin_text.append(word)
        # Check if the word contains numbers
        elif is_number_in_word(word):
            # Call the handle_numbers function to translate the word and append the result
            pig_latin_text.append(handle_numbers(word) + punctuation)
    # Join the translated words into a single string
    pig_latin_text = " ".join(pig_latin_text)
    # Return the final translated text
    return pig_latin_text


# Print the result of the Pig Latin translation
print(english_to_pig_latin())