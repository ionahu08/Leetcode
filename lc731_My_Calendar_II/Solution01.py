class MyCalendarTwo:

    def __init__(self):
        self.l = list()
        self.o = list()

    def book(self, startTime: int, endTime: int) -> bool:
        for os, oe in self.o:
            if startTime < oe and endTime > os:
                return False

        for ls, le in self.l:
            if startTime < le and endTime > ls:
                self.o.append([max(ls, startTime), min(le, endTime)])
            
        self.l.append((startTime, endTime))
        return True
            


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)