# main_T.py

from sorting_T import SortingAlgorithms
from timeit import default_timer as timer
import random

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_execution_time(algorithm_name, array):
    start_time = timer()
    SortingAlgorithms.__dict__[algorithm_name](array)
    end_time = timer()
    return end_time - start_time

def main():
    array = generate_random_array(1000)  # Adjust the size of the array as needed
    print("Input array:", array)

    algorithms = ["tri_par_selection", "tri_a_bulles"]  # Add more algorithms as needed
    for algorithm in algorithms:
        execution_time = measure_execution_time(algorithm, array)
        print(f"Execution time for {algorithm}: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()
