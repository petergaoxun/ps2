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
    
    def left_swap(self, csr):
       #swap entry in csr w/ csr's left child
       tmp = self.queue[csr]
       self.queue[csr] = self.queue[2*csr+1]
       
       
    def min(self):
        return self.queue[0]
    
    def _find_min(self):
        return 0
    
    
    def _pop_remove(self):
        #get rid of the first entry in the list
        csr = 0
        while(2*csr+1 <= self.ptr):
            if(ptr == 2*csr +1):
                if(self.queue[csr]>self.queue[2*csr+1]):
                    
            if(self.queue[2*csr+1]<self.queue[2*csr+2]):
                self[csr]
        
    
    
    
    def pop(self):
        ret = self.queue[0]
        self._pop_remove()
        
        
        
        
    
