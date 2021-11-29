import numpy as np

w = [[10.5,8,0],[10.5,0,8]]
util = [[1,1/2,1/2],[1,1/2,1/2]]

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

C.dot(np.linalg.inv(A))

