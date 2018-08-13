def Kadane(nums):
    cur_max = 0
    final_max = -1000
    length = len(nums)
    for i in range(length):
        cur_max = cur_max + nums[i]
        final_max = max(cur_max, final_max)
        if cur_max < 0:
            cur_max = 0
    return final_max
print Kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])

    
