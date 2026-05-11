class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed for each car
        # 2 cares will form a fleet if and only if the car ahead has time that is greater than or eaqual to the time of the car behind it

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) # Return the no of cars in the fleet fleet)