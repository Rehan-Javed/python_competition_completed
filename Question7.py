# Q7 : Given two sorted arrays  A and B, merge into a single array: A[3, 7, 10], B=[1, 2, 4, 5, 6, 9, 11] ==> [1,2,3,5,6,7,9,10,11]

import numpy as np

arr_a = np.array((1, 3, 2, 5, 6))
arr_b = np.array((7, 6, 8, 9, 10))
arr_c = np.concatenate((arr_a, arr_b), axis =0)
print(np.sort(arr_c))


