from util.ArrayUtil import ArrayUtil

class ShellSort:
   
    def sort(self, array):
        gap = len(array)
        length = len(array)
        
        while (gap > 0):
            for i in range(gap, length):
                for j in range(i, gap - 1, -gap):
                    if (array[j - gap] > array[j]):
                        array[j], array[j - gap] = array[j - gap], array[j]
            
            if (gap == 2): 
                gap = 1
            else:
                gap = gap // 2


def main():
    util = ArrayUtil()
    mylist = util.generateRandomArray(10)
    print(mylist)
    shell = ShellSort()
    shell.sort(mylist)
    print(mylist)

    
if __name__ == "__main__":
    main()
