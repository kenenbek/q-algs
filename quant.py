import numpy as np
from functools import reduce

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
    n = int(rho.shape[1] / P.shape[0])
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

def string_to_state(state): # todo vectorize code
    x = len(state)
    res = np.empty([len(state), 2, 1])
    for i, char in enumerate(state):
        if char == '0':
            res[i] = ZERO
        elif char == '1':
            res[i] = ONE
        else:
            raise Exception
    
    return reduce(np.kron, res)

def transfor_function_to_matrix(qubit_number, func):
    states = 2 ** qubit_number
    res = np.empty([states, states])
    
    for num in range(states):
        state = format(num, '0' + str(qubit_number) + 'b')
        X = state[:-1]
        y = str(int(state[-1]) ^ func(int(X, 2)))
        column = string_to_state(X+y)
        
        res[:, num] = column[:, 0]
    
    return res


