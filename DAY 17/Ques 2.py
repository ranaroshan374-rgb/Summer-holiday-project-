def union_sorted(arr1, arr2):
        arr1.sort()
            arr2.sort()
                union = []
                    i = j = 0

                        while i < len(arr1) and j < len(arr2):
                                # Skip duplicates in arr1
                                        if i > 0 and arr1[i] == arr1[i-1]:
                                                    i += 1
                                                                continue
                                                                        if arr1[i] < arr2[j]:
                                                                                    union.append(arr1[i])
                                                                                                i += 1
                                                                                                        elif arr1[i] > arr2[j]:
                                                                                                                    union.append(arr2[j])
                                                                                                                                j += 1
                                                                                                                                        else:                         # Equal elements
                                                                                                                                                    union.append(arr1[i])
                                                                                                                                                                i += 1
                                                                                                                                                                            j += 1

                                                                                                                                                                                # Add remaining from arr1
                                                                                                                                                                                    while i < len(arr1):
                                                                                                                                                                                            if i == 0 or arr1[i] != arr1[i-1]:
                                                                                                                                                                                                        union.append(arr1[i])
                                                                                                                                                                                                                i += 1

                                                                                                                                                                                                                    # Add remaining from arr2
                                                                                                                                                                                                                        while j < len(arr2):
                                                                                                                                                                                                                                if j == 0 or arr2[j] != arr2[j-1]:
                                                                                                                                                                                                                                            union.append(arr2[j])
                                                                                                                                                                                                                                                    j += 1

                                                                                                                                                                                                                                                        return union

                                                                                                                                                                                                                                                        arr1 = list(map(int, input("Enter first array : ").split()))
                                                                                                                                                                                                                                                        arr2 = list(map(int, input("Enter second array: ").split()))
                                                                                                                                                                                                                                                        print("Union:", union_sorted(arr1, arr2))