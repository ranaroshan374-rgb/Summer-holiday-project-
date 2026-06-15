def move_zeros_to_end(arr):
        pos = 0                         # Tracks next non-zero slot

            # Pass 1: Move all non-zeros forward
                for i in range(len(arr)):
                        if arr[i] != 0:
                                    arr[pos] = arr[i]
                                                pos += 1

                                                    # Pass 2: Fill rest with zeros
                                                        for i in range(pos, len(arr)):
                                                                arr[i] = 0

                                                                    return arr

                                                                    arr = list(map(int, input("Enter elements: ").split()))
                                                                    print("After moving zeros:", move_zeros_to_end(arr))