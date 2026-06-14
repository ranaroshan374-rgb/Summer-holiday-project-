n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
        element = int(input("Enter element: "))
            arr.append(element)

            largest = arr[0]
            smallest = arr[0]

            for num in arr:
                    if num > largest:
                                largest = num
                                    if num < smallest:
                                                smallest = num

                                                print("Largest element =", largest)
                                                print("Smallest element =", smallest)