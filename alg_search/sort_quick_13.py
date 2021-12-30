class Quick:
    def __init__(self, array, element, left, center, right):
        self.array = array
        self.element = element
        self.left = left
        self.center = center
        self.right = right
    def quick_sort(self):
        if len(self.array) <= 1:
            return self.array
        self.element = self.array[0]
        self.left = list(filter(lambda num: num < self.element, self.array))
        self.center = [nums for nums in self.array if nums == self.element]
        self.right = list(filter(lambda num: num > self.element, self.array))

        return self.left + self.center + self.right


quick = Quick(array=[64, 23, 89, 6, 1, 12, 33], element=None, left=None, center=None, right=None)
quick.quick_sort()
print(f'Sorted list: {quick.quick_sort()}')