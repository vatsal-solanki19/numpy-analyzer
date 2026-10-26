import numpy as np

class DataAnalytics:
    def __init__(self):
        self.data = None


    def create_array(self):
 
        try:
            print("Select the Type of array to Create :")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            choice = int(input("Enter your choice:- "))

            if choice == 1:
                element = input("Enter elements for 1D array:- ").split()
                arr = list(map(int, element))
                self.data = np.array(arr)
                print(f"Elements : {self.data}")
                print("Elements added successfully!")
                return self.data
            
            elif choice == 2:
                rows = int(input("Enter the number of rows for 2D array:- "))
                cols = int(input("Enter the number of columns for 2D array:- "))     
                arr = input(f"Enter {rows * cols} elements for the array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(rows, cols)
                self.data = arr2
                return self.data
            
            elif choice == 3:
                depth = int(input("Enter the depth for 3D array:- "))
                rows = int(input("Enter the number of rows for 3D array:- "))
                cols = int(input("Enter the number of columns for 3D array:- "))
                arr = input(f"Enter {depth * rows * cols} elements for the array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(depth, rows, cols)
                self.data = arr2
                return self.data
            
            else:
                print("Invalid choice!")

        except :
            print("something went wrong. Please enter the correct number of elements.")
   
    def indexing_operations(self,data):
        try:
            while True:
                print("Choose an option:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go back to main menu")
                choice = int(input("Enter your choice: "))  

                if choice == 1:
                    if data.ndim == 1:
                        inx = int(input("Enter the index of the element to access:- "))
                        print(f"Element at index {inx}: {data[inx]}")

                    elif data.ndim == 2:
                        row = int(input("Enter the row index:- "))
                        col = int(input("Enter the column index:- "))
                        print(f"Element at ({row}, {col}): {data[row, col]}")

                    elif data.ndim == 3:
                        dep = int(input("Enter the depth index:- "))
                        row = int(input("Enter the row index:- "))
                        col = int(input("Enter the column index:- "))
                        print(f"Element at ({dep}, {row}, {col}): {data[dep, row, col]}")

                    else:
                        print("Invalid choice!")

                elif choice == 2:
                    print("Slicing the array:")
                    if data.ndim == 1:
                        start = int(input("Enter the start index:- "))
                        end = int(input("Enter the end index:- "))
                        print(f"Sliced array: {data[start:end]}")

                    elif data.ndim == 2:
                        row_start = int(input("Enter the start row index:- "))
                        row_end = int(input("Enter the end row index:- "))
                        col_start = int(input("Enter the start column index:- "))
                        col_end = int(input("Enter the end column index:- "))
                        print(f"Sliced array:\n{data[row_start:row_end, col_start:col_end]}")

                    elif data.ndim == 3:
                        dep_start = int(input("Enter the start depth index:- "))
                        dep_end = int(input("Enter the end depth index:- "))
                        row_start = int(input("Enter the start row index:- "))
                        row_end = int(input("Enter the end row index:- "))
                        col_start = int(input("Enter the start column index:- "))
                        col_end = int(input("Enter the end column index:- "))
                        print(f"Sliced array:\n{data[dep_start:dep_end, row_start:row_end, col_start:col_end]}")

                    else:
                        print("Invalid choice!")

                elif choice == 3:
                    print("Going to main menu...")
                    break

                else :
                    print("Invalid choice ")
        except :
            print("Invalid input. Please enter a valid choice.")     

    def math_operation(self, data):

        try:
            print()
            print("="*15)
            print("Choose a Mathematical Operation ")
            print("="*15)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = int(input("Enter your choice:- "))

            if choice == 1 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data + arr2
                print("Result of addition:")
                print(result)

            elif choice == 2 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data - arr2
                print("Result of subtraction:")
                print(result)

            elif choice == 3 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data * arr2
                print("Result of multiplication:")
                print(result)

            elif choice == 4 :
                arr = input(f"Enter {data.size} elements for the second array, separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data / arr2
                print("Result of division:")
                print(result)

            else :
                print("Invalid choice!")
 
        except :
            print("Invalid input. Please enter a valid choice.")

    def search_arr(self, data):
        try:
            print()
            print("Choose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")

            choice = int(input("Enter your choice:- "))

            if choice == 1:
                print("Original array:")
                print(data)
                search = int(input("Enter a value to search for:- "))

                if search in data:
                    print("Value found at index:")
                    arr = np.where(data == search)
                    print(arr[0])
                else:
                    print("Value not found in the array.")

            elif choice == 2:
                print("Original array:")
                print(data)
                sort_arr = np.sort(data)
                print("Sorted array:")
                print(sort_arr)

            elif choice == 3:
                print()
                print("Choose a filter:")
                print("1. Values less than")
                print("2. Values greater than")

                choice = int(input("Enter your choice:- "))

                value = int(input("Enter the threshold value:- "))

                if choice == 1:
                    print("Original array:")
                    print(data)
                    print("Filtered array:")
                    less = data[data < value]
                    print(less)

                elif choice == 2:
                    print("Original array:")
                    print(data)
                    print("Filtered array:")
                    greater = data[data > value]
                    print(greater)

                else:
                    print("Invalid choice!")
 
            else :
                print("Invalid choice!")
                
        except :
            print("Invalid input. Please enter a valid choice.")    

    def combine_arrays(self, data):
        try:
            print()
            print("Choose an option:")
            print("1. Combine arrays")
            print("2. Split array")

            choice = int(input("Enter your choice:- "))

            if choice == 1:
                arr = input(f"Enter {data.size} Elements for Another Array: ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                print("Original Array:")
                print(data)
                print("Second Array:")
                print(arr2)
                print("Combined Array (Vertical Stack):")
                new = np.vstack((data, arr2))
                print(new)
 
            elif choice == 2:
                arr1 = int(input("Enter the Number of Splits: "))
                arr2 = np.array_split(data, arr1)
                print("Original Array:")
                print(data)
                print("Split Array:")
                print(arr2)

            else:
                print("Invalid Choice!")
        except:
            print("Something Went Wrong!")

    def Aggregates_operations(self, data):

        try:
  
            print()
            print("Choose an option:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Original array:")
                print(data)
                sum_arr = np.sum(data)
                print(f"Sum of all elements: {sum_arr}")

            elif choice == 2:
                print("Original array:")
                print(data)
                mean_arr = np.mean(data)
                print(f"Mean of all elements: {mean_arr}")

            elif choice == 3:
                print("Original array:")
                print(data)
                median_arr = np.median(data)
                print(f"Median of all elements: {median_arr}")

            else:
                print("Invalid choice!")
        except:
            print("Something went wrong!")

    def main_menu(self):
  
        print()
        print("="*25)
        print("Welcome to Numpy Analyzer !")
        print("="*25)
        print("Choose an choice :")
        print("1. Create a Numpy Array ")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays ")
        print("4. Search, Sort or Filter Arrays ")
        print("5. Compute Aggregates and Statistics ")
        print("6. Exit ")

    def start_program(self):
        while True :
            try :

                self.main_menu()

                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    self.data = obj.create_array()
                    obj.indexing_operations(self.data)

                elif choice == 2:
                    obj.math_operation(self.data)

                elif choice == 3:
                    obj.combine_arrays(self.data)

                elif choice == 4:
                    obj.search_arr(self.data)

                elif choice == 5:
                    obj.Aggregates_operations(self.data) 

                elif choice == 6:   
                    print("Thank You for using Numpy Analyzer! Goodbye!")
                    break

                else:
                    print("Invalid choice! Please try again.")
            except:
                print("Invalid input. Please enter a valid choice.")


obj=DataAnalytics()
obj.start_program()

