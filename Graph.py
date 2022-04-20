from SMatrix import *
from EigenvalueFind import powerInv
import matplotlib.pyplot as plt

a_l = np.arange(0.25, 10, 0.001)
k_val = np.zeros(len(a_l))
for i in range(len(a_l)):
    k_val[i] = k(a_l[i], 200, 200)
e_l = np.zeros(len(a_l), dtype='float')


def fn(k):
    A = BeamMatrix(0, k)
    B = BeamMatrix(np.pi / 4, k)
    C = BeamMatrix(np.pi / 2, k)
    D = BeamMatrix(0, k)
    g0, g1, g2, g3 = BeamMatrix.GlobalMatrix(1)  # Matrix Diagonals

    # Reset BeamMatrix class
    BeamMatrix.reset()

    E = BeamMatrix(0, k)
    F = BeamMatrix(3 * np.pi / 4, k)
    G = BeamMatrix(np.pi / 2, k)
    g4, g5, g6, g7 = BeamMatrix.GlobalMatrix(1)
    g0[-2:] += g4[0:2]  # Overlapping diagonals
    g1[-1:] += g5[0:1]
    MidDiag = np.concatenate((g0, g4[2:]))  # Main Matrix diagonal
    Off1 = np.concatenate((g1, g5[1:]))  # Main Matrix diagonal
    Off2 = np.concatenate((g2, g6))  # Main Matrix diagonal
    Off3 = np.concatenate((g3, g7))  # Main Matrix diagonal
    Off3 = np.pad(Off3, (2, 0), 'constant', constant_values=0)
    Off3 = np.pad(Off3, 2, 'constant', constant_values=0)
    a = np.diag(MidDiag)
    b = np.diag(Off1, k=1)
    c = np.diag(Off2, k=2)
    d = np.diag(Off3, k=3)
    m = a + b + c + d  # Create main matrix
    m += m.T - np.diag(np.diag(m))  # Fill based on symmetry
    mass = 7231200
    e_v = (np.sqrt(powerInv(m, 1)[0] / mass))
    BeamMatrix.reset()
    return e_v


for i in range(len(k_val)):
    e_l[i] = fn(k_val[i])

plt.plot(a_l, e_l)
plt.xlabel("Cross sectional area (m^2)")
plt.ylabel("Natural frequency (Hz)")
plt.grid()
plt.show()
