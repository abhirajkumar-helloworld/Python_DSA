nums = [5, 0, 2, 8, 1, 9, 2]
nums1 = []
sum = 0
n = len(nums)
largest = nums[0]
sec_largest = nums[0]
sorted_array = True
smallest = nums[0]
sec_smallest = nums[0]

for num in nums:
    sum = sum + num

    if num > largest:
        sec_largest = largest
        largest = num

    elif largest > num > sec_largest:
        sec_largest = num

    if num < smallest:
        sec_smallest = smallest
        smallest = num

    elif smallest < num < sec_smallest:
        sec_smallest = num

    if num not in nums1:
        nums1.append(num)

for i in range(len(nums) - 2):
    if nums[i] > nums[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("sorted")
else:
    print("not sorted")

for i in range(len(nums) - 1):
    if nums[i] == 0:
        nums.pop(i)
        nums.append(0)


print (f"Sum = {sum}")
print(f"Average = {sum/n}")
print(f"Second largest = {sec_largest}")
print(f"second smallest = {sec_smallest}")
print(f"nums = {nums}")
print(f"nums1 = {nums1}")