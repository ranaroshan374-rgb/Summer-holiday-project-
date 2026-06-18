def sort_words_by_length(sentence):
        words = sentence.split()

            for i in range(len(words)):
                    for j in range(i + 1, len(words)):
                                if len(words[i]) > len(words[j]):
                                                words[i], words[j] = words[j], words[i]

                                                    return words

                                                    # Input
                                                    sentence = input("Enter a sentence: ")

                                                    print("Words sorted by length:")
                                                    print(sort_words_by_length(sentence))