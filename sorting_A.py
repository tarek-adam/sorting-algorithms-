class SortingAlgorithms:
    @staticmethod
    def tri_par_insertion(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def tri_fusion(arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            SortingAlgorithms.tri_fusion(left_half)
            SortingAlgorithms.tri_fusion(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
            return arr
