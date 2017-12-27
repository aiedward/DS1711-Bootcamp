from util.ArrayUtil import ArrayUtil

class SelectionSort:
    
    def sort(self, array):
        for i in range(len(array)):
            pos_min = i
            for j in range(i + 1, len(array)):
                if (array[j] < array[pos_min]):
                    pos_min = j

            array[i], array[pos_min] = array[pos_min], array[i]
          
            
def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    selection = SelectionSort()
    selection.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
