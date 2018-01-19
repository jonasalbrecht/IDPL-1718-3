import MA
a = MA.array([1, 2, None], mask = [0, 0, 1])
print "average =", MA.average(a)
