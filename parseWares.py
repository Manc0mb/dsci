import numpy as np
# parse affinity analysis files
def parseWares(fileName):
    uniqdata = []
    with open(fileName,'r') as f:
        lines = list(enumerate(f.read().splitlines()))
        for num,line in lines:
            uniqdata +=(line.split(","))
        uniqdata = list(set(uniqdata))
        linenum=num+1
        darray = np.zeros((linenum,len(uniqdata)))
        for i,line in lines:
            for elem in line.split(","):
                j = uniqdata.index(elem)
                darray[i,j]=1
    return uniqdata,darray
