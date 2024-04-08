# time_measurement_T.py

from sorting_T import SortingAlgorithms
from timeit import default_timer as timer

def generate_input_list():
    user_input = input("Enter a list of values separated by spaces: ")
    return user_input.split()

def measure_execution_time(algorithm_name, array):
    sorting_algorithms = SortingAlgorithms()
    start_time = timer()
    getattr(sorting_algorithms, algorithm_name)(array)
    end_time = timer()
    return end_time - start_time

def main():
    input_list = generate_input_list()
    print("Input list:", input_list)

    algorithms = ["selection_sort", "bubble_sort"]
    for algorithm in algorithms:
        sorted_list = input_list.copy()  # Create a copy of the input list
        execution_time = measure_execution_time(algorithm, sorted_list)
        print(f"Sorted list using {algorithm}: {sorted_list}")
        print(f"Execution time for {algorithm}: {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()
