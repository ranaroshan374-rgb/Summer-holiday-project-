from collections import Counter

def remove_duplicates_full(arr):
    original   = arr.copy()
        freq       = Counter(arr)
            duplicates = {k: v for k, v in freq.items() if v > 1}
                seen       = set()
                    result     = []

                        for num in arr:
                                if num not in seen:
                                            result.append(num)
                                                        seen.add(num)

                                                            return {
                                                                    "original"        : original,
                                                                            "result"          : result,
                                                                                    "duplicates"      : duplicates,
                                                                                            "removed_count"   : len(original) - len(result),
                                                                                                    "unique_count"    : len(result)
                                                                                                        }

                                                                                                        arr  = list(map(int, input("Enter elements: ").split()))
                                                                                                        info = remove_duplicates_full(arr)

                                                                                                        print(f"\n{'─'*50}")
                                                                                                        print(f"  Original Array    : {info['original']}")
                                                                                                        print(f"  After Removing    : {info['result']}")
                                                                                                        print(f"  Duplicates Found  : {info['duplicates']}")
                                                                                                        print(f"  Elements Removed  : {info['removed_count']}")
                                                                                                        print(f"  Unique Elements   : {info['unique_count']}")
                                                                                                        print(f"{'─'*50}")