---

# 📘 Comparative Analysis of Sorting Algorithms on Varying Data Distributions

## 🎯 Objective

This project aims to implement and analyze the performance of four popular sorting algorithms—**Quick Sort, Merge Sort, Heap Sort, and Insertion Sort**—on various data distributions. These include random, sorted, reversed, and nearly sorted datasets. The project investigates the practical execution time and compares it against theoretical time complexities.

---

## ⚙️ Methodology

The project is divided into the following key components:

### 1. **Implementation of Sorting Algorithms**

Implemented in Python, the project includes:

* **Quick Sort**: Divide-and-conquer approach using a pivot to partition elements.
* **Merge Sort**: A stable recursive algorithm that merges sorted halves.
* **Heap Sort**: Utilizes a binary heap data structure for sorting.
* **Insertion Sort**: A simple algorithm ideal for small or nearly sorted datasets.

Each algorithm is modular and can be invoked independently.

### 2. **Dataset Generation**

Datasets are dynamically created using the `generate_data()` function, supporting the following types:

* **Random**: Random values from 0 to 10,000
* **Sorted**: Ascending order
* **Reversed**: Descending order
* **Nearly Sorted**: Slightly shuffled sorted array

### 3. **Performance Measurement**

Execution time is measured using Python’s `time` module. The `measure_performance()` function prints timing data for selected algorithms and dataset types and sizes (1K, 5K, 10K, and 100K elements).

### 4. **Data Visualization**

Using `matplotlib`, the project visualizes:

* Execution time vs. dataset size
* Comparison of all algorithms on a chosen distribution

### 5. **Graphical User Interface (GUI)**

A user-friendly GUI built with `tkinter` allows users to:

* Select dataset distribution
* Run and visualize performance for each algorithm
* Compare all algorithms interactively

---

## 🖥️ How to Run

### Requirements

* Python 3.x
* `matplotlib`
* `tkinter` (built-in in most Python installations)

### Run the Program

```
bash
python your_script_name.py
```

The GUI will launch, allowing you to explore sorting performance visually.

---

## 🧠 Contributors

* **Mark Joshua Bueta**
* **Denise Dela Cruz**
* **Francis Adrian Gapol**
* **Mark Jerome Teopaco**

---
