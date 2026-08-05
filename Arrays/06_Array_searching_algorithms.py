# Linear search

nums = [10, 25, 30, 45, 50]
target = 30
is_found = False

for i in range(len(nums)):
    if nums[i] == target:
        print(f"Found at index : {i}")
        is_found = True
        break

if not is_found:
    print("Not found")

# Count occurence

nums1 = [2, 5, 2, 7, 2, 9]
tar = 2
occurrences = 0

for num1 in nums1:
    if num1 == tar:
        occurrences += 1

print(f"Occurrences = {occurrences}")

# Minimum element

nums2 = [12, 5, 18, 2, 9]
minimum = nums2[0]
maximum = nums2[0]

for num2 in nums2:
    if num2 < minimum:
        minimum = num2

    if num2 > maximum:
        maximum = num2

print(f"Minimum = {minimum}")

# Maximum element 

print(f"Maximum = {maximum}")

# Binary search 

nums3 = [2, 5, 8, 12, 16, 20, 25]
t = 20
low = 0
high = len(nums3) - 1

while low <= high:

    mid = (low + high) // 2

    if nums3[mid] > t:
        high = mid - 1

    elif nums3[mid] < t:
        low = mid + 1

    else:
        print(f"Found at index {mid}")
        break

if low > high:
    print("Not Found")