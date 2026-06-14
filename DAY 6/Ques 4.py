def fast_power(x, n):
        if n == 0:
                    return 1
                        if n < 0:
                                    return 1 / fast_power(x, -n)
                                        if n % 2 == 0:
                                                    half = fast_power(x, n // 2)
                                                            return half * half          # Even: x^n = (x^n/2)²
                                                                return x * fast_power(x, n - 1) # Odd:  x^n = x * x^(n-1)

                                                                x = int(input("Enter base (x): "))
                                                                n = int(input("Enter exponent (n): "))
                                                                print(f"{x}^{n} =", fast_power(x, n))