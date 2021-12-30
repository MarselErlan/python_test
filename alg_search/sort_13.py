class Bubble:
    def __init__(self, array, number_1, number_2, swapped):
        self.array = array
        self.number_1 = number_1
        self.number_2 = number_2
        self.swapped = swapped

    def bubble_sort(self):
        self.swapped = False
        for self.number_1 in range(len(self.array) -1, 0, -1):
            for self.number_2 in range(self.number_1):
                if self.array[self.number_2] > self.array[self.number_2 + 1]:
                    self.array[self.number_2], self.array[self.number_2 + 1] = self.array[self.number_2 + 1], self.array[self.number_2]
                    self.swapped = True
            if self.swapped:
                self.swapped = False
            else:
                break
        return self.array
bubble = Bubble(array=[64, 23, 89, 6, 1, 12, 33], number_1=None, number_2=None, swapped=bool)
bubble.bubble_sort()
print(f'Sorted list: {bubble.bubble_sort()}')