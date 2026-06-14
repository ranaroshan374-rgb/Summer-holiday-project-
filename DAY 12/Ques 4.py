def is_perfect(num):
        sum_divisors = 0

            for i in range(1, num):
                        if num % i == 0:
                                        sum_divisors += i

                                            return sum_divisors == num

                                            num = int(input("Enter a number: "))

                                            if is_perfect(num):
                                                    print(num, "is a Perfect Number")
                                                    else:
                                                            print(num, "is not a Perfect Number")