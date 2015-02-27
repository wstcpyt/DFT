__author__ = 'yutongpang'
from jasp import *
from ase import Atoms,Atom
import numpy as np
np.set_printoptions(precision=3, suppress=True)

atoms = Atoms([Atom('C',[0,   0, 0]),
               Atom('O',[1.2, 0, 0])])

L = [4, 5, 6, 8, 10]

volumes, energies = [], []