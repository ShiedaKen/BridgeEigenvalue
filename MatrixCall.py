from SMatrix import *
from EigenvalueFind import powerInv

# Create beams
A = BeamMatrix(0)
B = BeamMatrix(np.pi/4)
C = BeamMatrix(np.pi/2)
D = BeamMatrix(0)
g0, g1, g2, g3 = BeamMatrix.GlobalMatrix(1)     # Matrix Diagonals

# Reset BeamMatrix class
BeamMatrix.reset()

E = BeamMatrix(0)
F = BeamMatrix(3*np.pi/4)
G = BeamMatrix(np.pi/2)
g4, g5, g6, g7 = BeamMatrix.GlobalMatrix(1)
g0[-2:] += g4[0:2]      # Overlapping diagonals
g1[-1:] += g5[0:1]
MidDiag = np.concatenate((g0, g4[2:]))      # Main Matrix diagonal
Off1 = np.concatenate((g1, g5[1:]))         # Main Matrix diagonal
Off2 = np.concatenate((g2, g6))             # Main Matrix diagonal
Off3 = np.concatenate((g3, g7))             # Main Matrix diagonal
Off3 = np.pad(Off3, (2, 0), 'constant', constant_values=0)
Off3 = np.pad(Off3, 2, 'constant', constant_values=0)
a = np.diag(MidDiag)
b = np.diag(Off1, k=1)
c = np.diag(Off2, k=2)
d = np.diag(Off3, k=3)
m = a+b+c+d         # Create main matrix
m += m.T - np.diag(np.diag(m))          # Fill based on symmetry
print(np.sqrt(powerInv(m, 1)[0]))
