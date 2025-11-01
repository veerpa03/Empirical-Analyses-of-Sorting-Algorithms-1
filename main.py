import random
import time

# -----------------------------------------------------
# Insertion Sort
# -----------------------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# -----------------------------------------------------
# Randomized Quick Sort
# -----------------------------------------------------
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# -----------------------------------------------------
# Testing Functions (as in assignment)
# -----------------------------------------------------
def test_me_insertion_sort():
    arr = [5, 2, 4, 6, 1, 3]
    print("Original array:", [5, 2, 4, 6, 1, 3])
    insertion_sort(arr)
    print("Sorted array:", arr)  # 👈 added this line
    assert arr == sorted([5, 2, 4, 6, 1, 3])
    print("Insertion Sort test passed!\n")

def test_me_randomized_quick_sort():
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", [10, 7, 8, 9, 1, 5])
    randomized_quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)  # 👈 added this line
    assert arr == sorted([10, 7, 8, 9, 1, 5])
    print("Randomized Quick Sort test passed!\n")

# -----------------------------------------------------
# Main function for runtime testing
# -----------------------------------------------------
def main():
    sizes = [10, 100, 1000, 2000, 5000, 10000, 20000]
    trials = 5  # number of trials per input size

    print("Insertion Sort:")
    for n in sizes:
        if n > 5000:  # skip very large inputs
            print(f"  n = {n}: skipped (too slow)")
            continue

        times = []  # store 5 runtimes
        for t in range(trials):
            arr = [random.randint(0, 10000) for _ in range(n)]
            start = time.time()
            insertion_sort(arr)
            end = time.time()
            times.append((end - start) * 1000)  # convert to ms

        # sort times and take median
        times.sort()
        median = times[len(times) // 2]
        print(f"  n = {n}: {median:.2f} ms")

    print("\nRandomized Quick Sort:")
    for n in sizes:
        times = []
        for t in range(trials):
            arr = [random.randint(0, 10000) for _ in range(n)]
            start = time.time()
            randomized_quick_sort(arr, 0, len(arr) - 1)
            end = time.time()
            times.append((end - start) * 1000)

        times.sort()
        median = times[len(times) // 2]
        print(f"  n = {n}: {median:.2f} ms")


# -----------------------------------------------------
# Run the tests and main
# -----------------------------------------------------
if __name__ == "__main__":
    test_me_insertion_sort()
    test_me_randomized_quick_sort()
    main()
