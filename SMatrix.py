import numpy as np
import sys
np.set_printoptions(suppress=True, threshold=sys.maxsize)


class BeamMatrix:
    C0List = []
    C1List = []
    G0List = []
    G1List = []
    G2List = []
    G3List = []
    CF0 = []
    CF1 = []

    def __init__(self, x, k=1):
        c = np.cos(x)
        s = np.sin(x)
        cs = c * s
        c, s = c ** 2, s ** 2
        self.a0 = k * np.array(([c, s, c, s]), dtype='float')
        self.a1 = k * np.array(([cs, -cs, cs]), dtype='float')
        self.a2 = k * np.array(([-c, -s]), dtype='float')
        self.a3 = k * np.array(([-cs]), dtype='float')
        BeamMatrix.CommonAppend(self)

    def CommonAppend(self):
        BeamMatrix.C0List.append(self.a0[2:4])
        BeamMatrix.C1List.append(self.a1[2])
        BeamMatrix.G0List.append(self.a0[0:2])
        BeamMatrix.G1List.append(self.a1[0:2])
        BeamMatrix.G2List.append(self.a2)
        BeamMatrix.G3List.append(self.a3)

    @staticmethod
    def CommonAdd(index):
        A1Arr = BeamMatrix.C0List[0]
        A2Arr = BeamMatrix.C1List[0]
        for n, i in enumerate(BeamMatrix.C0List):
            if n == 0:
                continue
            A1Arr = A1Arr + i
        for n, i in enumerate(BeamMatrix.C1List):
            if n == 0:
                continue
            A2Arr = A2Arr + i
        BeamMatrix.G0List.insert(index, A1Arr)
        BeamMatrix.G1List.insert(index, A2Arr)

    @staticmethod
    def GlobalMatrix(index):
        BeamMatrix.CommonAdd(index)
        g0 = np.concatenate(BeamMatrix.G0List, axis=None)
        g1 = np.concatenate(BeamMatrix.G1List, axis=None)
        g2 = np.concatenate(BeamMatrix.G2List, axis=None)
        g3 = np.concatenate(BeamMatrix.G3List, axis=None)
        return g0, g1, g2, g3

    @classmethod
    def reset(cls):
        BeamMatrix. C0List = []
        BeamMatrix.C1List = []
        BeamMatrix.G0List = []
        BeamMatrix.G1List = []
        BeamMatrix.G2List = []
        BeamMatrix.G3List = []
        BeamMatrix.CF0 = []
        BeamMatrix.CF1 = []


def k(a, e, l):
    return (a*e)/l

