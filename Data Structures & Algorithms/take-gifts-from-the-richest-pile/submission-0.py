import math # for math.floor
import heapq as hq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        We have an integer array gifts showing the number of gifts in various piles. Each second, we choose the pile with the max number of gits, and if there is more than one pile we choose any, adn then we reduce the number of gifts in the pile to the floor of the square root of the oriignal number of gifts in the pile. Return the number of gits remaining after k seconds. Very easy, a nice warmup quesiton. We can just use a max heap, honestly no more needs to be said, let's just implement it. 
        """
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
            
        hq.heapify(gifts) # Should be O(nlogn)

        while gifts and k > 0:
            temp = -hq.heappop(gifts)
            temp = math.floor(math.sqrt(temp))
            hq.heappush(gifts, -temp)
            k -= 1
        total_gifts = 0
        print(gifts)
        for gift in gifts:
            total_gifts += gift
        return -total_gifts

