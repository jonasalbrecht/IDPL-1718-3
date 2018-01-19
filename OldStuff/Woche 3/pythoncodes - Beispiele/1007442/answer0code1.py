x1 = a/b; % MRDIVIDE: sparsest solution (min L0 norm) 
x2 = a*pinv(b); % PINV: minimum norm solution (min L2)

>> x1 = a/b
Warning: Rank deficient, rank = 1,  tol = 2.3551e-014.
ans =

    5.0000 0 0 ... 0 

>> x2 = a*pinv(b)
ans =

    0.2 0.2 0.2 ... 0.2 
