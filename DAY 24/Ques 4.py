def remove_duplicates(s):
        return ''.join(dict.fromkeys(s))

        # Input
        string = input("Enter a string: ")

        print("String after removing duplicates:", remove_duplicates(string))