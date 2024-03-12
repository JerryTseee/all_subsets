def subset(A, mark, start, k):#mark: an array to track the subset elements; k: the count of selected elements;
    n = len(A)
    if start == n:#reach the end of the array
        if k > 0:#we have selected at least one element in the subset
            subset_result = []
            for i in range(n):
                if mark[i] == 1:
                    subset_result.append(A[i])
            print(subset_result)
    else:
        #perform recursion to generate all possible subsets
        #path 1:
        mark[start] = 1
        subset(A, mark, start + 1, k + 1)
        #path 2:
        mark[start] = 0
        subset(A, mark, start + 1, k)

# Example usage
A = [5, 10, -3]
mark = [0, 0, 0]
subset(A, mark, 0, 0)
