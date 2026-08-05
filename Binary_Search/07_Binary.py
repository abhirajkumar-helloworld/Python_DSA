nums = [2, 4, 4, 4, 7, 9, 11, 11, 15]
target = 4
low = 0
high = len(nums) - 1
first_occurence = -1
last_occurence = -1

while low <= high:
    mid = (low + high) // 2
# first occurence

    if nums[mid] > target:
        high = mid - 1

    elif nums[mid] < target:
        low = mid + 1

    elif nums[mid] == target:
        first_occurence = mid
        high = mid - 1

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] > target:
        high = mid - 1

    elif nums[mid] < target:
        low = mid + 1

    elif nums[mid] == target:
        last_occurence = mid
        low = mid + 1

if first_occurence == -1:
    print("Not Found")
else:
    print(f"fist occurence = {first_occurence}")
    print(f"last occurence = {last_occurence}")