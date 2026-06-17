def first_repeating_character(s):
        seen = set()

            for char in s:
                    if char in seen:
                                return char
                                        seen.add(char)

                                            return None


                                            # Input
                                            string = input("Enter a string: ")

                                            result = first_repeating_character(string)

                                            if result:
                                                print("First repeating character:", result)
                                                else:
                                                    print("No repeating character found.")