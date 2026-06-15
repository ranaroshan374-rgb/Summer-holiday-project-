from collections import Counter

def array_intersection_full(arr1, arr2):
    set1         = set(arr1)
        set2         = set(arr2)

            # All set operations
                intersection = sorted(set1 & set2)
                    union        = sorted(set1 | set2)
                        only_arr1    = sorted(set1 - set2)
                            only_arr2    = sorted(set2 - set1)
                                sym_diff     = sorted(set1 ^ set2)

                                    # With duplicates using Counter
                                        freq1        = Counter(arr1)
                                            freq2        = Counter(arr2)
                                                inter_dup    = sorted((freq1 & freq2).elements())

                                                    return {
                                                            "arr1"          : arr1,
                                                                    "arr2"          : arr2,
                                                                            "intersection"  : intersection,
                                                                                    "union"         : union,
                                                                                            "only_in_arr1"  : only_arr1,
                                                                                                    "only_in_arr2"  : only_arr2,
                                                                                                            "sym_diff"      : sym_diff,
                                                                                                                    "inter_dup"     : inter_dup,
                                                                                                                            "inter_size"    : len(intersection)
                                                                                                                                }

                                                                                                                                arr1   = list(map(int, input("Enter first array : ").split()))
                                                                                                                                arr2   = list(map(int, input("Enter second array: ").split()))
                                                                                                                                result = array_intersection_full(arr1, arr2)

                                                                                                                                print(f"\n{'─'*52}")
                                                                                                                                print(f"  Array 1                : {result['arr1']}")
                                                                                                                                print(f"  Array 2                : {result['arr2']}")
                                                                                                                                print(f"  Intersection (unique)  : {result['intersection']}")
                                                                                                                                print(f"  Intersection (with dup): {result['inter_dup']}")
                                                                                                                                print(f"  Union                  : {result['union']}")
                                                                                                                                print(f"  Only in Array 1        : {result['only_in_arr1']}")
                                                                                                                                print(f"  Only in Array 2        : {result['only_in_arr2']}")
                                                                                                                                print(f"  Symmetric Difference   : {result['sym_diff']}")
                                                                                                                                print(f"  Intersection Size      : {result['inter_size']}")
                                                                                                                                print(f"{'─'*52}")