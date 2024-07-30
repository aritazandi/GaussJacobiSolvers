import numpy as np
import copy

def print_equations(arrSorted):
    for i in range(len(arrSorted)): 
        tempStr = f'{arrSorted[i][0]}x + {arrSorted[i][1]}y + {arrSorted[i][2]}z = {arrSorted[i][3]}'
        tempStr = tempStr.replace("+-", "-")
        print(tempStr)
        #moadele ra baraye ma chap mikonad(moratab shode)

def jacobi_iteration(arr, xk, yk, zk):
    xk_1 = (arr[0][3] - arr[0][1] * yk - arr[0][2] * zk) / arr[0][0]
    yk_1 = (arr[1][3] - arr[1][0] * xk - arr[1][2] * zk) / arr[1][1]
    zk_1 = (arr[2][3] - arr[2][0] * xk - arr[2][1] * yk) / arr[2][2]
    return xk_1, yk_1, zk_1

def gauss_iteration(arr, xk, yk, zk):
    xk_1 = (arr[0][3] - arr[0][1] * yk - arr[0][2] * zk) / arr[0][0]
    yk_1 = (arr[1][3] - arr[1][0] * xk_1 - arr[1][2] * zk) / arr[1][1]
    zk_1 = (arr[2][3] - arr[2][0] * xk_1 - arr[2][1] * yk_1) / arr[2][2]
    return xk_1, yk_1, zk_1

def norm(x0, x1, epsilon):
    norm = 0
    for i in range(0, 3):
        norm += abs(x1[i] - x0[i])
    return norm > epsilon
    # baraye inke bdonim ta che gavabi brim
 
def calculate_khata(arrSorted, x_final):
    A = np.array([row[:3] for row in arrSorted])  
    B = np.array([row[3] for row in arrSorted])  
    X = np.array(x_final)                       
    AX = np.dot(A, X)                          
    khata = B - AX                              
    return khata
    # in method megdar khata ra mohasebe mikonad

def solve_jacobi(arrSorted, epsilon, first_x0):
    xk, yk, zk = 0, 0, 0
    X = np.array(first_x0, dtype=float)  # Initial value for X
    i = 0
    while True:
        xk, yk, zk = jacobi_iteration(arrSorted, X[0], X[1], X[2])  # Using X to compute xk, yk, zk
        X[0], X[1], X[2] = xk, yk, zk  # Update values of X
        i += 1
        print(f"Jacobi Iteration {i}: x = {xk:.6f}, y = {yk:.6f}, z = {zk:.6f}")
        if i > 1 and not norm(X_prev, X, epsilon):  # Stop iteration if the error condition is met
            break
        X_prev = np.copy(X)  # Save previous X for comparison in subsequent iterations
    
    khata = calculate_khata(arrSorted, X)  # Calculate error using final X
    print(f"khata: {khata}")

def solve_gauss(arrSorted, epsilon, first_x0):
    xk, yk, zk = 0, 0, 0
    X = np.array(first_x0, dtype=float)  # Initial value for X
    i = 0
    while True:
        xk, yk, zk = gauss_iteration(arrSorted, X[0], X[1], X[2])  # Using X to compute xk, yk, zk
        X[0], X[1], X[2] = xk, yk, zk  # Update values of X
        i += 1
        print(f"Gauss-Seidel Iteration {i}: x = {xk:.6f}, y = {yk:.6f}, z = {zk:.6f}")
        if i > 1 and not norm(X_prev, X, epsilon):  # Stop iteration if the error condition is met
            break
        X_prev = np.copy(X)  # Save previous X for comparison in subsequent iterations
    
    khata = calculate_khata(arrSorted, X)  # Calculate error using final X
    print(f"khata: {khata}")

# Examples for Jacobi
jacobi_examples = [
    [
        [-2, 1, 5, 15],
        [4, -1, 1, 7],
        [4, 8, 1, -21]
    ],
    [
        [10, -1, 2, 8],
        [-1, 11, -1, -9],
        [2, -1, 10, 7]
    ],
    [
        [3, -0.1, -0.2, 7.85],
        [0.1, 7, -0.3, -19.3],
        [0.3, -0.2, 10, 71.4]
    ]
]

# Examples for Gauss-Seidel
gauss_examples = [
    [
        [4, 1, 2, 4],
        [3, 5, 1, 7],
        [1, 1, 3, 3]
    ],
    [
        [4, -1, 0.2, 8],
        [3, 5, 1, -9],
        [1, 1, 4, 7]
    ],
    [
        [5, 2, 1, 12],
        [1, 7, 3, 22],
        [2, 1, 8, 35]
    ]
]

def main():
    print("Choose:")
    print("1. Jacobi examples")
    print("2. Gauss-Seidel examples")
    print("3. Enter equations manually")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Choose:")
        print("1. Jacobi example 1")
        print("2. Jacobi example 2")
        print("3. Jacobi example 3")
        example_choice = int(input("Enter the number of example: "))
        if example_choice in [1, 2, 3]:
            arr = jacobi_examples[example_choice - 1]
        else:
            print("error")
            return
    elif choice == 2:
        print("Choose:")
        print("1. Gauss-Seidel example 1")
        print("2. Gauss-Seidel example 2")
        print("3. Gauss-Seidel example 3")
        example_choice = int(input("Enter the number of example: "))
        if example_choice in [1, 2, 3]:
            arr = gauss_examples[example_choice - 1]
        else:
            print("error")
            return
    elif choice == 3:
        arr = []
        for i in range(3):
            row = []
            print(f"Enter coefficients for equation {i+1}:")
            for j in range(4):
                coef = float(input(f"Coefficient {j+1}: "))
                row.append(coef)
            arr.append(row)
    else:
        print("error")
        return

    arrSorted = [[0, 0, 0, 0] for _ in range(3)]

    for i in range(3):
        if abs(arr[i][0]) > abs(arr[i][1]) + abs(arr[i][2]):
            arrSorted[0] = arr[i]
        elif abs(arr[i][1]) > abs(arr[i][0]) + abs(arr[i][2]):
            arrSorted[1] = arr[i]
        elif abs(arr[i][2]) > abs(arr[i][0]) + abs(arr[i][1]):
            arrSorted[2] = arr[i]
        else:
            print("Error")
            print(arr[i])
            return

    print("Sorted equations:")
    print_equations(arrSorted)
    first_x0=[]
    for i in range(3):
        first_x0.append(int(input(f"Enter initial guess for x0[{i+1}]: ")))

    if choice == 1 or choice == 3:
        epsilon = float(input("Enter epsilon for Jacobi method: "))
        solve_jacobi(arrSorted, epsilon, first_x0)
    if choice == 2 or choice == 3:
        print("*******************")
        epsilon = float(input("Enter epsilon for Gauss-Seidel method: "))
        solve_gauss(arrSorted, epsilon, first_x0)

if __name__ == "__main__":
    main()
