from sklearn.metrics.pairwise import rbf_kernel#pairwise_kernels
from dscribe.descriptors import SOAP
from ase.io import read
from dscribe.kernels import AverageKernel
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
species = ["H", "O"]
rcut = 3.5
nmax = 6
lmax = 3
sigma=rcut/8

# Setting up the SOAP descriptor
soap = SOAP(
    species=species,
    periodic=False,
    rcut=rcut,
    nmax=nmax,
    lmax=lmax,
    sigma=sigma
)

mols = read("pos.xyz@:",format="extxyz")
soap_mols = soap.create(mols)
#kernel = rbf_kernel(soap_mols,soap_mols,gamma=1)
print(len(mols))
re = AverageKernel(metric="rbf", gamma=1)
re_kernel = re.create(soap_mols, soap_mols)
#print(re_kernel)
#np.savetxt("g.txt",re_kernel)
for a_index,a in enumerate(re_kernel):
    for b_index,b in enumerate(a):
        if b > 0.95:
            if a_index != b_index:
                print(a_index,b_index)
