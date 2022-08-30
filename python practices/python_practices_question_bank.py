import numpy as np


###############################################################
# arrays operations, math, etc.

# calculate the square distance between two points
def calc_sq_distance(point_a, point_b):
    """
    >>> calc_sq_distance((0,0), (3,4))
    5
    >>> calc_sq_distance((0,0), (0,0))
    0
    >>> val = calc_sq_distance((0,0), (1,1))
    >>> assert np.isclose(val, 1.414)
    True
    """    

# rewrite calc_sq_distance completely using numpy operations
def calc_sq_distance_numpy(point_a, point_b):
    """
    >>> calc_sq_distance((0,0), (3,4))
    5
    >>> calc_sq_distance((0,0), (0,0))
    0
    >>> val = calc_sq_distance((0,0), (100,1))
    >>> assert np.isclose(val, 100)
    True
    """

# find the index of the minimum value given an array:
def find_min_index(arr):
    """
    >>> find_min_index([1,2,3,4])
    0
    >>> find_min_index([0,0,0])
    0
    >>> find_min_index([3,2,1,0])
    3
    """

# find the index of the minimum value in a given array only using numpy operation
def find_min_index_numpy(arr):
    """
    >>> find_min_index([1,2,3,4])
    0
    >>> find_min_index([0,0,0])
    0
    >>> find_min_index([3,2,1,0])
    3
    """

# what about finding the index of the minimum value of each row in a matrix
def find_min_matrix(mat):
    """
    >>> find_min_matrix([[0, 0, 1], [10, 0, 2], [-3, -4, -5]])
    [0, 1, 2]
    >>> find_min_matrix([[100, 1000, 1], [2, 4, 6], [-3, -4, -5], [1.1, 1.2, 1.3]])
    [2, 0, 2, 1]
    >>> find_min_matrix([[3, 2, 1], [-1000, 0, 0], [1.1, 1.01, 1.001], [1, 0.999, 0.998]])
    [2, 0, 2, 2]
    """

# find the index of the minimum value in a given matrix along each row only using numpy operation
def find_min_matrix_numpy(arr):
    """
    >>> index_array = find_min_matrix([[3, 2, 1], [-1000, 0, 0], [1.1, 1.01, 1.001], [1, 0.999, 0.998]])
    >>> assert len(index_array) == 4
    True
    >>> assert isinstance(index_array, np.ndarray)
    True
    >>> index_array
    array([2, 0, 2, 2])
    """

# given an array, assign its minimum value to 1 while all others to 0
def assign_rank(arr):
    """
    >>> rank_matrix = assign_rank([[3, 2, 1], [-1000, 0, 0], [1.1, 1.01, 1.001], [1, 0.999, 0.998]])
    >>> assert isinstance(rank_matrix, np.ndarray)
    True
    >>> rank_matrix.shape
    (4, 3)
    >>> rank_matrix
    array([[0, 0, 1],
           [1, 0, 0],
           [0, 0, 1],
           [0, 0, 1]])
    """

# elementwise addition given two arrays
def add_arrays(arr_1, arr_2):
    """
    >>> add_arrays([1, 2, 3], [1, 1, 1])
    [2, 3, 4]
    >>> add_arrays([1, 2, 3], [0, 0, 0])
    [1, 2, 3]
    # since the two arrays are of differing length, element-wise operation can't be done, return None
    >>> add_arrays([1, 2, 3], [100, 1000]) 
    """

# element wise addition using numpy operations:
def add_arrays_numpy(arr_1, arr_2):
    """
    >>> result_array = add_arrays_numpy([1, 2, 3], [2, 3, 4])
    >>> assert isinstance(result_array, np.ndarray)
    True
    >>> assert len(result_array) == 3
    True
    >>> result_array
    [3, 5, 7]
    """

# square every value of the given array
def square_arrays(arr):
    """
    >>> square_arrays([-1, 1, 0])
    [1, 1, 0]
    >>> square_arrays([-10, -100, 2])
    [100, 10000, 4]
    >>> square_arrays([])
    []
    """

# square every element of an array strictly using numpy operations
def square_arrays_numpy(arr):
    """
    >>> square_arrays_numpy([-1, 1, 0])
    array([1, 1, 0])
    >>> square_arrays_numpy([])
    array([], dtype=float64)
    >>> square_arrays_numpy([1, 2, 3, 4])
    array([ 1,  4,  9, 16])
    """
    
# build an identity matrix with the specified dimension
def build_identity(dim):
    """
    >>> build_identity(0)
    []
    >>> build_identity(1)
    [1]
    >>> build_identity(4)
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    """

# build an identity matrix with the specified dimension strictly using numpy operations
def build_identity_numpy(dim):
    """
    >>> build_identity_numpy(1)
    array([[1.]])
    >>> build_identity_numpy(0)
    array([], shape=(0, 0), dtype=float64)
    >>> build_identity_numpy(3)
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])
    """

# define a matrix of 1's with the specified dimensions
def build_matrix(num_row, num_column):
    """
    >>> build_matrix(3, 4)
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    >>> build_matrix(4, 3)
    [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # below should all return none since either row or column can't be 0
    >>> build_matrix(0, 1)
    >>> build_matrix(1, 0)
    >>> build_matrix(0, 0)
    """

# define a matrix of 1's with the specified dimensions strictly using numpy operations
def build_matrix_numpy(num_row, num_column):
    """
    >>> build_matrix_numpy(4, 3)
    array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]])
    >>> build_matrix_numpy(10, 3)
    array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]])
    # shouldn't be able to create a matrix where row or column is passed in as 0
    >>> buil_matrix_numpy(1, 0)
    array([], shape=(1, 0), dtype=float64)
    """

# define a matrix of any dimension with any aribitrary values using numpy
def build_any_matrix_numpy():
    """
    >>> random_matrix = build_any_matrix_numpy()
    >>> assert isinstance(random_matrix, np.ndarray)
    True
    >>> assert hasattr(random_matrix, 'shape')
    True
    """

# take the sum of two given values
def summation(val_a, val_b):
    """
    >>> summation(1, 1)
    2
    >>> summation(1, -1)
    0
    >>> summation(1.1, 100.1)
    101.2
    """

# take the sum along the rows of a given matrix
def sum_matrix_row(matrix):
    """
    >>> sum_matrix_row([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    [3, 6, 9]
    >>> sum_matrix_row([[-1, 10, np.pi], [100, 1000, 10000], [1, 1, 2]])
    [12.141592653589793, 11100, 4]
    >>> sum_matrix_row([[-3, -2, 100], [333, 333, 333], [0.5, -1.6, -100]])
    [95, 999, -101.1]
    """

# take the sum along the columns of a given matrix
def sum_matrix_column(matrix):
    """
    >>> sum_matrix_column([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    [6, 6, 6]
    >>> sum_matrix_column([[-1, 10, np.pi], [100, 1000, 10000], [1, 1, 2]])
    [100, 1011, 10005.14159265359]
    >>> sum_matrix_column([[-3, -2, 100], [333, 333, 333], [0.5, -1.6, -100]])
    [330.5, 329.4, 333]
    """

# take the sum along the rows of a given matrix strictly using numpy operations
def sum_matrix_row_numpy(matrix):
    """
    >>> result = sum_matrix_row_numpy(np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
    >>> assert result.shape == (3,)
    True
    >>> assert isinstance(result, np.ndarray)
    True
    >>> result
    array([3, 6, 9])
    """

# take the sum along the columns of a given matrix strictly using numpy operations
def sum_matrix_column_numpy(matrix):
    """
    >>> result = sum_matrix_column_numpy([[-3, -2, 100], [333, 333, 333], [0.5, -1.6, -100]])
    >>> assert isinstance(result, np.ndarray)
    True
    >>> result
    array([330.5, 329.4, 333. ])
    """

# take the mean of a given array
def find_mean(arr):
    """
    >>> find_mean([1, 2, 3])
    2
    # if the array has no elements, return none
    >>> find_mean([])
    >>> result = find_mean([1, 1, 2])
    >>> assert np.isclose(result, 1.3333)
    True
    """

# take the mean along the rows of a given matrix
def find_mean_matrix_row(matrix):
    """
    >>> find_mean_matrix_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [2, 5, 8]
    >>> find_mean_matrix_row([[-1, 100, 3], [5, 6, 10], [-3, 6, -9]])
    [34, 7, -2]
    >>> find_mean_matrix_row([0, 0], [1, 0], [0, 1])
    [0, 0.5, 0.5]
    """

# take the mean along the columns of a given matrix
def find_mean_matrix_column(matrix):
    ...

# take the mean along the rows of a given matrix strictly using numpy operations
def find_mean_matrix_row_numpy(matrix):
    ...

# take the mean along the columns of a given matrix strictly using numpy operations
def find_mean_matrix_column_numpy(matrix):
    ...

# append the given element to arr
def add_element_to_list(arr, new_element):
    ...

# append the given element to arr strictly using numpy operations
def add_element_to_numpy_array(arr, new_element):
    ...  

# perform elementwise division using the two arrays
def elementwise_division(arr_1, arr_2):
    ...
    
# perform elementwise division strictly using numpy operations
def elementwise_division_numpy(arr_1, arr_2):
    ...
    
# find the absolute value of the given value
def find_the_absolute_value(input_val):
    ...
   
# collapse a given 2D matrix (list of lists) into a 1D list 
def collapse_matrix(matrix):
    ...

# collapse a np.ndarray into a 1D array
def collapse_numpy_nd_array(arr):
    """
    >>> collapse_numpy_nd_array(np.array([[1, 2], [3, 4]]))
    array([1, 2, 3, 4])
    """
    
###############################################################
# basic python

# loop practices
def print_natural_numbers():
    """
    Print the first 15 natural number (starting from 1)
    
    Ex. 
    print_natural_numbers()
    1
    2
    3
    .
    .
    .
    15
    """
    
def print_natural_numbers_with_input(threshold):
    """
    Given a value, print all natural numbers up to the value.
    If the input value less than the first natural number 1, return None
    Args:
        threshold (int): the upper bound of your natural numbers to be printed
    
    >>> print_natural_numbers_with_input(5)
    1
    2
    3
    4
    5
    >>> print_natural_numbers_with_input(1)
    1
    >>> print_natural_numbers_with_input(0)
    """

def divide_by_2(starting_number):
    """
    Given a starting number, half it until it becomes less than 1. 
    Return the number of times it took to shrink below 1.
    
    Args:
        starting_number (int or float): starting value
    
    >>> divide_by_2(10)
    4
    >>> divide_by_2(2)
    2
    >>> divide_by_2(-1)
    0
    >>> divide_by_2(1.0000001)
    1
    """
    
def calculate_sum_with_input(ending_number):
    """
    Given the ending value, calculate the sum of all natural numbers till (inclusive)
    the ending value. If the input value is already less than 1, return None

    Args:
        ending_number (int): inclusive ending value
        
    >>> calculate_sum_with_input(1)
    1
    >>> calculate_sum_with_input(0)
    >>> calculate_sum_with_input(-100)
    >>> calculate_sum_with_input(10)
    55
    """
    
def calculate_factorial(value):
    """
    Calculate the factorial of the given value
    If the value is less than 0, return None

    Args:
        value (int)
        
    >>> calculate_factorial(3)
    6
    >>> calculate_factorial(0)
    1
    >>> calculate_factorial(-10)
    """
    
def recreate_multiplication_table(value):
    """
    Given a value (it will be between 1 to 9), recreate the mutiplication
    table from 1 up to (inclusive) that value. If the value is invalid, 
    return None

    Args:
        value (int)
        
    >>> recreate_multiplication_table(1)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> recreate_multiplication_table(2)
    1 2
    2 4
    3 6
    4 8
    5 10
    6 12
    7 14
    8 16
    9 18
    >>> recreate_multiplication_table(10)
    >>> recreate_multiplication_table(0)
    """

def find_sum_of_values_at_odd_index(arr):
    """
    Given an array, find the sum of all its odd index values

    Args:
        arr (list): array of values
    
    >>> find_sum_of_values_at_odd_index([])
    0
    >>> find_sum_of_values_at_odd_index([1])
    0
    >>> find_sum_of_values_at_odd_index([1, 2])
    2
    >>> find_sum_of_values_at_odd_index([1, 4, 10, -1, 3, 1.7])
    4.7
    """
    
def display_in_reverse_order(arr):
    """
    Given the array, print all its elements in reversed order.
    If the array contains no elements, return None

    Args:
        arr (list): input array containing arbirary elements
    
    >>> display_in_reverse_order([1, 2, 3, 4, 5])
    5
    4
    3
    2
    1
    >>> display_in_reverse_order([])
    >>> display_in_reverse_order([1, 1, 1])
    1
    1
    1
    """
    
def display_numbers_in_reverse(val):
    """
    Given a value, print all integers starting from that value till 1 (inclusive)
    If the given values is less than 1, function should do nothing

    Args:
        val (int): upper bound value
        
    >>> display_numbers_in_reverse(5)
    5
    4
    3
    2
    1
    >>> display_numbers_in_reverse(0)
    >>> display_numbers_in_reverse(-999)
    """
    

# list exercises
def reverse_list(arr):
    """
    Given a list of elements, return it in reversed order

    Args:
        arr (list): 
    
    >>> reverse_list([])
    []
    >>> reverse_list([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse_list([1, 2, 3, 2, 1])
    [1, 2, 3, 2, 1]
    """
    
def concatenate_two_lists(list_1, list_2):
    """
    Concatenate the two lists into one

    Args:
        list_1 (list)
        list_2 (list)
        
    >>> concatenate_two_lists([], [])
    []
    >>> concatenate_two_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> concatenate_two_lists([], [1])
    [1]
    """
    
def filter_odd_elements(arr):
    """
    Given a list of integers, return a list containing only the odd values

    Args:
        arr (list): list of integers
    
    >>> filter_odd_elements([])
    []
    >>> filter_odd_elements([1, 1, 1])
    [1, 1, 1]
    >>> filter_odd_elements([2, 4, 6])
    []
    >>> filter_odd_elements([1, 2, 3, 4, 5])
    [1, 3, 5]
    """

def add_odd_elements_to_list(list_1, list_2):
    """
    Given two lists, add all odd elements from the second list to the
    first list, then return the extended first list

    Args:
        list_1 (list): first list
        list_2 (list): second list
    
    >>> add_odd_elements_to_list([], [2, 4, 6])
    []
    >>> add_odd_elements_to_list([2, 4, 6], [2, 2, 2])
    [2, 4, 6]
    >>> add_odd_elements_to_list([100, 12, 314, 8002], [1, 10, 100])
    [100, 12, 314, 8002, 1]
    """
    
def display_two_lists(list_1, list_2):
    """
    Given two input lists, iterate through them simultaneously and 
    iteratively display the elements at the same index position;
    if the lists are of differing length, display None

    Args:
        list_1 (list)
        list_2 (list)
    
    >>> display_two_lists([], [])
    >>> display_two_lists([], [1])
    >>> display_two_lists([1, 2], [11, 12])
    1 11 
    2 12
    """
    
def replace_element_in_list(arr, element_to_replace, value_to_replace):
    """
    Iterate through the entire list and replace the target element found 
    in the list with the specified value, then return the list
    target element and value to replace won't be null.

    Args:
        arr (list): full list of elements
        element_to_replace (int, float, or str): target element 
        value_to_replace (int, float, or str): value to replace the target elements with
            if found
            
    >>> replace_element_in_list([], 1, '')
    []
    >>> replace_element_in_list([1, 2, 3, 4], 1, '')
    ['', 2, 3, 4]
    >>> replace_element_in_list(['a', 'b', 'c', 'd', 'e'], 'z', '')
    ['a', 'b', 'c', 'd', 'e']
    """