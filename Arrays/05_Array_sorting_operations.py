nums = [5, 3, 8, 2, 1, 6]

# outter loop = no. of passes
# inner loop = compare adjacent elements

for pass_numder in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(f"nums = {nums}")

nums1 = [5, 3, 8, 2]
smallest_index = 0
for pass_no in range(len(nums1) - 1):
    for i in range(pass_no + 1, len(nums1)):
        if nums1[i] < nums1[smallest_index]:
            smallest_index = i

    nums1[smallest_index], nums1[0] = nums1[0], nums1[smallest_index]

print(f"nums1 = {nums1}")

# Insertion sort

nums2 = [8, 5, 3]
for i in range(1, len(nums2)):
    j = i - 1
    key = nums2[i]
    while j >= 0 and nums2[j] > key:
        nums2[j + 1] = nums2[j]
        j -= 1
        nums2[j + 1] = key


print(f"nums2 = {nums2}")

# challenge question

nums3 = [7, 2, 9, 1, 5]

for pass_numder in range(len(nums3) - 1):
    for i in range(len(nums3) - 1):
        if nums3[i] > nums3[i + 1]:
            nums3[i], nums3[i + 1] = nums3[i + 1], nums3[i]

print(f"nums3 = {nums3}")

# bonus challenge

print(f"third largest = {nums3[len(nums3) - 3]}")