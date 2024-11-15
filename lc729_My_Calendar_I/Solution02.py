class MyCalendar:
    def __init__(self):
        self.l = list()

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.l:
            self.l.append([startTime, endTime])
            return True

        if self.l[-1][0] < startTime:
            if self.l[-1][1] <= startTime:
                self.l.append([startTime, endTime])
                return True
            else:
                return False


        left, right = 0, len(self.l)-1
        while left < right:
            mid = (left+right)//2
            if self.l[mid][0] < startTime:
                left = mid + 1
            else:
                right = mid

        if left > 0 and startTime < self.l[left-1][1]:
            return False
        if endTime > self.l[left][0]:
            return False
        self.l.insert(left, [startTime, endTime])
        return True

            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)