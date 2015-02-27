__author__ = 'yutongpang'
from ase.io import write,read

atoms = read('supportfile/graphene_sodium.xyz')
atoms.center(vacuum=5)
print(atoms.get_cell())
write('images/graphene_sodium.png',atoms, show_unit_cell=2,rotation='60x,45y,0z')
