start = int(input("Enter start: "))
end   = int(input("Enter end: "))

print(f"Armstrong numbers between {start} and {end}:")
for n in range(start, end + 1):
    original  = n
        num_digits = len(str(n))
            total = 0
                temp  = n
                    while temp > 0:
                            digit = temp % 10
                                    total += digit ** num_digits
                                            temp //= 10
                                                if total == original:
                                                        print(n, end=" ")