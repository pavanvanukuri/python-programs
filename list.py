colourlist=["red","blue","purple","black"]
colourlist.append("green")
print(colourlist)

colourlist.remove("black")
print(colourlist)

colourlist.pop(2)

print(colourlist)

colourlist.sort()
print(colourlist)

colourlist.reverse()
print(colourlist)

colorli.copy(colourlist)
print(colorli)
print(colorlist.index("blue"))
print(colourlist.count("red"))


# Input
nums = list(map(int, input().split()))

# Ensure at least 20 numbers (as per question expectation)
# (In exams, they usually give input instead of random)

# Minimum
minimum = nums[0]
for num in nums:
    if num < minimum:
        minimum = num

# Maximum
maximum = nums[0]
for num in nums:
    if num > maximum:
        maximum = num

# Average
total = 0
for num in nums:
    total += num
average = total / len(nums)

# Even count
even_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1

# Output
print("Min:", minimum)
print("Max:", maximum)
print("Average:", average)
print("Even Count:", even_count)
