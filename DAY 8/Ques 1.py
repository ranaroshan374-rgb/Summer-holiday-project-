def half_pyramid(n):
        for i in range(1, n + 1):
                    print("* " * i)

                    n = int(input("Enter number of rows: "))
                    half_pyramid(n)