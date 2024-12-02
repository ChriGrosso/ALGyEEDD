#II.A.1
def edit_distances(str_1: str, str_2: str) -> int:
    distance=0
    i=len(str_1)-1
    j=len(str_2)-1
    while i>=0 and j>=0:
        if(str_1[i]==str_2[j]):
            i=i-1
            j=j-1
        elif(str_1[i-1]==str_2[j]):
            i=i-1
            distance+=1
        elif(str_1[i]==str_2[j-1]):
            j=j-1
            distance+=1
        else:
            i-=1
            j-=1
            distance+=1
    return distance

#II.A.2
def max_subsequence_length(str_1: str, str_2: str)-> int:
    eq=0
    j=0
    for i in range(len(str_1)):
        if(str_1[i]==str_2[j]):
            j+=1
            eq+=1
        elif(str_1[i-1]==str_2[j]):
            i=i-1
        elif(str_1[i]==str_2[j-1]):
            j=j-1
        else:
            i-=1
            j-=1
    return eq
    

#II.A.3
def max_common_subsequence(str_1: str, str_2: str) -> str:
    pass

# #II.B.1 Multiplicacion de matrices
# def min_mult_matrix(l_dims: List[int])-> int:
#     pass

edit_distances("casa","calle")
max_subsequence_length("biscuit","suitcase")