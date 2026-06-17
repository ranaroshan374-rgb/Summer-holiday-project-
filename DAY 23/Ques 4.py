def max_occurring_character(s):
        char_count = {}

            for char in s:
                    char_count[char] = char_count.get(char, 0) + 1

                        max_char = max(char_count, key=char_count.get)
                            return max_char, char_count[max_char]


                            # Input
                            string = input("Enter a string: ")

                            char, count = max_occurring_character(string)

                            print("Maximum occurring character:", char)
                            print("Frequency:", count)