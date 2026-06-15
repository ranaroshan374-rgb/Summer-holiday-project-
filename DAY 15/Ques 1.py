def reverse_array(arr):
        n     = len(arr)
            left  = 0
                right = n - 1
                    steps = []

                        while left < right:
                                steps.append(f"Swap index {left} ({arr[left]}) "
                                                     f"↔ index {right} ({arr[right]})")
                                                             arr[left], arr[right] = arr[right], arr[left]
                                                                     left  += 1
                                                                             right -= 1

                                                                                 return arr, steps

                                                                                 arr          = list(map(int, input("Enter elements: ").split()))
                                                                                 original     = arr.copy()
                                                                                 reversed_arr, steps = reverse_array(arr)

                                                                                 print(f"\n{'─'*40}")
                                                                                 print(f"  Original  : {original}")
                                                                                 for step in steps:
                                                                                     print(f"  Step      : {step}")
                                                                                     print(f"  Reversed  : {reversed_arr}")
                                                                                     print(f"{'─'*40}")