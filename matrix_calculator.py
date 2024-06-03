'''Program that completes operations on matrices'''
import re
import numpy as np

def phone_number():
    '''Requests and Validates a users phone number'''
    while True:
        # Gathers user's phone number
        phone = input("Enter a valid phone number (XXX-XXX-XXXX): ")
        # Ensures the users zipcode follows the correct format
        if re.match(r'\d{3}-\d{3}-\d{4}', phone):
            return phone
        else:
            # Returns a message if user's input does not follow format
            print("Incorrect format. Please Try Again.")

def zip_code():
    '''Requests and Validates a zipcode'''
    while True:
        #Gathers user's zipcode
        zipcode = input("Enter your zipcode (XXXXX-XXXX): ")
        #Ensures the users zipcode follows the correct format
        if re.match(r'\d{5}-\d{4}', zip):
            return zipcode
        else:
            #Returns a message if user's input does not follow format
            print("Incorrect format. Please Try Again.")

def create_matrix():
    """Function that creates the matrix"""
    matrix = []
    #Creates the matrix and its values
    for _ in range(3):
        #Establishes where the input values go
        row = input("")
        values = list(map(int,row.split()))
        matrix.append(values)
    return np.array(matrix)

def display_matrix(matrix):
    """Function that prints the matrix"""
    for row in matrix:
        #Prints the matrix
        print(''.join(map(str, row)))

def matrix_operations(matrix_1, matrix_2):
    '''Function that requests the operation the user want to complete on the created matrices '''
    #List the operations that can be performed by the user
    print("Select and operation from the list: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Matrix Multiplication")
    print("4. Element by Element multiplication")
    print("5. Exit matrix operations")
    #Menu interface to select an operation
    operation = 0
    while operation != 5:
        operation = int(input("Select a matrix operation: "))
        #Selects addition if user selects "1"
        if operation == 1:
            print("You are adding matrices")
            #Calls function that adds the matrices
            mat_addition(matrix_1, matrix_2)
        # Selects subtraction if user selects "2"
        elif operation == 2:
            print("You are subtracting matrices")
            # Calls function that subtracts the matrices
            mat_subtraction(matrix_1, matrix_2)
        # Selects matrix multiplication if user selects "3"
        elif operation == 3:
            print("You are matrix multiplying matrices")
            # Calls function that multiplies the matrices
            mat_matrix_multiplication(matrix_1, matrix_2)
        # Selects element multiplication if user selects "4"
        elif operation == 4:
            print("You are element multiplying matrices")
            # Calls function that multiplies the matrices by element
            mat_element(matrix_1, matrix_2)
        elif operation == 5:
            print("Exiting operations.")
            #Exits operations and returns to the main function
            break
        else:
            #Prints the user's choice was invalid
            print("Invalid Choice")

def mat_addition(matrix_1, matrix_2):
    '''Function that adds the matrices together'''
    #Calls function that adds the matrices
    result = np.add(matrix_1, matrix_2)
    #Prints the result of operation
    print("The result is: \n ", result)

    #Prints Transpose
    print("\nThe Transpose is:\n")
    print(np.transpose(result))

    print("\nMean of rows:\n")
    #Prints the result of finding the mean of the row
    print(np.mean(result, axis=1))

    print("\nMean of columns:\n")
    #Prints the result of finding the mean of the columns
    print(np.mean(result, axis=0))

    return result
def mat_subtraction(matrix_1, matrix_2):
    '''Function that subtracts the matrices together'''
    # Calls function that adds the matrices
    result = np.subtract(matrix_1, matrix_2)
    # Prints the result of operation
    print("The result is: \n ", result)
    # Prints Transpose of the results
    print("\nThe Transpose is\n:")
    print(np.transpose(result))

    # Prints mean of both columns and rows
    print("\nMean of rows:")
    # Prints the result of finding the mean of the row
    print(np.mean(result, axis=1))

    print("\nMean of columns:")
    # Prints the result of finding the mean of the columns
    print(np.mean(result, axis=0))
    return result
def mat_matrix_multiplication(matrix_1, matrix_2):
    '''Function that performs matrix multiplication the matrices together'''
    # Calls function that multiplies the matrices
    result = np.matmul(matrix_1, matrix_2)
    # Prints the result of operation
    print("The result is: \n", result)

    print("\nThe Transpose is\n:")
    # Prints Transpose
    print(np.transpose(result))

    print("\nMean of rows:")
    # Prints the result of finding the mean of the row
    print(np.mean(result, axis=1))

    print("\nMean of columns:")
    # Prints the result of finding the mean of the row
    print(np.mean(result, axis=0))
    return result
def mat_element(matrix_1, matrix_2):
    '''Function that performs element multiplication'''
    # Calls function that multiplies by elements of the matrices
    result = np.multiply(matrix_1, matrix_2)
    # Prints the result of operation
    print("The result is: \n", result)

    print("\nThe Transpose is\n:")
    # Prints Transpose
    print(np.transpose(result))

    print("\nMean of rows:")
    # Prints the result of finding the mean of the row
    print(np.mean(result, axis=1))

    print("\nMean of columns:")
    # Prints the result of finding the mean of the row
    print(np.mean(result, axis=0))
    return result

def main():
    '''Function that runs the main program'''
    # Asks the user if they want to continue with the program
    user_choice = 0
    while user_choice != 2:
        user_choice = int(input("Do you want to play the Matrix Game (1=yes/2=no): "))
        if user_choice == 1:
            # Welcomes user to the application
            print("********Welcome to the Matrix Application******")
            # Calls function that inputs and validates the users phone number
            number = phone_number()
            print("Your phone number is: ", number)
            # Calls function that inputs and validates the users phone number
            z_code = zip_code()
            print("Your zipcode is: ", z_code)

            # Requests the first matrix
            print("Enter your first 3x3 matrix: ")
            # Calls function that creates matrix
            matrix_1 = create_matrix()
            print("Your first 3x3 matrix: ")
            # Calls function that displays function
            display_matrix(matrix_1)

            # Requests the second matrix
            print("Enter your Second 3x3 matrix: ")
            # Calls function that creates matrix
            matrix_2 = create_matrix()
            print("Your Second 3x3 matrix: ")
            # Calls function that displays function
            display_matrix(matrix_2)
            # Calls function that completes operations on matrices
            matrix_operations(matrix_1, matrix_2)
        elif user_choice == 2:
            # Prints an exit thank you message for the program
            print("Thank you for using the program.")
            break
        else:
            # Informs user that the input choice was invalid
            print("Invalid choice")

if __name__ == '__main__':
    main()
