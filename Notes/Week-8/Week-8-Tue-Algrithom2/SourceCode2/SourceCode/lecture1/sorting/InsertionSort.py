from util.ArrayUtil import ArrayUtil

class InsertionSort:
   
    def sort(self, array):
        for i in range(1, len(array)):
            for j in range(0, i):
                if (array[i] < array[j]):
                    array[i], array[j] = array[j], array[i]

def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    insertion = InsertionSort()
    insertion.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
