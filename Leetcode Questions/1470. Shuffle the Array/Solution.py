class Solution(object):
    def shuffle(self, nums, n):
        new_list = []
        
        for index in range(0, n):
            new_list.append(nums[index])
            new_list.append(nums[index + n])
            
        return new_list