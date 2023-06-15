from arcobundle import Arcobundle
from arcosymbol import Arcosymbol
from inversions import Inversion

bundle = Arcobundle([Arcosymbol.KSI, Arcosymbol.LAMBDA, Arcosymbol.GAMMA, Arcosymbol.EPSILON, Arcosymbol.ZETA])

inv_input = Arcobundle([Arcosymbol.KSI, Arcosymbol.LAMBDA, Arcosymbol.GAMMA, Arcosymbol.EPSILON])
inv_output = Arcobundle([Arcosymbol.PHI, Arcosymbol.ZETA, Arcosymbol.THETA, Arcosymbol.OMEGA])
inversion = Inversion(inv_input, inv_output)

print(inversion.apply(bundle))