import numpy as np
 
'''
* Input
    * x       input data
    * k       half window size (full 2*k+1)          
    * thr     threshold (defaut 3), optional
 
* Output
    * output_x    filtered data
    * output_Idx indices of outliers
'''
def Hampel(x, k, thr=3):
    arraySize = len(x)
    idx = np.arange(arraySize)
    output_x = x.copy()
    output_Idx = np.zeros_like(x)
 
    for i in range(arraySize):
        mask1 = np.where( idx >= (idx[i] - k) ,True, False)
        mask2 = np.where( idx <= (idx[i] + k) ,True, False)
        kernel = np.logical_and(mask1, mask2)
        median = np.median(x[kernel])
        std = 1.4826 * np.median(np.abs(x[kernel] - median))
        '''
        print("mask1 =", mask1)
        print("mask2 =", mask2)
        print("kernel =", kernel.astype(int))
        print("x[kernel] =", x[kernel])
        print("median =", median)
        print("std =", std)
        print("")
        '''
        if np.abs(x[i] - median) > thr * std:
            output_Idx[i] = 1
            output_x[i] = median
 
    # return output_x, output_Idx.astype(bool)
    return output_x, output_Idx