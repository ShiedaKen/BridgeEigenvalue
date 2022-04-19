import numpy as np


def max_element(a):
    """
    :param a: Matrix
    :return: Greatest element of a
    """
    max_el = abs(a[0])
    for i in range(len(a)):
        if abs(a[i]) > max_el:
            max_el = abs(a[i])
    return max_el


def powerInv(a, x=1, tol=10e-9):
    """
    :param a: Matrix
    :param x: Guess vector
    :param tol: Tolerance
    :return: Smallest Eigenvalue and corresponding eigenvector
    """
    x = np.full(len(a), x, dtype='float')
    a = np.linalg.pinv(a)
    x1 = a@x
    while True:
        xi_max = max_element(x1)
        x = x1/xi_max
        x1 = a@x
        x1_max = max_element(x1)
        if abs(x1_max - xi_max) < tol:
            break
    if np.sign(x1[0]) != np.sign(x[0]):
        x1_max = -x1_max
    return 1/x1_max, x