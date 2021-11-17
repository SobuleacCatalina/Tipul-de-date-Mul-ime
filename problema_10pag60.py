import itertools 
multime={1,2,3,4}
def submultimi(x):
    return [c for i in range(len(x)+1) for c in itertools.combinations(x,i)]
print('Submultimile multimii {1,2,3,4} sunt = ',submultimi(multime))