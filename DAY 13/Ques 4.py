n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
        element = int(input("Enter element: "))
            arr.append(element)

            even_count = 0
            odd_count = 0

            for num in arr:
                    if num % 2 == 0:
                                even_count += 1
                                    else:
                                                odd_count += 1

                                                print("Number of even elements =", even_count)
                                                print("Number of odd elements =", odd_count)