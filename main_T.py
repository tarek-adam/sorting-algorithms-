from sorting_T import SortingAlgorithms

def get_user_input():
    user_input = input("Enter a list of numbers separated by spaces: ")
    arr = [int(x) for x in user_input.split()]
    return arr

def main():
    # Get user input
    arr = get_user_input()
    
    # Using Tri par sélection
    sorted_arr_selection = SortingAlgorithms.tri_par_selection(arr.copy())
    print("Sorted array using Tri par sélection:", sorted_arr_selection)
    
    # Using Tri à bulles
    sorted_arr_bubble = SortingAlgorithms.tri_a_bulles(arr.copy())
    print("Sorted array using Tri à bulles:", sorted_arr_bubble)

if __name__ == "__main__":
    main()
