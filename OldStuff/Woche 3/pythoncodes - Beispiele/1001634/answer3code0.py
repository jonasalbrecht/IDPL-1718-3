A = numpy.matrix(numpy.random.random((18, 1))) # as noted by others, your dimensions are off
B = numpy.matrix(numpy.random.random((25, 18)))
C = A.T * B.T * (B * B.T).I
