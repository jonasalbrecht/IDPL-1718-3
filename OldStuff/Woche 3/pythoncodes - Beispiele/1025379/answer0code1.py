import re
import textwrap

a = [  5.50056103e+02,   6.77383566e+03,   6.01001513e+05,
         3.55425142e+08,   7.07254875e+05,   8.83174744e+02,
         8.22320510e+01,   4.25076609e+08,   6.28662635e+07,
         1.56503068e+02]

thelist = textwrap.dedent(
        '\n'.join(ut0.sub(r'\1', "%20f" % x) for x in a)).splitlines()

print '\n'.join(thelist)
