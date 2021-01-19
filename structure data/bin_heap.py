class BinHeap:
    def __init__(self):
        self.heaplist = []
        self.heapsize = 0

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        # Знаки
        if l <= self.heapsize and self.heaplist[l] > self.heaplist[i]:
            largest = l
        else:
            largest = i
        # Знаки и последний индекс
        if r <= self.heapsize and self.heaplist[r] > self.heaplist[largest]:
            largest = r
        if largest != i:
            # Обмен значениями явный
            tmp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[largest]
            self.heaplist[largest] = tmp
            self.heapify(largest)

    def buildHeap(self, list):
        self.heaplist = list
        # Из-за того, что у вас в процедуре используется <=, heapsize должен быть строго меньше, чтобы избежать выхода за пределы
        self.heapsize = len(list) - 1
        # Индексы также c середины и до нуля включительно
        for i in range(len(list) // 2, -1, -1):
            print(i)
            self.heapify(i)

    def heapSort(self):
        pass

    def extractMax(self):
        pass

    def getHeap(self):
        return self.heaplist

heap = BinHeap()
heap.buildHeap([0, 0, 9, 5, 23, 0, 0, 2, 2, 1, 4, 0, 12, -1, 0])
print(heap.getHeap())