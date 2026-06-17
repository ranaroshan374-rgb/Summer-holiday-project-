s    = input("Enter a string: ")
freq = [0] * 256

for ch in s:
    freq[ord(ch)] += 1

    found = False
    for ch in s:
        if freq[ord(ch)] == 1:
                print(f"First non-repeating: '{ch}' ✅")
                        found = True
                                break

                                if not found:
                                    print("No non-repeating character ❌")