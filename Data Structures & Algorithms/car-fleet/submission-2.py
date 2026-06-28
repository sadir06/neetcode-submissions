class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            arrival_time = (target - pos)/spd
            stack.append(arrival_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: # If it is faster or equal, it get's absorbed into the fleet ahead, and loses it's identity so we pop it
                stack.pop()
            # else:
            #   fleet size will increase by one beacuse the stack will gain a new term because we never popped anything. This means that we have an extra term that won't be touched in our list, as we only ever look at the last 2 terms, and that 3rd extra term is kept as it's separate fleet. Got that?? If not, we go into the above if condition, and we don't worry about that as it gets absorbed into the curernt fleet, so we do +1, do this check, and if it is true, we do -1, so fleet size stays the same. Got that?

        return len(stack)