from sorting_A import SortingAlgorithms

def get_user_input():
    user_input = input("Enter a list of numbers separated by spaces: ")
    arr = [int(x) for x in user_input.split()]
    return arr

def main():
    # Get user input
    arr = get_user_input()
    
    # Using Tri par insertion
    sorted_arr_insertion = SortingAlgorithms.tri_par_insertion(arr.copy())
    print("Sorted array using Tri par insertion:", sorted_arr_insertion)
    
    # Using Tri fusion
    sorted_arr_fusion = SortingAlgorithms.tri_fusion(arr.copy())
    print("Sorted array using Tri fusion:", sorted_arr_fusion)

if __name__ == "__main__":
    main()
