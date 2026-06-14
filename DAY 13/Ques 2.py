n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
        element = int(input("Enter element: "))
            arr.append(element)

            total = sum(arr)
            average = total / n

            print("Sum =", total)
            print("Average =", average)