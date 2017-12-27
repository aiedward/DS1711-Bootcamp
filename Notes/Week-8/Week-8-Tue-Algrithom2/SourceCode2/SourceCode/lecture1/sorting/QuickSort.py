from util.ArrayUtil import ArrayUtil

class QuickSort:
    
    def sort(self, alist):
        self.helper(alist, 0, len(alist) - 1)
    
    def helper(self, alist, first, last):
        if (first < last): 
            splitpoint = self.partition(alist, first, last)
            
            self.helper(alist, first, splitpoint - 1)
            self.helper(alist, splitpoint + 1, last)
    
    
    def partition(self, alist, first, last):
        pivotvalue = alist[first]
        leftmark = first + 1
        rightmark = last
    
        done = False
        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
    
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
    
            if rightmark < leftmark:
                done = True
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    
        alist[first], alist[rightmark] = alist[rightmark], alist[first]

        return rightmark
   
   
def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    quick = QuickSort()
    quick.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
