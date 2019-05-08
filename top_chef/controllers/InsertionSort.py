class Insertionsort:
    def __init__(self,array):
        self.array = array

    def insertionSort(self):
        # for every element in our array
        for index in range(1, len(self.array)):
            current = self.array[index]
            position = index

            while position > 0 and self.array[position - 1] > current:
                self.array[position] = self.array[position - 1]
                position -= 1

            self.array[position] = current

        return self.array

if __name__ == '__main__':
    i = Insertionsort([4,5,3,1,7,9])
    a =i.insertionSort()
    print(a)
