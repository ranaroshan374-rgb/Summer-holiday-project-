def max_frequency_element(arr):
        if not arr:
                return None, 0

                    freq     = {}
                        for num in arr:
                                freq[num] = freq.get(num, 0) + 1

                                    max_freq    = max(freq.values())
                                        max_element = max(freq, key=freq.get)
                                            all_max     = [k for k, v in freq.items()
                                                               if v == max_freq]

                                                                   return max_element, max_freq, all_max, freq

                                                                   arr = list(map(int, input("Enter elements: ").split()))
                                                                   element, count, all_max, freq = max_frequency_element(arr)

                                                                   print(f"Max frequency element : {element}")
                                                                   print(f"Frequency             : {count}")
                                                                   if len(all_max) > 1:
                                                                       print(f"All max freq elements : {all_max}")