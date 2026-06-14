n = int(input("Enter number of rows: "))
for i in range(n):
        for j in range(i + 1):
                    print(chr(65 + i), end=" ")   # Row 0→A, Row 1→B...
                        print()