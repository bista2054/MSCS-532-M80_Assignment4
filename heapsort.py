import random
import time

# Implementing HeapSort
class Heapsort:
    def __init__(self):
        pass

    def heapify(self, arr, n, i):
        """Maintain the max-heap property for the subtree rooted at index i"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and recursively heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def build_max_heap(self, arr):
        """Build a max-heap from an unsorted array"""
        n = len(arr)
        # Start from the last non-leaf node and heapify each node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def sort(self, arr):
        """Main heapsort algorithm"""
        n = len(arr)
        self.build_max_heap(arr)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
        return arr


def main():
    sorter = Heapsort()
    sizes = [1000, 5000, 10000]
    scenarios = ["Random", "Sorted", "Reverse-sorted", "Nearly-sorted"]

    print("\n==============================")
    print(" Heapsort Performance Results ")
    print("==============================")

    for n in sizes:
        print(f"\n--- Array Size: {n} ---")

        # Generate random base array
        base = [random.randint(0, 100000) for _ in range(n)]

        # 1. Random array
        arr = base.copy()
        start = time.time()
        sorter.sort(arr)
        print(f"Random array:        {time.time() - start:.6f} seconds")

        # 2. Sorted array
        arr = sorted(base)
        start = time.time()
        sorter.sort(arr)
        print(f"Sorted array:        {time.time() - start:.6f} seconds")

        # 3. Reverse-sorted array
        arr = sorted(base, reverse=True)
        start = time.time()
        sorter.sort(arr)
        print(f"Reverse-sorted array:{time.time() - start:.6f} seconds")

        # 4. Nearly-sorted array
        arr = sorted(base)
        for _ in range(int(0.05 * n)):  # 5% random swaps
            i, j = random.sample(range(n), 2)
            arr[i], arr[j] = arr[j], arr[i]
        start = time.time()
        sorter.sort(arr)
        print(f"Nearly-sorted array: {time.time() - start:.6f} seconds")

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    main()
