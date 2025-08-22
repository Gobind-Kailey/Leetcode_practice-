class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for numbers in nums:
            if numbers in hashset:
                return True
            hashset.add(numbers)
        return False
        
        # hashmap = {}

        # for num in nums:
        #     hashmap[num] = 1 + hashmap.get(num, 0)

        # for iterations in nums:
        #     if hashmap[iterations] > 1:
        #         return True
        # return False