class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    
    def __init__(self,first_terms = [0,1]):
        self.seq = first_terms
    
    def N(self,n):
        while len(self.seq) < n:
            self.seq.append(self.seq[-1]+self.seq[-2])
        return self.seq
    
    def N_M(self,n,m):
        sq = np.array(self.N(n))
        return sq[sq % m == 0]

N = int(eval('Input N: '))
M = int(eval('Input M: '))
print(Fibonacci().N_M(N,M))