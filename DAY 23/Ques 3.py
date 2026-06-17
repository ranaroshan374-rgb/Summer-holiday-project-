from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

    # Input
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    if is_anagram(string1, string2):
        print("The strings are Anagrams.")
        else:
            print("The strings are Not Anagrams.")