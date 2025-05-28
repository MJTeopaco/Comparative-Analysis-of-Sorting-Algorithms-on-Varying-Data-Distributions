import time
import random
import matplotlib.pyplot as plt
import tkinter as tk

# sorting algorithms
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[i] < arr[left]: largest = left
        if right < n and arr[largest] < arr[right]: largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# generated data (1K, 10K, 100K)
def generate_data(size, distribution_type):
    if distribution_type == 'random':
        return [random.randint(0, 10000) for _ in range(size)]
    elif distribution_type == 'sorted':
        return list(range(size))
    elif distribution_type == 'reversed':
        return list(range(size, 0, -1))
    elif distribution_type == 'nearly_sorted':
        arr = list(range(size))
        for _ in range(size // 10):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

# execution time in terminal
def measure_performance(sort_func, data, size, distribution):
    start_time = time.time()
    sort_func(data.copy())  
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"✅ {sort_func.__name__} | {distribution} | {size} elements | Execution Time: {execution_time:.6f} seconds")
    
    return execution_time

# graph of algorithm performance
def show_graph(sort_func, distribution):
    sizes = [1000, 10000, 100000] if sort_func != insertion_sort else [1000, 5000, 10000]  # Restrict Insertion Sort to ≤10,000 elements
    times = []

    for size in sizes:
        data = generate_data(size, distribution)
        execution_time = measure_performance(sort_func, data, size, distribution)
        times.append(execution_time)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', label=f"{sort_func.__name__} on {distribution} data")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Performance of {sort_func.__name__} on {distribution} Data")
    plt.legend()
    plt.show()

# comparison of all sorting algorithms
def compare_all_algorithms(distribution):
    plt.figure(figsize=(10, 6))
    for sort_func in [quick_sort, merge_sort, heap_sort, insertion_sort]:
        sizes = [1000, 10000, 100000] if sort_func != insertion_sort else [1000, 5000, 10000]  # Restrict Insertion Sort size
        times = []
        for size in sizes:
            data = generate_data(size, distribution)
            execution_time = measure_performance(sort_func, data, size, distribution)
            times.append(execution_time)

        plt.plot(sizes, times, marker='o', linestyle='-', label=f"{sort_func.__name__} on {distribution} data")

    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Comparison of Sorting Algorithms on {distribution} Data")
    plt.legend()
    plt.show()

# gui visualization
def create_gui():
    root = tk.Tk()
    root.title("Sorting Algorithm Performance Viewer")
    root.geometry("500x700")
    root.configure(bg="#f0f0f0")

    header = tk.Label(root, text="Sorting Algorithm Performance Viewer", font=("Poppins", 16, "bold"), bg="#f0f0f0")
    header.pack(pady=10)

    selection_frame = tk.Frame(root, bg="#ffffff", relief="groove", bd=2)
    selection_frame.pack(padx=10, pady=10, fill="x")

    tk.Label(selection_frame, text="Select Data Distribution Type:", font=("Poppins", 12)).pack(pady=5)
    selected_dist = tk.StringVar(value="random")
    distributions = ['random', 'sorted', 'reversed', 'nearly_sorted']
    for dist in distributions:
        tk.Radiobutton(selection_frame, text=dist.capitalize(), variable=selected_dist, value=dist, font=("Poppins", 10)).pack(anchor="w", padx=10)

    button_frame = tk.Frame(root, bg="#ffffff", relief="groove", bd=2)
    button_frame.pack(padx=10, pady=10, fill="x")

    tk.Button(button_frame, text="Quick Sort", command=lambda: show_graph(quick_sort, selected_dist.get()), font=("Poppins", 12), bg="#add8e6").pack(pady=5, fill="x")
    tk.Button(button_frame, text="Merge Sort", command=lambda: show_graph(merge_sort, selected_dist.get()), font=("Poppins", 12), bg="#add8e6").pack(pady=5, fill="x")
    tk.Button(button_frame, text="Heap Sort", command=lambda: show_graph(heap_sort, selected_dist.get()), font=("Poppins", 12), bg="#add8e6").pack(pady=5, fill="x")
    tk.Button(button_frame, text="Insertion Sort", command=lambda: show_graph(insertion_sort, selected_dist.get()), font=("Poppins", 12), bg="#9aa2a5").pack(pady=5, fill="x")
    tk.Button(button_frame, text="Compare All Algorithms", command=lambda: compare_all_algorithms(selected_dist.get()), font=("Poppins", 12), bg="#ffcccb").pack(pady=10, fill="x")

    tk.Button(root, text="Exit", command=root.quit, font=("Poppins", 12), bg="gray").pack(pady=10)

    root.mainloop()

# Mriin function: Runs GUI
def main():
    create_gui()

if __name__ == "__main__":
    main()
