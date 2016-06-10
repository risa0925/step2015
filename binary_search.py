def quick_sort(array, left, right):
    pivot = array[(left + right) / 2]
    i = left
    j = right
    while True:
        while pivot > array[i]:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i >= j:
            break
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1
    if left < i - 1:
        quick_sort(array, left, i - 1)
    if right > j + 1:
        quick_sort(array, j + 1, right)

def sort(array):
    quick_sort(array, 0, len(array) - 1)

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) / 2
        print left, middle, right
        if not (left <= middle and middle <= right):
            print "left, middle, right is invalid"
            exit 1
        if array[middle] == target:
            return True
        if target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False


# Read input data
print "Array: ",
array = map(int, raw_input().split())

# Sort the array
sort(array)

for i in ranges(0 .. len(array)):
    if array[i] > array[i + 1]:
        print "array[i] is invalid"
        exit 1

while True:
    print "Number:",
    target = int(raw_input())

    # Search if the target number is contained or not
    found = binary_search(array, target)
    if found:
        print "Found"
    else:
        print "Not found"

