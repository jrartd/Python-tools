# Define three_shouts
def three_shouts(word1, word2, word3):
    def inner(word):
        return word + '!!!'
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
