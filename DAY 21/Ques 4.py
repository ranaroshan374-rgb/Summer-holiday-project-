def to_uppercase(text):
        result = ""
            
                for char in text:
                        if 'a' <= char <= 'z':
                                    result += chr(ord(char) - 32)
                                            else:
                                                        result += char

                                                            return result

                                                            string = input("Enter a string: ")
                                                            print("Uppercase:", to_uppercase(string))