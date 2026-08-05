nums = [12, 45, 7, 23, 89, 15]
target = 23
found = False

for i in range(len(nums)):
    if nums[i] == target:
        found = True
        print(f"Found at {i}")
        break

if not found:
    print("not found")

nums1 = [1, 2, 3, 2, 5, 2, 7]
tar = 2
freq = 0

for num1 in nums1:
    if num1 == tar:
        freq += 1

print(f"frequency = {freq}")

nums2 = [1, 2, 3, 5, 6]

for i in range(1, len(nums2)):
    if nums2[i - 1] == i:
        continue
    else :
        nums2.insert(i-1, i)

print(f"nums2 = {nums2}")

nums3 = [1, 2, 3, 4, 5]
nums3.append(nums3[0])
del nums3[0]
print(f"nums3 = {nums3}")

nums4 = [1, 2, 3, 4, 5]
nums4.insert(0, nums4[-1])
del nums4[-1]
print(f"nums4 = {nums4}")

# Challenge question :

nums5 = [2, 5, 7, 5, 1, 5, 9]
t = 5
firt_index = -1
last_index = -1

for i in range(len(nums5)):
    if nums5[i] == t:
        if firt_index == -1:
            firt_index = i
            last_index = i
        else:
            last_index = i

print(f"fist index = {firt_index}")
print(f"last index = {last_index}")