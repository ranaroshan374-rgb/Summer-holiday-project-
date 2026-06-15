def find_missing(arr):
        n            = len(arr) + 1
            expected_sum = n * (n + 1) // 2
                actual_sum   = sum(arr)
                    return expected_sum - actual_sum

                    arr = list(map(int, input("Enter elements (1 to N with one missing): ").split()))
                    print("Missing number =", find_missing(arr))