class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
         if len(jewels) == 0 or len(stones) == 0:
            return 0
        stones = [stone for stone in stones]
        if len(jewels) == 1:
            if jewels[0] not in stones:
                return 0
        ans = 0
        for el in jewels:
            if el not in stones:
                continue
            else:
                for nl in stones:
                    if el == nl:
                        ans+=1
    #2nd method
        for el in jewels:
            ans += stones.count(el)
        return ans
    #3rd method
        jewels = set(jewels)
        count = 0
        
        for char in stones:
            if char in jewels:
                count += 1
        
        return count
       
    