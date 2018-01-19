#!/usr/bin/env python

from numpy.linalg.linalg import lstsq



def find_coefficients(data, exponents):
    X = tuple((tuple((pow(x,p) for p in exponents)) for (x,y) in data))
    y = tuple(((y) for (x,y) in data))
    x, resids, rank, s = lstsq(X,y)
    return x

if __name__ == "__main__":
    data = tuple((
        (1.47, 52.21),
        (1.50, 53.12),
        (1.52, 54.48),
        (1.55, 55.84),
        (1.57, 57.20),
        (1.60, 58.57),
        (1.63, 59.93),
        (1.65, 61.29),
        (1.68, 63.11),
        (1.70, 64.47),
        (1.73, 66.28),
        (1.75, 68.10),
        (1.78, 69.92),
        (1.80, 72.19),
        (1.83, 74.46)
    ))
    print find_coefficients(data, range(3))
