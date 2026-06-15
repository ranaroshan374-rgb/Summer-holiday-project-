arr1 = list(map(int, input("Enter first array elements: ").split()))
arr2 = list(map(int, input("Enter second array elements: ").split()))

common = []

for element in arr1:
    if element in arr2 and element not in common:
            common.append(element)

            print("Common elements are:", common)