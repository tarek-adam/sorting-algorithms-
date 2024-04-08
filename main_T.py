# main_T.py

from sorting_T import SortingAlgorithms

def get_user_input():
    while True:
        user_input = input("Enter a list of numbers separated by spaces: ")
        try:
            arr = [int(x) for x in user_input.split()]
            return arr
        except ValueError:
            print("Invalid input. Please enter only numeric values separated by spaces.")

def main():
    arr = get_user_input()
    print("Input array:", arr)

    # Example usage of sorting algorithms from sorting_T.py
    sorted_arr_selection = SortingAlgorithms.tri_par_selection(arr.copy())
    print("Sorted array using Tri par sélection:", sorted_arr_selection)

    sorted_arr_bubble = SortingAlgorithms.tri_a_bulles(arr.copy())
    print("Sorted array using Tri à bulles:", sorted_arr_bubble)

if __name__ == "__main__":
    main()
