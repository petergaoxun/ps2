import circuit


def totB():
    global inmmaBox 
    inmmaBox = 55
    inmmaBox = 88
    

    
class bucky:
    somePub = "this isn't mean to change"
    
    def __init__(self):
        print("bucky init")
        __someTrick__ = "passcode"
    
    def changePasscode(self, argString):
        self.__someTrick__ = argString
        
    def prtPsc(self):
        print(self.__someTrick__)
    
    def forge(self):
        print("argentina")
        
class bunker:
    #the default color is black, if a two ball has same weight than white
    #is bigger than black one
    def __init__(self, weight=5, blk = True):
        self.pound = weight
        self.black = blk
    
    def __lt__(self, blonde):
        print("inside less than")
        if (self.pound < blonde.pound) or (self.pound == blonde.pound and self.black and (not blonde.black)):
            return True; 
        else:
            return False;
    
    def __gt__(self,blonde):
        print("inside __gt__")
        if(self.pound > blonde.pound) or  (self.pound == blonde.pound and not self.black and blonde.black):
            return True
        else:
            return False
    
def richTests():
    jim = bunker(6, True)
    alice = bunker(5,False)
    print(jim<alice)
    print(jim>alice)
    
def baseTest():
    print(5//2)
    
    
    
if __name__ == "__main__":
    baseTest()
    
    