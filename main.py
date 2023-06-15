from arcobundle import Arcobundle
from arcosymbol import Arcosymbol

s1 = [ Arcosymbol.KSI, Arcosymbol.LAMBDA, Arcosymbol.LAMBDA, Arcosymbol.KSI]
s2 = [Arcosymbol.LAMBDA, Arcosymbol.KSI, Arcosymbol.LAMBDA, Arcosymbol.EPSILON]

a1 = Arcobundle(s1)
a2 = Arcobundle(s2)
print(a1 == a2)
