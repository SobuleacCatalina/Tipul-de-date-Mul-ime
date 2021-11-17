import itertools 
multime={'A','B','C','D'}
def submultimi(x):
    return [c for i in range(len(x)+1) for c in itertools.combinations(x,i)]
print('Submultimile multimii {A,B,C,D} sunt = ',submultimi(multime))