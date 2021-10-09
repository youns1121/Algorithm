#카데인 알고리즘

def solution(nums):
    a_max = b_max = nums[0]
    for nums in nums[1:]:
        a_max = max(nums, a_max + nums)
        b_max = max(a_max, b_max)
    return b_max


nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

if (len(nums) > 0 and 1000000 >= len(nums)):
    print(solution(nums))