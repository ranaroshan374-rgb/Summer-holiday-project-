def string_length(s):
        count = 0
            for _ in s:
                    count += 1
                        return count

                        def count_words(s):
                            return len(s.split())

                            def count_vowels(s):
                                return sum(1 for c in s
                                               if c.lower() in 'aeiou')

                                               def count_consonants(s):
                                                   return sum(1 for c in s
                                                                  if c.isalpha() and
                                                                                 c.lower() not in 'aeiou')

                                                                                 s = input("Enter a string: ")

                                                                                 print(f"\n{'─'*40}")
                                                                                 print(f"  String       : '{s}'")
                                                                                 print(f"  Length       : {string_length(s)}")
                                                                                 print(f"  Words        : {count_words(s)}")
                                                                                 print(f"  Vowels       : {count_vowels(s)}")
                                                                                 print(f"  Consonants   : {count_consonants(s)}")
                                                                                 print(f"  Spaces       : {s.count(' ')}")
                                                                                 print(f"  Digits       : {sum(1 for c in s if c.isdigit())}")
                                                                                 print(f"  Special      : {sum(1 for c in s if not c.isalnum() and c != ' ')}")
                                                                                 print(f"{'─'*40}")