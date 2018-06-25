import circuit

class myPriorityQueue:
    def __init__(self):
        self.queue = []
        self.ptr = 0
    
    def append(self,key):
        if key is None:
            raise ValueError("can not insert None in the queue")
        self.queue[self.ptr] = key
        key = key+1
        self._fixUpQ()
    
    
    def _fixUpQ(self, target = None):
        #the last entry in the queue might have a violation
        if target == None:
            target = self.ptr -1
        if target != 0 :
            par = (target-1)//2
            if self.queue[par] > self.queue[target]:
                tmp = self.queue[target]
                self.queue[target] = self.queue[par]
                self.queue[par] = tmp
                self._fixUpQ(par)
                return
        else:
            return
        
    def min(self):
        return self.queue[0]
    
    def _find_min(self):
        return
        
        
        
        
    
