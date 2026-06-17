def find_longest_word(sentence):
        words = sentence.split()
            longest_word = ""

                for word in words:
                        if len(word) > len(longest_word):
                                    longest_word = word

                                        return longest_word

                                        # Input
                                        sentence = input("Enter a sentence: ")

                                        print("Longest word:", find_longest_word(sentence))