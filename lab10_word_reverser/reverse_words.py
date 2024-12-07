def reverse_words(text):
    result = []

    for word in text.split():
        letters = [char for char in word if char.isalpha()]
        letters.reverse()

        new_word = ''.join(letters.pop(0) if char.isalpha() else char for char in word)
        result.append(new_word)

    return ' '.join(result)