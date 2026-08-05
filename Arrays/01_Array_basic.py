nums = [2, 4, 10, 12, 1, 19, 9, 20, 62, 30, 32]
largest = nums[0]
smallest = nums[0]
even = 0
odd = 0
n = 0
m = len(nums) - 1

for num in nums:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

while n < m:
    nums[n], nums[m] = nums[m], nums[n]
    n += 1
    m -= 1

print(f"Largest = {largest}")
print(f"Smallest = {smallest}")
print(f"Even = {even}")
print(f"Odd = {odd}")
print(f"nums = {nums}")