class QuantumState:
    def __init__(self, alpha: 'complex', beta: 'complex'):
        self.state = np.empty([alpha, beta])

class ZeroState:
    def __init__(self):
        self.state = np.array([1+0j, 0+0j])

class OneState:
    def __init__(self):
        self.state = np.array([0+0j, 0+1j])
        

class QuantumRegister:
    def __init__(self, n: int):
        #let's start with zero
        self.n_qubits = n
        self.n_states = 1 << n
        self.vector = None
        
        self.qubits_states_sep = np.empty(n, 2)
        self.register_state = None
        
        for i in range(len(self.qubits_states)):
            self.qubits_states_sep[i] = np.array([1+0j, 0+0j])
        
        self.full_state = self.get_full_state()
    
    def get_full_state(self, qubits_states_sep):
        from functools import reduce         
        return reduce(np.kron, qubits_states_sep)
    
    @property
    def get_n(self):
        return self.n
        
        

def hadamard(x, Q):
	codomain = []
	for y in range(Q):
		amplitude = complex(pow(-1.0, bitCount(x & y) & 1))
		codomain.append(Mapping(y, amplitude))

	return  codomain

def hadamard(x, Q):
    """
    :type x: vector state to be Hadamardized
    :type Q: 2^n
    """
    codomain = []
    for y in range(Q):
        amplitude = complex(pow(-1., bit_count(x & y) & 1))
        codomain.append(Mapping(y, amplitude))
    return codomain

def hadamard(x, y_i):
    """
    :type x: vector state to be Hadamardized
    :type Q: 2^n
    """
    return np.complex(pow(-1., bit_count(x & y_i) & 1))