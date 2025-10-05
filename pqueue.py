import random
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline=None, description=""):
        self.task_id = task_id
        self.priority = priority  # Higher number = higher priority
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.description = description

    def __lt__(self, other):
        """For min-heap implementation (lower priority number = higher priority)"""
        return self.priority < other.priority

    def __gt__(self, other):
        """For max-heap implementation"""
        return self.priority > other.priority

    def __repr__(self):
        return f"Task({self.task_id}, priority={self.priority}, arrival={self.arrival_time})"


class PriorityQueue:
    def __init__(self, max_heap=True):
        """
        Initialize priority queue
        max_heap=True: highest priority first (largest number)
        max_heap=False: lowest priority first (smallest number)
        """
        self.heap = []
        self.max_heap = max_heap
        self.task_counter = 0

    def _heapify_up(self, index):
        """Maintain heap property by moving element up"""
        if index == 0:
            return

        parent = (index - 1) // 2

        if self.max_heap:
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                self._heapify_up(parent)
        else:
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                self._heapify_up(parent)

    def _heapify_down(self, index):
        """Maintain heap property by moving element down"""
        left = 2 * index + 1
        right = 2 * index + 2
        extreme = index

        if self.max_heap:
            if left < len(self.heap) and self.heap[left] > self.heap[extreme]:
                extreme = left
            if right < len(self.heap) and self.heap[right] > self.heap[extreme]:
                extreme = right
        else:
            if left < len(self.heap) and self.heap[left] < self.heap[extreme]:
                extreme = left
            if right < len(self.heap) and self.heap[right] < self.heap[extreme]:
                extreme = right

        if extreme != index:
            self.heap[index], self.heap[extreme] = self.heap[extreme], self.heap[index]
            self._heapify_down(extreme)

    def insert(self, task):
        """
        Insert a new task into the priority queue
        Time Complexity: O(log n)
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_top(self):
        """
        Remove and return the highest priority task
        Time Complexity: O(log n)
        """
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return top

    def peek(self):
        """Return the highest priority task without removing it"""
        return self.heap[0] if self.heap else None

    def is_empty(self):
        """Check if the priority queue is empty"""
        return len(self.heap) == 0

    def size(self):
        """Return the number of tasks in the queue"""
        return len(self.heap)

    def change_priority(self, task_id, new_priority):
        """
        Change priority of a specific task
        Time Complexity: O(n) to find + O(log n) to update
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                old_priority = task.priority
                task.priority = new_priority

                # Re-heapify based on priority change direction
                if (self.max_heap and new_priority > old_priority) or \
                        (not self.max_heap and new_priority < old_priority):
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return True
        return False


class TaskScheduler:
    """Real-world application of priority queue for task scheduling"""

    def __init__(self):
        self.pq = PriorityQueue(max_heap=True)  # Higher priority number = more urgent
        self.completed_tasks = []
        self.current_time = 0

    def add_task(self, description, priority, duration, deadline=None):
        """Add a new task to the scheduler"""
        task = Task(
            task_id=len(self.pq.heap) + len(self.completed_tasks) + 1,
            priority=priority,
            arrival_time=self.current_time,
            deadline=deadline,
            description=description
        )
        task.duration = duration
        self.pq.insert(task)
        print(f"Added: {description} (Priority: {priority})")

    def execute_next(self):
        """Execute the highest priority task"""
        if self.pq.is_empty():
            print("No tasks to execute")
            return None

        task = self.pq.extract_top()
        print(f"Executing: {task.description} (Priority: {task.priority})")

        # Simulate task execution
        self.current_time += task.duration
        task.completion_time = self.current_time

        self.completed_tasks.append(task)
        return task

    def show_queue(self):
        """Display current task queue"""
        if self.pq.is_empty():
            print("Queue is empty")
            return

        print("\nCurrent Task Queue (by priority):")
        # Create a copy for display without modifying the heap
        temp_pq = PriorityQueue(max_heap=self.pq.max_heap)
        temp_pq.heap = self.pq.heap.copy()

        while not temp_pq.is_empty():
            task = temp_pq.extract_top()
            print(f"  - {task.description} (Priority: {task.priority}, Duration: {task.duration})")

    def get_statistics(self):
        """Calculate scheduling statistics"""
        if not self.completed_tasks:
            return "No tasks completed yet"

        total_tasks = len(self.completed_tasks)
        avg_waiting_time = sum(task.completion_time - task.arrival_time for task in self.completed_tasks) / total_tasks
        avg_turnaround_time = sum(
            task.completion_time - task.arrival_time for task in self.completed_tasks) / total_tasks

        return {
            'total_completed': total_tasks,
            'average_waiting_time': avg_waiting_time,
            'average_turnaround_time': avg_turnaround_time,
            'current_time': self.current_time
        }


# Demonstration and Testing
def demonstrate_priority_queue():
    """Comprehensive demonstration of priority queue functionality"""

    print("=== PRIORITY QUEUE  ===\n")

    # Create a task scheduler
    scheduler = TaskScheduler()

    # Add various tasks with different priorities
    tasks = [
        ("System Backup", 1, 30),  # Low priority
        ("User Request", 5, 5),  # Medium priority
        ("Critical Bug Fix", 10, 15),  # High priority
        ("Email Processing", 2, 10),  # Low priority
        ("Security Patch", 8, 20),  # High priority
    ]

    for description, priority, duration in tasks:
        scheduler.add_task(description, priority, duration)

    print("\n" + "=" * 50)
    scheduler.show_queue()

    print("\n" + "=" * 50)
    print("EXECUTING TASKS:")
    print("=" * 50)

    # Execute all tasks
    while not scheduler.pq.is_empty():
        scheduler.execute_next()
        print(f"Time elapsed: {scheduler.current_time} units")

    print("\n" + "=" * 50)
    print("SCHEDULING STATISTICS:")
    stats = scheduler.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")


def performance_analysis():
    """Analyze performance of priority queue operations"""
    import time

    print("\n=== PERFORMANCE ANALYSIS ===")

    pq = PriorityQueue(max_heap=True)

    # Test insertion performance
    sizes = [100, 1000, 5000, 10000]
    insertion_times = []
    extraction_times = []

    for size in sizes:
        # Insertion test
        start = time.time()
        for i in range(size):
            task = Task(i, random.randint(1, 100), time.time())
            pq.insert(task)
        insertion_time = time.time() - start
        insertion_times.append(insertion_time)

        # Extraction test
        start = time.time()
        for i in range(size):
            pq.extract_top()
        extraction_time = time.time() - start
        extraction_times.append(extraction_time)

        print(f"Size: {size:5d} | Insertion: {insertion_time:.6f}s | Extraction: {extraction_time:.6f}s")



# Run demonstrations
if __name__ == "__main__":
    demonstrate_priority_queue()
    performance_analysis()