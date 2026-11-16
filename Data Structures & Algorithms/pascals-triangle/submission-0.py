class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        """
        We are gievn an integer n and we return the first n rows of pascals triangle as a list of lists, where each sublist is one layer, in order. OK, the way that it works is that it is always padded with 0s, each layer aside from the first is padded with 0s. Each layer always have 1 more element than the one above it, so the length of each sublist increases by 1. We pad the left and right by 1, but the way the interals work are intersting, beacuse we need to form the new layer by doing additions from the previous layer. One way we could do this is by just calculating each new layer by hand, by using the previous layer, padding the start and end with 0s, adn then figuring out the middle terms by using a sliding window across the previous list, however, this feels really slow as each layer will have to use the layer previously and go through the entire thing. Instead we could use something like.. HOnestly I don't see a better way to do it, let's try that. Where left and right are always set to 0, 1, and end when right == len(sublist) - 1
        """
        output = []
        for i in range(numRows): # We create this many outputs
            if i == 0:
                output.append([1])
                continue
            temp = [1] # Always pad with a starting 0, and at the end with an ending 0
            prev = output[-1]
            left, right = 0, 1
            while right < len(prev):
                temp.append(prev[left] + prev[right])
                left += 1
                right += 1
            temp.append(1)
            output.append(temp[:]) # This work beacuse temp is just a list of ints
        return output
        