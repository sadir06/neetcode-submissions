class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = "" # We will slowly add the letters to the string
        count = {
            "a" : a, 
            "b" : b, 
            "c" : c, 
        }
        max_heap = [(-cnt, char) for char, cnt in count.items() if cnt != 0]
        heapq.heapify(max_heap)

        while max_heap:
            cnt, char = heapq.heappop(max_heap) # gives us the most frequent value
            if len(res) >= 2 and res[-1] == res[-2] == char:
                store = (cnt, char)
                if max_heap:
                    cnt2, char2 = heapq.heappop(max_heap)
                    res += char2 # has to be different
                    cnt2 += 1
                    if cnt2 != 0:
                        heapq.heappush(max_heap, (cnt2, char2))
                    heapq.heappush(max_heap, (cnt, char)) # Add these back, they are legal again
                else:
                    break # this is the longest possible one
            else:     
                res += char # Add the most frequent value onto the string
                cnt += 1
                if cnt != 0:
                    heapq.heappush(max_heap, (cnt, char))
        
        return res
            

            

     
        