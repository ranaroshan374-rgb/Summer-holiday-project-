def find_pairs_full(arr, target):
        seen   = {}
            pairs  = []
                steps  = []

                    for i, num in enumerate(arr):
                            complement = target - num
                                    steps.append(
                                                f"num={num}, need={complement}, "
                                                            f"seen={set(seen.keys())}")
                                                                    if complement in seen:
                                                                                pairs.append({
                                                                                                "pair"     : (complement, num),
                                                                                                                "indices"  : (seen[complement], i),
                                                                                                                                "sum"      : complement + num
                                                                                                                                            })
                                                                                                                                                    if num not in seen:
                                                                                                                                                                seen[num] = i

                                                                                                                                                                    return pairs, steps

                                                                                                                                                                    arr    = list(map(int, input("Enter elements: ").split()))
                                                                                                                                                                    target = int(input("Enter target sum: "))
                                                                                                                                                                    pairs, steps = find_pairs_full(arr, target)

                                                                                                                                                                    print(f"\n{'─'*50}")
                                                                                                                                                                    print(f"  Array          : {arr}")
                                                                                                                                                                    print(f"  Target Sum     : {target}")
                                                                                                                                                                    print(f"\n  Step-by-step:")
                                                                                                                                                                    for step in steps:
                                                                                                                                                                        print(f"  → {step}")

                                                                                                                                                                        if pairs:
                                                                                                                                                                            print(f"\n  Pairs Found    : {len(pairs)}")
                                                                                                                                                                                for i, p in enumerate(pairs, 1):
                                                                                                                                                                                        a, b = p['pair']
                                                                                                                                                                                                x, y = p['indices']
                                                                                                                                                                                                        print(f"  Pair {i}         :"
                                                                                                                                                                                                                      f" {a} + {b} = {target}"
                                                                                                                                                                                                                                    f" (indices {x},{y})")
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        print(f"\n  No pairs found ❌")
                                                                                                                                                                                                                                        print(f"{'─'*50}")