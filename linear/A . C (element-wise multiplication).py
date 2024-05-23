import numpy as np

def elementwise_multiply(A, C):
    # Get the dimensions of matrix A
    m, n = A.shape
    # Initialize the result matrix F with zeros
    F = np.zeros((m, n))
    # Loop through each element of the matrices
    for i in range(m):
        for j in range(n):
            # Multiply corresponding elements of A and C
            F[i, j] = A[i, j] * C[i, j]
    return F

# Example usage
A = np.array([[1, 2], [3, 4]])  # Define matrix A
C = np.array([[5, 6], [7, 8]])  # Define matrix C
F = elementwise_multiply(A, C)  # Call the function for element-wise multiplication
print(F)                        # Print the result
