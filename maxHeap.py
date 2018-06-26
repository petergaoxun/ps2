import random
import math
from spyder.widgets.ipythonconsole.client import BLANK
class maxHeap:
    
    queue = []
    
    def __init__(self, feed =[]):
        self.queue = feed
    
    def swap_left(self,idx):
        tmp = self.queue[idx]
        self.queue[idx] = self.queue[2*idx+1]
        self.queue[2*idx+1] = tmp
        
        
    def swap_right(self,idx):
        tmp = self.queue[idx]
        self.queue[idx] = self.queue[2*idx+2]
        self.queue[2*idx+2] = tmp
    
    def maxHeapify(self, idx):
        #the max heap has one violation @ idx-th entry
        if(len(self.queue)-1 < (2*idx + 1)):
            return
        elif (len(self.queue)-1 == (2*idx +1)):
            if self.queue[2*idx+1]> self.queue[idx]:
                self.swap_left(idx)
            else:
                return
        else:
            if(self.queue[2*idx+1] > self.queue[2*idx+2]):
                self.swap_left(idx)
                self.maxHeapify(2*idx+1)
            else:
                self.swap_right(idx)
                self.maxHeapify(2*idx+2)
                
def heightHeap(nodeNum):
    return math.ceil(math.log((nodeNum+1),2))
    
def rdListGen(size = 10):
    ret =  []
    for x in range(size):
        ret.append(random.randint(0,100))
    return ret
    
def maxHeapify_Tester():
    tia = rdListGen()
    for x in range(len(tia), 0, -1):
        print(x)




                
def printHeap(domino = []):
    #domino is a heap, print as a tree
    height = heightHeap(len(domino))
    nodeCap = math.pow(2, height-1)
    width = nodeCap*6
    for x in range(height):
        if x != height-1 :
            nodeOnLv = math.pow(2, x)
            lvWid = width//nodeOnLv
            #as long as it's implemented as a BST, no residue to worry about
            stroller = []
            for tok in range(int(math.pow(2, math.floor(x)))):
                stroller.append(domino[int(math.pow(2, x)-1)+tok])
            ptNodes = printableNode(lvWid, stroller)
            for jin in ptNodes:
                print(jin, sep='', end='')
            print(" ")    
        else:
            #for last line, get number of elements left
            nodeOnLv = len(domino) - math.pow(2,x) + 1
            numSlots = math.pow(2, x)
            stroller = []
            for j in range(int (numSlots)):
                if j < nodeOnLv:
                     stroller.append(domino[(int)(math.pow(2,x))-1+j])
                else:
                    stroller.append(" ")
            ptNodes = printableNode(6, stroller)
            for jin in ptNodes:
                print(jin, sep='', end='')
            print(" ")
        
     
        
def printableNode(width, tray):
    ret = []    
    for tok in tray:
        blankLen = width - len(str(tok))
        frontLen = int (blankLen//2)
        backLen = int (blankLen - frontLen)
        ret.append(frontLen*" "+str(tok)+backLen*" ")
    return ret
        
def printHeapTester():
    pool = rdListGen()
    print(pool)
    print(" ")
    printHeap(pool)
        
        
def trial():
    for x in range(10):
        print(x)

def trial2():
    x = 25
    print(len(str(x)))

def trial3():
    beat = "b"
    beats = beat*0
    print(beats)

def trial5():
    beam = " "
    print(str(beam))
    print(len(str(beam)))
    print("ok")

def trial4():
    pool = ["alice","kuma","john"]
    for jim in pool:
        print(jim, sep='' , end ='')
    
#maxHeapify_Tester()
#printHeap()
#trial5()

printHeapTester()