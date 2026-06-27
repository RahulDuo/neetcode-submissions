class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dublicate = set()
        for num in nums:
            if num in dublicate:
                return True
            dublicate.add(num)
        return False
            
        