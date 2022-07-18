import decimal

#common floating error

decimal.getcontext().prec = 4
flt_calc = 0.1 + 0.1 + 0.1 - 0.3
dec_calc  = decimal.Decimal("0.1") + decimal.Decimal("0.10") + decimal.Decimal("0.1") - decimal.Decimal("0.3") #has fixed precision
dec_loc_cont = ""
with decimal.localcontext() as ctx:
  ctx.prec = 5 #setting the precision temporarily
  dec_loc_cont = decimal.Decimal(1) / decimal.Decimal(7)
dec_div = decimal.Decimal('1') / decimal.Decimal('7')
