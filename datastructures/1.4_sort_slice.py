# better performance than heapq for a large item selection
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
nums.sort()

# index -1 is equivalent to len(nums)-1
print nums[2:-1]
