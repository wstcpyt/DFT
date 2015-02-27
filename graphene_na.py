__author__ = 'yutongpang'
from PyQuante import Molecule

graphene_base_with_Na = Molecule('graphene_base_with_Na',[('C',(0,0,0)),('C',(0,1.42,0)),('C',(1.23,2.13,0)),('C',(2.46,1.42,0)),('C',(2.46,0,0)),('C',(1.23,-0.71,0)),('Na',(1.23,0.71,1.42))],multiplicity=2,units='Angstrom')
h2o=Molecule('h2o',[('O',(0,0,0)), ('H',(1.0,0,0)),('H',(0,1.0,0))],units = 'Angstrom')
from PyQuante.dft import dft
print(graphene_base_with_Na)
print('calculating')
en,orbe,orbs = dft(graphene_base_with_Na)
print(en)