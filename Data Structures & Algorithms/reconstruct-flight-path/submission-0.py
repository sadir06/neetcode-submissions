class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        results = []
        hashMap = defaultdict(list)
        for source, dest in tickets:
            hashMap[source].append(dest)
        
        for airport in hashMap:
            hashMap[airport].sort(reverse=True) # Reverse it's destination list
        
        def dfs(airport):
            while hashMap[airport]:
                output = hashMap[airport].pop()
                dfs(output) # Keep searching as far as possible

            results.append(airport) # This appends the final airport that we need to take first

        dfs("JFK")
        results.reverse()
        return results
            