class Patient:
    """A patient with a name and urgency from 1 (highest) to 10."""

    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10.")
        self.name = name
        self.urgency = urgency


class MinHeap:
    """Keeps the most urgent patient at the start of a list."""

    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent].urgency:
                break
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print("-", patient.name, "(" + str(patient.urgency) + ")")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        most_urgent = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return most_urgent


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    served = heap.remove_min()
    print("Next patient:", served.name)
    heap.print_heap()
