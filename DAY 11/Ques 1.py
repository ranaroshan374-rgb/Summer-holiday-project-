def sum_two(a, b):
        if not isinstance(a, (int, float)):
                    raise TypeError("a must be a number")
                        if not isinstance(b, (int, float)):
                                    raise TypeError("b must be a number")
                                        return a + b

                                        try:
                                                a = float(input("Enter first number: "))
                                                    b = float(input("Enter second number: "))
                                                        print("Sum =", sum_two(a, b))
                                                        except ValueError:
                                                                print("Invalid input! Please enter numbers only.")
                                                                except TypeError as e:
                                                                        print("Error:", e)