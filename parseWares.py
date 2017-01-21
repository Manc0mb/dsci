import numpy as np
# parse affinity analysis files
def parseWares(fileName):
    uniqdata = []
    with open(fileName,'r') as f:
        lines = list(enumerate(f.read().splitlines()))
        uniqdata = list(set([c for y,x in lines for c in x.split(",") ]))
        darray = np.zeros((len(lines),len(uniqdata)))
        for i,line in lines:
            for elem in line.split(","):
                j = uniqdata.index(elem)
                darray[i,j]=1
    return uniqdata,darray
a,b=parseWares("text")
print(a)
print(b)
