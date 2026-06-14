n = int(input("Enter a number: "))
original = n
num_digits = len(str(n))    # Count digits
total = 0
while n > 0:
    digit = n % 10
        total += digit ** num_digits  # Raise to power of digit count
            n //= 10
            if total == original:
                print(f"{original} is an Armstrong number ✅")
                else:
                    print(f"{original} is NOT an Armstrong number ❌")