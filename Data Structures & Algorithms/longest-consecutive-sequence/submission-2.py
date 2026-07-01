class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(tuple(nums))
        max_seq = 0
        seq_len = 1
        for num in nums:
            if num-1 not in sett:
                for i in range(1,len(nums)):
                    if num+i in sett:
                        seq_len += 1
                    else:
                        break 
            if seq_len > max_seq:
                max_seq = seq_len
            seq_len = 1       


        return max_seq
        