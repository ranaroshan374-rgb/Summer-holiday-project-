def binary_to_decimal(binary):
        binary  = str(binary)
            decimal = 0
                power   = 0
                    for bit in reversed(binary):
                                if bit not in ('0', '1'):
                                                return "Invalid binary number"
                                                        decimal += int(bit) * (2 ** power)
                                                                power   += 1
                                                                    return decimal

                                                                    binary = input("Enter a binary number: ")
                                                                    print("Decimal =", binary_to_decimal(binary))