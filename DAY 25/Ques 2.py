def common_characters(str1, str2):
        result = ""

            for char in str1:
                    if char in str2 and char not in result:
                                result += char

                                    return result

                                    # Input
                                    string1 = input("Enter first string: ")
                                    string2 = input("Enter second string: ")

                                    print("Common characters:", common_characters(string1, string2))