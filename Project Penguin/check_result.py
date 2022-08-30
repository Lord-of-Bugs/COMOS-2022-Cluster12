# This script is used to check the student's resulting clustering 
# assignment's total sum of squared distances from running K-Means clustering
import itertools


# global variables
valid_feature_list = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
success_msg = 'You\'ve uncovered the correct number of penguin clusters (species), congratulations!'
fail_msg_1 = 'You may have falsely uncovered too many non-existing species of penguines, try adjust your K; \
or it may just be bad luck due to randomness, try re-run your K-Means alogrithm and see if the result \
changes significantly'
fail_msg_2 = 'You may have failed to uncover enough species of penguines, try adjust your K; \
or it may just be bad luck due to randomness, try re-run your K-Means alogrithm and see if the result \
changes significantly'

# student inputs
feature_1 = str(input('Please provide your first feature:'))
if feature_1 not in valid_feature_list:
    raise KeyError(f'{feature_1} is not a valid feature variable, please make sure your spelling matches exactly')

feature_2 = str(input('Please provide your second feature:'))
if feature_2 not in valid_feature_list:
    raise KeyError(f'{feature_2} is not a valid feature variable, please make sure your spelling matches exactly')

if feature_1 == feature_2:
    raise ValueError('You should provide two different feature names')

student_result_input = float(input(
    'Please provide your clustering result in terms of sum of within-cluster sum of squared distances'
))

possible_feature_combinations = list(itertools.combinations(valid_feature_list, 2))
# ranges constructed using mean +/- 2 * standard deviation
valid_ranges = [
    # culmen_length * culmen_depth
    [2266.0775969547108, 2266.0775969547108],
    # culmen_length * flipper_length
    [14016.439707365647 - 2 * 195.20111639618818, 14016.439707365647 + 2 * 195.20111639618818],
    # culmen_length * body_mass
    [28845006.240518935 - 2 * 184633.98614686567, 28845006.240518935 + 2 * 184633.98614686567],
    # culmen_depth * flipper_length
    [9312.892729461728 - 2 * 400.1862782484602, 9312.892729461728 + 2 * 400.1862782484602],
    # culmen_depth * body_mass
    [28837125.25369629 - 2 * 188454.895919211, 28837125.25369629 + 2 * 188454.895919211],
    # flipper_length * body_mass
    [28857800.99250205 - 2 * 184449.3469116241, 28857800.99250205 + 2 * 184449.3469116241]
]
valid_parameter_ranges = {k:v for k,v in zip(possible_feature_combinations, valid_ranges)}

expected_range = None
try:
    expected_range = valid_parameter_ranges[(feature_1, feature_2)]
except KeyError:
    expected_range = valid_parameter_ranges[(feature_2, feature_1)]

if student_result_input >= expected_range[0] and student_result_input <= expected_range[1]:
    print(success_msg)
else:
    if student_result_input < expected_range[0]:
        print(fail_msg_1)
        print(
            f'We expect your sum of within-cluster sum of squared distances obtained from \
running K-Means on this pair of features to be in the range: {expected_range}'
            )
    elif student_result_input > expected_range[1]:
        print(fail_msg_2)
        print(
            f'We expect your sum of within-cluster sum of squared distances obtained from \
running K-Means on this pair of features to be in the range: {expected_range}'
            )
