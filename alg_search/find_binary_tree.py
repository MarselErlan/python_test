class Binar():
    def __init__(self, array, desired_num, mid, low, high):
        self.array = array
        self.desired_num = desired_num
        self.mid = mid
        self.low = low
        self.high = high

    def binary_tree(self):

        self.array.sort()
        print(self.array)
        self.desired_num = int(input('Enter the number u want to find'))
        self.mid = len(self.array) // 2
        self.low = 0
        self.high = len(self.array) - 1

        while self.array[self.mid] != self.desired_num and self.low <= self.high:
            if self.desired_num > self.array[self.mid]:
                self.low = self.mid + 1
            else:
                self.high = self.mid - 1
            self.mid = (self.low + self.high) // 2
        if self.low > self.high:
            print('No value')
        else:
            print('Index:', self.mid)

b = Binar(array=[64, 23, 89, 6, 1, 12, 33], desired_num=None, mid=None, low=None, high=None)
b.binary_tree()
