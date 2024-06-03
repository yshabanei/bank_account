class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        n = len(self.arr)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    swapped = True
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            if not swapped:
                break


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_instance = BubbleSort(arr)
bubble_sort_instance.bubbleSort()

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
