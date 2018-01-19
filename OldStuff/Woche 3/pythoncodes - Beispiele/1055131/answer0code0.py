dat = mlab.csv2rec(args[0], delimiter=' ')
m_Obsr = dat.is_observed == 1
m_ZeroScale = dat[m_Obsr].scale_mean < 0.01
the_copy = dat[m_Obsr][m_ZeroScale]

for d in the_copy:
    d.scale_mean = 1.0

newFile = args[0] + ".no-zero-scale"
mlab.rec2csv(the_copy, newFile, delimiter=' ')
