class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = [i]
            else:
                num_dict[num].append(i)
        for i, num in enumerate(nums):
            if target - num in num_dict:
                if target - num == num:
                    if len(num_dict[num]) > 1:
                        return [num_dict[num][0], num_dict[num][1]]
                else:
                    return [i, num_dict[target - num][0]]