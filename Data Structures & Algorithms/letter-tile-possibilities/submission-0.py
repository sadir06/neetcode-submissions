class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Each character in tiles labels a separate tile. From nonempty strings by selecting and ordering some of the tiles, using each tile at most once. Return the number of distict strings you can form. Tiles with the same letter do not make otherwise idential strings different. E.g, given "AB", you can form "A", "B", "AB", "BA". From "AAA", you can make "A", "AA", "AAA". Otherwise they are the same. I think the best way to do this is to create a set. So even if we decide to go through all the different combinations, this will be fine, because we will have the set accounting for our repretitions, and at the end we just return the length of the set. The way we can do this is very simple, imagine going through the set of tiles, and doing a for loop through them. We can choose each one at most once, so we can go through it and either choose it or not choose it, and then we immediately move onto the next one. One problem thtough is the ordering. How can we ever get B, A? Hmm, well for that to happen, we need to choose B first and then pick A and not B. We have to make sure that the length of the curr string is max len(tiles). Hmm, then the for loop can make the choice for us, and all choices will be made, as we will first not pick A, pick B, and then pick A and we will have length 2, and we have to immediately return. However, even shorter ones can be strings, so what is the base case to return, it cannot be that len(curr) == len(tiles)? Honestly not sure. 
        """
        final_set = set()
        visiting = set()
        curr_string = ""
        def dfs():
            nonlocal curr_string 
            
            for j in range(len(tiles)):
                if j in visiting:
                    continue # This index has already been chosen down this path.
                visiting.add(j)
                curr_string += tiles[j]
                final_set.add(curr_string)
                dfs()
                visiting.remove(j)
                curr_string = curr_string[:-1]

            return
        dfs()
        return len(final_set)