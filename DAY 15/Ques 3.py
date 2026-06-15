from collections import deque

def rotate_right_full(arr, k):
    n        = len(arr)
        k        = k % n
            original = arr.copy()
                rotated  = arr[-k:] + arr[:-k]
                    return original, rotated, k

                    arr      = list(map(int, input("Enter elements: ").split()))
                    k        = int(input("Enter positions to rotate right: "))
                    orig, rot, effective_k = rotate_right_full(arr, k)

                    print(f"\n{'─'*45}")
                    print(f"  Original Array    : {orig}")
                    print(f"  Rotate Right By   : {k}")
                    print(f"  Effective Rotate  : {effective_k} (k%n)")
                    print(f"  Rotated Array     : {rot}")
                    print(f"  Last {effective_k} moved to front : {orig[-effective_k:]}")
                    print(f"{'─'*45}")