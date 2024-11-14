class MyCalendar:

    def __init__(self):
        self.l = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Handle empty list case
        if not self.l:
            self.l.append([startTime, endTime])
            return True
        
        # Check for insertion position and potential overlap
        left, right = 0, len(self.l)

        # In binary search implementations, using len(self.l) as the right pointer (rather than len(self.l) - 1) is a common approach in insertion problems. Here's why it's preferred in this context:

        # Inclusive vs. Exclusive Boundaries:
        # When using len(self.l) for the right pointer, we treat the range as [left, right) (right-exclusive). This setup ensures that left can move to the position where the new interval should be inserted without missing any index.
        # If we used len(self.l) - 1, we would need additional checks to handle cases where left lands just outside the actual list (e.g., at len(self.l)). It would also make handling insertion logic a bit more complex.
        # Simplifies the Insertion Process:
        # Using len(self.l) for right means that when left and right converge, left will be exactly at the position where the new event can be inserted without needing further adjustment.
        # This setup also avoids edge cases at the end of the list since we’re not required to add additional checks for left being at the list’s end.

        while left < right:
            mid = (left + right) // 2
            if self.l[mid][0] < startTime:
                left = mid + 1
            else:
                right = mid
        
        # Check overlap with previous event, if any
        if left > 0 and self.l[left - 1][1] > startTime:
            return False
        # Check overlap with next event, if any
        if left < len(self.l) and endTime > self.l[left][0]:
            return False
        
        # Insert the new event
        self.l.insert(left, [startTime, endTime])
        return True