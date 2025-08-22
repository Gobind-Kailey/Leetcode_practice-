class Solution(object):
    def isAnagram(self, s, t):
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for char in countS:
        #     if countS[char] != countT.get(char,0):
        #         return False
        # return True

        if len(s) != len(t): return False
        
        hashmap1 = {}
        hashmap2 = {}
        for letter in s:
            hashmap1[letter] = 1 + hashmap1.get(letter, 0)

        for letter in t:
            hashmap2[letter] = 1 + hashmap2.get(letter, 0)

        for letter in s:
            if hashmap1[letter] != hashmap2.get(letter, 0):
                return False

        return True 
        