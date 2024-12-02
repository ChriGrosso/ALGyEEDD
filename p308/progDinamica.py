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
    """
    Calcula la longitud de la subsecuencia común más larga (LCS) entre dos cadenas.
    Utiliza una cantidad mínima de memoria.
    """
    n, m = len(str_1), len(str_2)
    # Variabile per memorizzare l'LCS attuale
    current = 0

    for i in range(n):
        prev_diagonal = 0  # Valore della cella diagonale precedente
        prev_col = 0      # Valore della cella precedente nella stessa riga
        for j in range(m):
            temp = prev_col  # Conserviamo il valore corrente della colonna
            if str_1[i] == str_2[j]:
                prev_col = prev_diagonal + 1  # Incremento in caso di match
            else:
                prev_col = max(prev_col, current)  # Calcolo del massimo
            prev_diagonal = temp  # Aggiorniamo la diagonale
            current = prev_col  # Memorizziamo il valore attuale

    return current
    

#II.A.3
def max_common_subsequence(str_1: str, str_2: str) -> str:
    pass

# #II.B.1 Multiplicacion de matrices
# def min_mult_matrix(l_dims: List[int])-> int:
#     pass

edit_distances("casa","calle")
max_subsequence_length("biscuit","biscuit")