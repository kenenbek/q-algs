import numpy as np

ZERO = np.array([[1], [0]])
ONE = np.array([[0], [1]])

def hadamard_n(n):
    """
    return (2^n, 2^n) Hadamard matrix 
    """
    H = (1 / np.sqrt(2)) * np.array([[1, 1],
                [1, -1]])
    res = np.array([[1.]])
    while n > 0:
        res = np.kron(res, H)
        n -= 1
    return res

def measure(state, basis):
    """
    Measure a probability of state to be in basis
    
    Parameters
    ---------- 
    
    """
    
    rho = np.dot(state, state.T)

    P = np.dot(basis, basis.T)
    n = int(rho.shape[1] / P.shape)
    P1 = np.kron(P, np.eye(n))

    prob = np.trace(np.dot(rho, P1))
    return prob

def bit_count(n: int) -> int:    
    """
    Count numbers of '1' in a binary represenation of `n` number.  
    """
    ones = 0
    while n != 0:
        ones += 1
        n &= n-1
    return ones

def bit_count(n: int) -> int:    
    """
    Count numbers of '1' in a binary represenation of `n` number.  
    """
    ones = 0
    while n != 0:
        ones += 1
        n &= n-1
    return ones
