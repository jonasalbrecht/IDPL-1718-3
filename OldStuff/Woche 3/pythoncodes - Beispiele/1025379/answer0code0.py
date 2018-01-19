import re
ut0 = re.compile(r'(\d)0+$')

thelist = [ut0.sub(r'\1', "%12f" % x) for x in a]

print '\n'.join(thelist)
