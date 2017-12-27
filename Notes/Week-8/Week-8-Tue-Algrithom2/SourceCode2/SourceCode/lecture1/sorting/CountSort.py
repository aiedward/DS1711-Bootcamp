from util.ArrayUtil import ArrayUtil

class CountSort:
   
    def sort(self, array):
        mmax, mmin = array[0], array[0]
        for i in range(1, len(array)):
            if (array[i] > mmax): mmax = array[i]
            elif (array[i] < mmin): mmin = array[i];
            
        nums = mmax - mmin + 1
        counts = [0] * nums
        for i in range (len(array)):
            counts[array[i] - mmin] = counts[array[i] - mmin] + 1
            
        pos = 0
        for i in range(nums):
            for j in range(counts[i]):
                array[pos] = i + mmin
                pos += 1
     
        
def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    count = CountSort()
    count.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
