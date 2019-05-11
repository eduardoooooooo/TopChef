class InsertionSort:
    def __init__(self,array):
        self.array = array

    def sort(self):
        # for every element in our array
        if self.is_sorted():
            for index in range(1, len(self.array)):
                current = self.array[index]
                position = index

                while position > 0 and self.array[position - 1].get_score() < current.get_score():
                    self.array[position] = self.array[position - 1]
                    position -= 1

                self.array[position] = current
                return self.array

        return self.array

    def is_sorted(self):
        for index in range(1,len(self.array)):
            index1= self.array[index].get_score()
            index2 = self.array[index+1].get_score()
            if index1 > index2:
                return False
        return True