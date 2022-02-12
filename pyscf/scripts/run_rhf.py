## This is a basic python script to run a RHF calculation
## on H2O using PySCF

#!/usr/bin/env python
from pyscf import gto, scf

mol = gto.Mole()
mol.atom = '''
    O  0  0  0
    H  0  1  0
    H  0  0  1'''
mol.unit = 'B'
mol.basis = {'O': 'cc-pvdz', 'H': 'cc-pvdz'}
mol.symmetry = True
#mol.symmetry_subgroup = "C2"
mol.spin=0
mol.charge=0
# mol.max_memory = 1000
mol.verbose=4
mol.build()

mf = scf.RHF(mol)
mf.diis_space = 5
mf.kernel()
print("RHF Calculation over.")
print("---------------------")
mf.dip_moment()
print("Calculationo of dipole moments done")
print("------------------------")
mf.analyze()
print("Analyze done")
print("-----------------")
mf.mulliken_pop()
print("Mulliken population calculation done")
print("-----------------------")
g = mf.Gradients()
g.kernel()
print("Gradient calculation done.")
print("Done")

