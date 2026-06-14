def is_armstrong(num):
        order = len(str(num))
            total = 0
                temp = num

                    while temp > 0:
                                digit = temp % 10
                                        total += digit ** order
                                                temp //= 10

                                                    return total == num

                                                    num = int(input("Enter a number: "))

                                                    if is_armstrong(num):
                                                            print(num, "is an Armstrong Number")
                                                            else:
                                                                    print(num, "is not an Armstrong Number")