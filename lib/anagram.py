# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, possible_anagrams):
        sorted_possible_anagrams = [sorted(possible_anagram.lower()) for possible_anagram in possible_anagrams]

        return [word for word in possible_anagrams if sorted(word.lower()) == sorted(self.word)]

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))