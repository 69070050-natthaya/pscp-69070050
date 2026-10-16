"""Shorten"""
nums = []
while True:
    number = int(input())
    if number == -1:
        break
    nums.append(number)

if not nums:
    print()
else:
    result = ""
    start = nums[0]
    last = nums[0]

    for n in nums[1:]:
        if n == last + 1:
            last = n
        else:
            if start == last:
                result = result + str(start) + ", "
            else:
                result = result + str(start) + "-" + str(last) + ", "
            start = n
            last = n

    if start == last:
        result = result + str(start)
    else:
        result = result + str(start) + "-" + str(last)

    print(result)
