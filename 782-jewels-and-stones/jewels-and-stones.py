class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for i in stones:
            if i in jewels:
                sum += 1
        return sum

                