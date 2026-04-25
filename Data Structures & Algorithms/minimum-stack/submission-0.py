class MinStack:
    def __init__(self):
        self.d = deque()
        self.l = []
        
        
        

    def push(self, val: int) -> None:
        heapq.heappush(self.l,val)

            
        self.d.append(val)


        

    def pop(self) -> None:
        x = self.d.pop()
        self.l.remove(x)

        

    def top(self) -> int:
        if(len(self.d)==0):
            return -1
        return self.d[-1]
        

    def getMin(self) -> int:
        return min(self.l)
        
