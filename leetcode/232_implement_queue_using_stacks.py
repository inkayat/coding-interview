from collections import deque

class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None
        
    def pop(self) -> int:
        x = self.queue.popleft()
        return x
            
    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
