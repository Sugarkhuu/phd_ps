import numpy as np

def AD_eq(w,util):
    nagent = len(w)
    nprod  = len(w[0])
    shares = np.empty((nagent, nprod))
    for agent in range(nagent):
        for prod in range(nprod): 
            shares[agent][prod] = util[agent][prod]/sum(util[agent])   
    AE = np.zeros((nprod, nprod))
    BE = np.zeros((nprod, nprod))
    for date in range(nprod):
        BE[date][date] = w[0][date]+w[1][date]
        for price in range(nprod):
            AE[date][price] = shares[0][date]*w[0][price] + shares[1][date]*w[1][price]
    A = AE[1:,1:]
    C = AE[1:,0]
    B = BE[1:,1:]
    A = B-A
    print("shares is: {}".format(shares))
    print("AE is: {}".format(AE))
    print("BE is: {}".format(BE))
    print("A is: {}".format(A))
    print("B is: {}".format(B))
    print("C is: {}".format(C))
    
    cont_p = list(C.dot(np.linalg.inv(A)))
    p = [1,cont_p[0],cont_p[0]]
    w = np.array(w)
    W = w.dot(p)
    ww = (W*np.ones((3,2))).T*shares
    qq = ww/p
    
    return p, qq

# baseline
w = [[10.5,8,0],[10.5,0,8]]
util = [[1,1/2,1/2],[1,1/2,1/2]]
p,qq = AD_eq(w,util)
print(p,qq)

# lower future
w = [[10.5,4,0],[10.5,0,4]]
util = [[1,1/2,1/2],[1,1/2,1/2]]
p = [1].append(AD_eq(w,util))
print(p,qq)

# only one has future
w = [[10.5,4,4],[10.5,0,0]]
util = [[1,1/2,1/2],[1,1/2,1/2]]
p,qq = AD_eq(w,util)
print(p,qq)

# i=1 believes in s1 - ERROR here!
w = [[10.5,8,0],[10.5,0,8]]
util = [[1,1,1/2],[1,1/2,1/2]]
p,qq = AD_eq(w,util)
print(p,qq)

