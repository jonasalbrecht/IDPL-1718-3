yToFind = 140
yreduced = np.array(y) - yToFind
freduced = interpolate.UnivariateSpline(x, yreduced, s=0)
freduced.roots()
