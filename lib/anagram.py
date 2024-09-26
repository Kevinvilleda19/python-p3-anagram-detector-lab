class Anagram:
    def __init__(self, word):
        # Store the word after sorting its letters for comparison later
        self.word = word.lower()  # Normalize case by converting to lowercase

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)

        # List comprehension to find the matching anagrams
        return [word for word in word_list if sorted(word.lower()) == sorted_word]


