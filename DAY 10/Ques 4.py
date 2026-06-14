def char_pyramid(n):
        for i in range(1, n + 1):
                    # Build left half
                            left  = "".join(chr(65 + j) for j in range(i))
                                    # Mirror for right half (exclude last char)
                                            right = left[-2::-1]
                                                    row   = left + right
                                                            print(" " * (n - i) + row)

                                                            n = int(input("Enter number of rows: "))
                                                            char_pyramid(n)