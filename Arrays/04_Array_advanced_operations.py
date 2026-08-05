nums = [1, 2, 3, 4, 5]
n = 0
m = len(nums) - 1

while n < m:
    nums[n], nums[m] = nums[m], nums[n]
    n += 1
    m -= 1

print(f"nums = {nums}")

nums1 = [1, 2, 3, 2, 1]
a = 0
b = len(nums1) - 1 
is_palindrome = True

while a < b:
    if nums1[a] != nums1[b]:
        print("not palindrome")
        is_palindrome = False
        break
    a += 1
    b -= 1

if is_palindrome:
    print("palindrome")

nums2 = [1, 1, 0, 1, 1, 1]
current = 0
maximum = 0

for num2 in nums2:
    if num2 == 1:
        current += 1
        if current > maximum:
            maximum = current
    else:
        current = 0

print(f"Maximum consicutive of 1s : {maximum}")

a = [1, 2, 3]
b = [2, 3, 4]
union = []

for c in b:
    if c not in a:
        a.append(c)

for num in a:
    if num not in union:
        union.append(num)

print(f"Union : {union}")

c = [1, 2, 3, 2]
d = [2, 3, 4, 2]
intersection = []
i = []

for e in c:
    if e in d:
        intersection.append(e)

for num in intersection:
    if num not in i:
        i.append(num)

print(f"Intersection : {i}")

# Challenge question

nums3 = [2, 7, 11, 15]
target = 9

for i, num3 in enumerate(nums3):
    for j in range(i + 1, len(nums3)):
        if num3 + nums3[j] == target:
            print(f"Indices : {i}, {j}")
            break