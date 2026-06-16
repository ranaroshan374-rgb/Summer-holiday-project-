def count_vowels_consonants(text):
        vowels = "aeiouAEIOU"
            vowel_count = 0
                consonant_count = 0

                    for char in text:
                            if char.isalpha():
                                        if char in vowels:
                                                        vowel_count += 1
                                                                    else:
                                                                                    consonant_count += 1

                                                                                        return vowel_count, consonant_count


                                                                                        # Input
                                                                                        string = input("Enter a string: ")

                                                                                        # Output
                                                                                        vowels, consonants = count_vowels_consonants(string)

                                                                                        print("Vowels:", vowels)
                                                                                        print("Consonants:", consonants)