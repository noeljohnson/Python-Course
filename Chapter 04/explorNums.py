##GTG

# prorgam that explores both decimals and fractions

import decimal
from fractions import Fraction

#can set the precision in decimals
decimal.getcontext().prec = 2

d1 = decimal.Decimal('1') / decimal.Decimal('3')

f = Fraction(2, 3)
f += 1
f += Fraction(1, 2)
##TYJC
