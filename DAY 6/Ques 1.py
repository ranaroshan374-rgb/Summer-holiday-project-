def decimal_to_binary(n):
        """Convert a positive decimal integer to binary string manually."""
            if n == 0:
                    return "0"
                        if n < 0:
                                raise ValueError("Negative numbers not supported in this implementation.")
                                    
                                        binary = ""
                                            while n > 0:
                                                    binary = str(n % 2) + binary
                                                            n = n // 2
                                                                return binary


                                                                # Main program
                                                                if __name__ == "__main__":
                                                                    try:
                                                                            decimal = int(input("Enter a non-negative decimal number: "))
                                                                                    binary_manual = decimal_to_binary(decimal)
                                                                                            binary_builtin = bin(decimal)[2:]  # Python's built-in way
                                                                                                    
                                                                                                            print(f"Decimal {decimal} in binary (manual method): {binary_manual}")
                                                                                                                    print(f"Decimal {decimal} in binary (using bin()):   {binary_builtin}")
                                                                                                                            
                                                                                                                                    # Verification
                                                                                                                                            assert binary_manual == binary_builtin, "Conversion mismatch!"
                                                                                                                                                    
                                                                                                                                                        except ValueError:
                                                                                                                                                                print("Error: Please enter a valid integer.")
                                                                                                                                                                    except Exception as e:
                                                                                                                                                                            print(f"An error occurred: {e}")