from util.ArrayUtil import ArrayUtil

class BubbleSort:
    
    def sort(self, array):
        for i in range(len(array)): # n pass
            is_sorted = True
            for j in range(1, len(array) - i):
                if (array[j] < array[j - 1]):
                    # swap
                    array[j], array[j - 1] = array[j - 1], array[j]
                    is_sorted = False
        
            if (is_sorted): break
            
def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    bubble = BubbleSort()
    bubble.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
