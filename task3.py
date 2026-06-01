import numpy as np

def print_separator():
    print("\n" + "="*50 + "\n")

def get_matrix(rows, cols, name="Matrix"):
    print(f"Enter the elements for {name} ({rows}x{cols}) row by row, separating numbers with spaces:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"  Row {i+1}: ").split()
                if len(row_input) != cols:
                    print(f"    ❌ Error: Please enter exactly {cols} numbers.")
                    continue
                row = [float(x) for x in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("    ❌ Error: Invalid input. Please enter numbers only.")
    return np.array(matrix)

def main():
    print_separator()
    print("      ✨ WELCOME TO THE MATRIX OPERATIONS TOOL ✨")
    print_separator()
    
    while True:
        print("Choose a Matrix Operation:")
        print("1. Matrix Addition (+)")
        print("2. Matrix Subtraction (-)")
        print("3. Matrix Multiplication (×)")
        print("4. Matrix Transpose (T)")
        print("5. Determinant Calculation (det)")
        print("6. Exit Application")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '6':
            print("\nThank you for using the Matrix Operations Tool! Goodbye! 👋")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("\n❌ Invalid choice! Please select a valid option from the menu.")
            print_separator()
            continue
            
        try:
            # Operations requiring TWO matrices
            if choice in ['1', '2', '3']:
                r1 = int(input("Enter number of rows for Matrix A: "))
                c1 = int(input("Enter number of columns for Matrix A: "))
                
                if choice == '3':
                    r2 = int(input("Enter number of rows for Matrix B: "))
                    c2 = int(input("Enter number of columns for Matrix B: "))
                    if c1 != r2:
                        print("\n❌ Error: For multiplication, Matrix A columns must equal Matrix B rows!")
                        print_separator()
                        continue
                else:
                    r2, c2 = r1, c1
                    print(f"Matrix B will automatically be {r2}x{c2} for this operation.")
                
                print()
                matrix_A = get_matrix(r1, c1, "Matrix A")
                print()
                matrix_B = get_matrix(r2, c2, "Matrix B")
                
                print_separator()
                print("📐 INPUT MATRICES:")
                print(f"\nMatrix A:\n{matrix_A}")
                print(f"\nMatrix B:\n{matrix_B}")
                
                print("\n📊 RESULT:")
                if choice == '1':
                    result = np.add(matrix_A, matrix_B)
                    print(f"Matrix A + Matrix B =\n{result}")
                elif choice == '2':
                    result = np.subtract(matrix_A, matrix_B)
                    print(f"Matrix A - Matrix B =\n{result}")
                elif choice == '3':
                    result = np.dot(matrix_A, matrix_B)
                    print(f"Matrix A × Matrix B =\n{result}")
            
            # Operations requiring ONE matrix
            elif choice in ['4', '5']:
                r = int(input("Enter number of rows for the matrix: "))
                c = int(input("Enter number of columns for the matrix: "))
                
                if choice == '5' and r != c:
                    print("\n❌ Error: Determinant can only be calculated for SQUARE matrices (Rows = Columns)!")
                    print_separator()
                    continue
                    
                print()
                matrix_M = get_matrix(r, c, "Your Matrix")
                
                print_separator()
                print("📐 INPUT MATRIX:")
                print(f"\nMatrix:\n{matrix_M}")
                
                print("\n📊 RESULT:")
                if choice == '4':
                    result = matrix_M.T
                    print(f"Transposed Matrix =\n{result}")
                elif choice == '5':
                    result = np.linalg.det(matrix_M)
                    print(f"Determinant = {result:.2f}")
                    
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            
        print_separator()

if __name__ == "__main__":
    main()