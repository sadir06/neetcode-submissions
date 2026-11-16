import heapq as hq

class SeatManager:
    """
    We need to design a system that manages the reservation state of n seats that are numbered form 1 to n. The init just sets an object that will manage n seats from 1 to n. All are avaiable initially. 
    reserve() fetches the smallest numbered unreserved seat, reserves it, and returns its numbers. Unservseve unserseves the seat with the given seat number. 10^5 seats max. For each call to reserve, it is guaranteed that there will be atleast one seat free. We can do a simple min heap solution with lazy deletion. We can always find the seat that is the smallest that is unreserved and add it. However, we have to make sure that when we unreserve a seat, we check in some data structure that it is actually free or not, and based on that, whiel this is not true, we pop from the heap during reserve, this is lazy deletion. Let's implement it with a heapq and a simple list. 
    """

    def __init__(self, n: int):
        self.smallest = []
        self.next_seat = 1

    def reserve(self) -> int:
        if self.smallest:
            top = hq.heappop(self.smallest)
            return top
        else:
            seat = self.next_seat
            self.next_seat += 1
            return seat 

    def unreserve(self, seatNumber: int) -> None:
        hq.heappush(self.smallest, seatNumber)
        return
        
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)