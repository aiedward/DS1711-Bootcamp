from util.ArrayUtil import ArrayUtil

class MergeSort:
   
    def sort(self, array):
        tmp_array = [None] * len(array)
        self.helper(array, tmp_array, 0, len(array) - 1)
        
    def helper(self, array, tmp_array, left, right):
        if (left < right):
            middle = left + (right - left) // 2   # (left+right)//2
            self.helper(array, tmp_array, left, middle)
            self.helper(array, tmp_array, middle + 1, right)
            self.merge(array, tmp_array, left, middle + 1, right)

    def merge(self, array, tmpArray, leftPos, rightPos, rightEnd):
        leftEnd = rightPos - 1;
        tmpPos = leftPos;
        count = rightEnd - leftPos + 1;
        
        while (leftPos <= leftEnd and rightPos <= rightEnd):
            if(array[leftPos] < array[rightPos]):
                tmpArray[tmpPos] = array[leftPos]
                tmpPos += 1
                leftPos += 1
            else:
                tmpArray[tmpPos] = array[rightPos]
                tmpPos += 1
                rightPos += 1
                
        while (leftPos <= leftEnd):
            tmpArray[tmpPos] = array[leftPos]
            tmpPos += 1
            leftPos += 1
            
        while (rightPos <= rightEnd):
            tmpArray[tmpPos] = array[rightPos]
            tmpPos += 1
            rightPos += 1
        
        for i in range (count):  # Copy tmpArray back
            array[rightEnd] = tmpArray[rightEnd]
            rightEnd -= 1
        
def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    merge = MergeSort()
    merge.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
