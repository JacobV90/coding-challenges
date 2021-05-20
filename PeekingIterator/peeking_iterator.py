class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        self.idx = -1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.idx != self.size - 1

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.idx += 1
        return self.nums[self.idx]

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.last_peek = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.last_peek:
            return self.last_peek
        self.last_peek = self.iterator.next()
        return self.last_peek
        
    def next(self):
        """
        :rtype: int
        """
        if self.last_peek:
            n = self.last_peek
            self.last_peek = None
            return n
        return self.iterator.next()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.last_peek:
            return True
        return self.iterator.hasNext()
        

if __name__ == "__main__":
  nums = [1,2,3,4,5,6,7]
  iter = PeekingIterator(Iterator(nums))
  while iter.hasNext():
      # Get the next element but not advance the iterator.
      print(f"peek val = {iter.peek()}")  
       # Should return the same value as [val].
      print(f"next val = {iter.next()}")        