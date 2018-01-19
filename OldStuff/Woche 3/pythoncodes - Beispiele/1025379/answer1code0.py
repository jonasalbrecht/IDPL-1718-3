def printarr(arr):
    for x in array:
        if math.floor(x) == x:
            res = '%.1f' % x
        else:
            res = '%.10g' % x
        print "%*s" % (15-res.find('.')+len(res), res)
