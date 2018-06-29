import circuit
import math
from maxHeap import rdListGen,printHeap,printableNode

class myPriorityQueue:

    def height(self):
        nodeNum = len(self.queue)
        rawHeight = math.log(nodeNum+1,2)
        acutal = math.ceil(rawHeight)
        return acutal
    
    def delete(self,idx=0):
        if len(self.queue) != 1:
            tok = self.queue.pop()
            self.queue[idx] = tok
            self.minHeapify(idx)
        else:
            self.queue = []
        return

    def parDx(self,idx):
        return (idx-1)//2

    def __init__(self, dome=[]):
            self.queue = dome
            if len(dome) == 0:
                return
            else:
                #proc raw list from max_idx non-leaf node to root
                capIdx = (int) (math.pow(2,self.height()-1) - 1)
                for j in range(capIdx,-1,-1):
                    self.minHeapify(j)

    def minHeapify(self,idx):
        #assume the queue[idx] is the only node with violation
        if((len(self.queue)-1) < (2*idx+1)):
            return
        elif ((len(self.queue)-1) == (2*idx+1)):
            if self.queue[2*idx+1]> self.queue[idx]:
                    self.swap_left(idx)
            else:
                return
        else:
            if(self.queue[2*idx+1] >= self.queue[2*idx+2])and(self.queue[2*idx+1]<self.queue[idx]):
                self.swap_right(idx)
                self.minHeapify(2*idx+2)
            elif(self.queue[2*idx+1] < self.queue[2*idx+2])and(self.queue[2*idx+2]<self.queue[idx]):
                self.swap_left(idx)
                self.minHeapify(2*idx+1)
            

    def swap_left(self,idx):
        tmp = self.queue[idx]
        self.queue[idx] = self.queue[2*idx+1]
        self.queue[2*idx+1] = tmp
        
        
    def swap_right(self,idx):
        tmp = self.queue[idx]
        self.queue[idx] = self.queue[2*idx+2]
        self.queue[2*idx+2] = tmp

    def insert(self,key):
        self.queue.append(key)
        if len(self.queue) != 1:
            self.upFix(len(self.queue)-1)
        return

    def upFix(self,idx):
        if idx != 0:
            if self.queue[idx] < self.queue[self.parDx(idx)]:
                self.queue[idx],self.queue[self.parDx(idx)] = self.queue[self.parDx(idx)],self.queue[idx]
                self.upFix(self.parDx(idx))
        return

def insertionTester():
    pool = rdListGen()
    hotPot = myPriorityQueue([])
    for ele in pool:
        hotPot.insert(ele)
    printHeap(hotPot.queue)


def buildHeapTester():
    lind = rdListGen(20)
    print(lind)
    alice = myPriorityQueue(lind)
    printHeap(alice.queue)

def deletionTester():
    pool = rdListGen()
    hotPot = myPriorityQueue([])
    for ele in pool:
        hotPot.insert(ele)
    printHeap(hotPot.queue)
    hotPot.delete()
    printHeap(hotPot.queue)
    print("DONE")

if __name__ == "__main__":
    #buildHeapTester()
    #insertionTester()
    deletionTester()