x = [70, 80, 90, 100, 110]
y = [49.7, 80.6, 122.5, 153.8, 163.0]
f = interpolate.UnivariateSpline(x, y, s=0)
xnew = np.arange(70,111,1)

plt.plot(x,y,'x',xnew,f(xnew))
