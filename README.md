# MSCS-532-M80
# Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications

## Overview
This assignment focuses on the implementation and analysis of **heap data structures** and their applications in:

1. **Heapsort** - sorting algorithm using a binary heap.
2. **Priority Queue** - task scheduling using a max-heap.

The goal is to understand heap operations, analyze their efficiency, and explore real-world applications.


## Summary of Findings

### Heapsort Implementation and Analysis
1. **Heapsort** demonstrates stable and predictable performance across all input types but has slightly higher overhead due to heap maintenance operations.  
2. **Quicksort** outperforms others on small and medium datasets due to efficient partitioning and better memory locality.  
3. **MergeSort** is highly reliable and stable but requires additional **O(n)** memory, making it less space-efficient than Heapsort.  
4. Overall, empirical results align well with theoretical **O(n log n)** time complexity.

### Priority Queue Implementation and Applications
- The implemented **priority queue using a binary heap** efficiently supports task scheduling with **O(log n)** insertion and extraction.  
- A **max-heap** ensures that high-priority tasks are executed first.  
- Priority updates work correctly, and metrics like waiting and turnaround time demonstrate efficient scheduling.  
- The system combines theoretical efficiency with practical applicability for real-world task management.

---

## Running the Code
```bash
# Clone the repository and navigate to it
git clone https://github.com/bista2054/MSCS-532-M80_Assignment4.git
cd MSCS-532-M80_Assignment4

# Ensure Python is installed
python --version
# If Python is not installed, download it from https://www.python.org/ and install the latest version

# Install required dependencies
pip install matplotlib

# Run the scripts
# Heapsort Implementation
python heapsort.py

# Priority Queue Implementation
python pqueue.py
---
