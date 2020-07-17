class RingBuffer:
    """ Ring buffer, not full state"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        
    def append(self, x):
        # append x in ringbuffer until reaching capacity
        self.data.append(x)
        # reach capacity once the ring buffer is full
        if len(self.data) == self.capacity:
            # self.cur is the index that will be overwritten
            # when buffer is full, reset self.cur to 0
            self.cur = 0
            # change self class to full:
            self.__class__ =  self.__Full             
         
    def get(self):
        return self.data 

    class __Full:
        """Class implements a full butter"""
        def append(self, x):
            #add x, overwrite the oldest (index = self.cur) in the buffer
            self.data[self.cur] = x
            # update index with remainder of x/y
            self.cur = (self.cur + 1 ) % self.capacity
            #print(f"overwrite index: {self.cur}")

        def get(self):
            return self.data

